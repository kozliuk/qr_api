import io

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer


def make_qrcode(
    data: str,
) -> bytes:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        border=1,
        box_size=10,
    )
    qr.add_data(data)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=SquareModuleDrawer(),
    )
    img_io = io.BytesIO()
    img.save(img_io)
    return img_io.getvalue()
