from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.password_service import analyze_password

router = APIRouter(prefix="/password", tags=["Password"])

class PasswordRequest(BaseModel):
    password: str = Field(..., min_length=1)

class PasswordResponse(BaseModel):
    entropy_score: float
    strength: str
    length: int
    weaknesses: list[str]

@router.post("/analyze", response_model=PasswordResponse)
def analyze(req: PasswordRequest):
    if len(req.password) > 1000:
        raise HTTPException(400, "Password too long")
    return analyze_password(req.password)
