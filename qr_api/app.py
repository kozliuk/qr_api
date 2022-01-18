from fastapi import FastAPI
from loguru import logger

from . import routes
from .version import __version__

logger.info(f"App started. Version {__version__}")
app = FastAPI(version=__version__)
app.include_router(routes.service.router)
app.include_router(routes.qr.router)
