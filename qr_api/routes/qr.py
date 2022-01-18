from fastapi import APIRouter, Response
from loguru import logger

from ..qr import make_qrcode
from ..models.qr import QrCreate

router = APIRouter(prefix="")


@router.post("/qr")
def qr(qr_create: QrCreate):
    try:
        return Response(
            status_code=200,
            content=make_qrcode(data=qr_create.data),
            media_type="image/png",
        )
    except Exception as err:
        logger.exception(f"Error happened: {err}")
        return Response(status_code=500)
