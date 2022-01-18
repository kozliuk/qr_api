from pydantic import BaseModel


class QrCreate(BaseModel):
    data: str
