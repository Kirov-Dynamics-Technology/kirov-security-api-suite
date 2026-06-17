from app.services.hash_service import hash_password, verify_password

def test_bcrypt_hash_and_verify():
    result = hash_password("TestPassword123!")
    assert result["algorithm"] == "bcrypt"
    assert result["hash"].startswith("$2b$")

    verified = verify_password("TestPassword123!", result["hash"])
    assert verified["valid"] is True

def test_sha256_hash_and_verify():
    result = hash_password("TestPassword123!", "sha256")
    assert result["algorithm"] == "sha256"
    assert len(result["hash"]) == 64

    verified = verify_password("TestPassword123!", result["hash"], "sha256")
    assert verified["valid"] is True

def test_wrong_password_rejected():
    result = hash_password("RealPassword1!")
    verified = verify_password("WrongPassword1!", result["hash"])
    assert verified["valid"] is False
