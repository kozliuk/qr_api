from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="")


@router.get("/health")
def health():
    return HTMLResponse("<div style='font-size: 72px'>It works</div>")
