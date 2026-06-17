from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.services.url_service import analyze_url

router = APIRouter(prefix="/url", tags=["URL"])

class UrlRequest(BaseModel):
    url: str = Field(..., min_length=1)

class UrlResponse(BaseModel):
    url: str
    valid: bool
    domain: str | None = None
    risk: str
    flags: list[str]

@router.post("/analyze", response_model=UrlResponse)
def analyze(req: UrlRequest):
    if len(req.url) > 2048:
        return UrlResponse(url=req.url, valid=False, risk="invalid", flags=["URL too long"])
    return analyze_url(req.url)
