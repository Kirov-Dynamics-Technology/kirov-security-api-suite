from app.services.password_service import analyze_password

def test_weak_password():
    result = analyze_password("password")
    assert result["strength"] in ("weak", "very_weak")
    assert len(result["weaknesses"]) > 0

def test_strong_password():
    result = analyze_password("K1r0v#Dyn4m1c$S3cur3!")
    assert result["strength"] in ("strong", "very_strong")
    assert len(result["weaknesses"]) == 0

def test_entropy_increases_with_complexity():
    simple = analyze_password("abc")
    complex_pwd = analyze_password("K1r0v#Dyn4m1c$S3cur3!")
    assert complex_pwd["entropy_score"] > simple["entropy_score"]
