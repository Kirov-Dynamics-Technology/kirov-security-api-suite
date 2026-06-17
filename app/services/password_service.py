import re
from math import log2
from app.utils.validators import count_entropy

COMMON_PASSWORDS = {"password", "123456", "12345678", "qwerty", "admin", "letmein", "welcome", "monkey", "dragon", "master"}

def analyze_password(password: str) -> dict:
    weaknesses = []
    if password.lower() in COMMON_PASSWORDS:
        weaknesses.append("Common password")
    if len(password) < 8:
        weaknesses.append("Too short (minimum 8 characters)")
    if not re.search(r'[a-z]', password):
        weaknesses.append("Missing lowercase letter")
    if not re.search(r'[A-Z]', password):
        weaknesses.append("Missing uppercase letter")
    if not re.search(r'[0-9]', password):
        weaknesses.append("Missing digit")
    if not re.search(r'[^a-zA-Z0-9]', password):
        weaknesses.append("Missing special character")
    if len(set(password)) < len(password) * 0.5:
        weaknesses.append("Too many repeated characters")

    entropy = count_entropy(password)
    if entropy >= 80:
        strength = "very_strong"
    elif entropy >= 60:
        strength = "strong"
    elif entropy >= 40:
        strength = "moderate"
    elif entropy >= 20:
        strength = "weak"
    else:
        strength = "very_weak"

    return {
        "entropy_score": round(entropy, 2),
        "strength": strength,
        "length": len(password),
        "weaknesses": weaknesses,
    }
