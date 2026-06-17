import hashlib
import bcrypt as _bcrypt
from argon2 import PasswordHasher
from app.config import settings

_argon2_hasher = PasswordHasher()

def hash_password(password: str, algorithm: str = "bcrypt") -> dict:
    algorithm = algorithm.lower()
    if algorithm == "bcrypt":
        hashed = _bcrypt.hashpw(password.encode(), _bcrypt.gensalt(rounds=settings.hash_rounds)).decode()
    elif algorithm == "argon2":
        hashed = _argon2_hasher.hash(password)
    elif algorithm == "sha256":
        hashed = hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    return {"algorithm": algorithm, "hash": hashed}

def verify_password(password: str, hash_value: str, algorithm: str = "bcrypt") -> dict:
    algorithm = algorithm.lower()
    if algorithm == "bcrypt":
        valid = _bcrypt.checkpw(password.encode(), hash_value.encode())
    elif algorithm == "argon2":
        try:
            _argon2_hasher.verify(hash_value, password)
            valid = True
        except Exception:
            valid = False
    elif algorithm == "sha256":
        valid = hashlib.sha256(password.encode()).hexdigest() == hash_value
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    return {"algorithm": algorithm, "valid": valid}
