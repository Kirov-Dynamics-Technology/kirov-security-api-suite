from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.hash_service import hash_password, verify_password

router = APIRouter(prefix="/hash", tags=["Hash"])

class HashRequest(BaseModel):
    password: str = Field(..., min_length=1)
    algorithm: str = "bcrypt"

class HashResponse(BaseModel):
    algorithm: str
    hash: str

class VerifyRequest(BaseModel):
    password: str = Field(..., min_length=1)
    hash: str = Field(..., min_length=1)
    algorithm: str = "bcrypt"

class VerifyResponse(BaseModel):
    algorithm: str
    valid: bool

@router.post("/generate", response_model=HashResponse)
def generate(req: HashRequest):
    if req.algorithm not in ("bcrypt", "argon2", "sha256"):
        raise HTTPException(400, "Unsupported algorithm. Use: bcrypt, argon2, sha256")
    return hash_password(req.password, req.algorithm)

@router.post("/verify", response_model=VerifyResponse)
def verify(req: VerifyRequest):
    if req.algorithm not in ("bcrypt", "argon2", "sha256"):
        raise HTTPException(400, "Unsupported algorithm. Use: bcrypt, argon2, sha256")
    return verify_password(req.password, req.hash, req.algorithm)
