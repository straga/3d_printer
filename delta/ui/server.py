from pathlib import Path
from aiohttp import web
import asyncio

static_dir_path = Path('/opt/printer/ui/fluidd')

@web.middleware
async def static_serve(request, handler):
    relative_file_path = Path(request.path).relative_to('/')  # remove root '/'
    file_path = static_dir_path / relative_file_path  # rebase into static dir
    if not file_path.exists():
        return web.HTTPNotFound()
    if file_path.is_dir():
        file_path /= 'index.html'
        if not file_path.exists():
            return web.HTTPNotFound()
    return web.FileResponse(file_path)

# app = web.Application(middlewares=[static_serve])
# web.run_app(app)

import logging

stdio_handler = logging.StreamHandler()
stdio_handler.setLevel(logging.INFO)
_logger = logging.getLogger('aiohttp.access')
_logger.addHandler(stdio_handler)
_logger.setLevel(logging.ERROR)
app = web.Application(logger=_logger, middlewares=[static_serve])
web.run_app(app, port=8080)

