from fastapi import FastAPI
from app.config import settings
from app.routes import password, url, hash, email

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Production-ready security microservice API for analyzing passwords, URLs, hashing, and email risk classification.",
)

app.include_router(password.router)
app.include_router(url.router)
app.include_router(hash.router)
app.include_router(email.router)

@app.get("/")
def root():
    return {"service": settings.app_name, "version": settings.app_version, "status": "operational"}

@app.get("/health")
def health():
    return {"status": "UP", "service": "kirov-security-api-suite"}
