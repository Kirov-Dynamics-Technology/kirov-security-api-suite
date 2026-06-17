from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.services.email_service import analyze_email

router = APIRouter(prefix="/email", tags=["Email"])

class EmailRequest(BaseModel):
    subject: str = Field(default="")
    body: str = Field(default="")
    sender: str = Field(default="")

class EmailResponse(BaseModel):
    sender: str
    subject: str
    risk_score: int
    risk_level: str
    flags: list[str]

@router.post("/analyze", response_model=EmailResponse)
def analyze(req: EmailRequest):
    if len(req.subject) + len(req.body) > 50000:
        return EmailResponse(sender=req.sender, subject=req.subject,
                             risk_score=0, risk_level="low",
                             flags=["Content too large to analyze"])
    return analyze_email(req.subject, req.body, req.sender)
