import asyncio
import os
import sys
from dataclasses import dataclass
from typing import List

import aiodns
from aiohttp import web
from aiohttp.test_utils import TestServer
from aiohttp.web import Application
from aiohttp.web_exceptions import HTTPException
from aiohttp.web_middlewares import middleware
from aiohttp.web_response import Response, json_response
from async_timeout import timeout


async def return_any_status(request):
    status = int(request.match_info['status'])
    # TODO how do we deal with 301 extra which should have the "Location" header
    return Response(text=f'test response with status {status}', status=status)


async def grecaptcha_dummy(request):
    data = await request.post()
    request['log_msg'] = 'grecaptcha {response}'.format(**data)
    if data['response'] == '__ok__':
        return json_response(dict(success=True, hostname='127.0.0.1'))
    elif data['response'] == '__400__':
        return json_response({}, status=400)
    else:
        return json_response(dict(success=False, hostname='127.0.0.1'))


@middleware
async def log_middleware(request, handler):
    try:
        r = await handler(request)
    except Exception as e:
        status = e.status if isinstance(e, HTTPException) else 500
        request.app['log'].append(f'{request.method} {request.path_qs} > {status}')
        raise
    else:
        log = f'{request.method} {request.path_qs} > {r.status}'
        if 'log_msg' in request:
            log += ' ({})'.format(request['log_msg'])
        request.app['log'].append(log)
        return r


def create_dummy_app() -> Application:
    app = web.Application(middlewares=(log_middleware,))
    app.add_routes(
        [
            web.route('*', r'/status/{status:\d+}/', return_any_status, name='any-status'),
            web.post('/grecaptcha_url/', grecaptcha_dummy, name='grecaptcha-dummy'),
        ]
    )
    app['log'] = []
    return app


@dataclass
class DummyServer:
    server: TestServer
    app: Application
    log: List
    server_name: str


async def create_dummy_server(create_server, *, extra_routes=None, extra_context=None) -> DummyServer:
    app = create_dummy_app()
    if extra_routes:
        app.add_routes(extra_routes)
    if extra_context:
        app.update(extra_context)
    server = await create_server(app)
    return DummyServer(server, app, app['log'], f'http://localhost:{server.port}')


class Offline:
    """
    Lazy pytest decorator to skip tests if you're currently not online.

    Usage:
        _offline = Offline()
        skip_if_offline = pytest.mark.skipif(_offline, reason='not online')
    """

    def __init__(self):
        self.is_offline = None

    def __bool__(self):
        if self.is_offline is None:
            loop = asyncio.new_event_loop()
            self.is_offline = loop.run_until_complete(self._check())
        return self.is_offline

    async def _check(self):
        if os.getenv('CI'):
            # on CI we should always be online
            # I assume that all CI services set the CI environment variable!
            return False

        resolver = aiodns.DNSResolver()
        try:
            with timeout(1):
                await resolver.query('google.com', 'A')
        except (aiodns.error.DNSError, asyncio.TimeoutError) as e:
            print(f'\nnot online: {e.__class__.__name__} {e}\n', file=sys.stderr)
            return True
        else:
            return False
