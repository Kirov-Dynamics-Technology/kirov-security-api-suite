from app.services.email_service import analyze_email

def test_clean_email():
    result = analyze_email("Meeting Reminder", "See you at 3pm", "colleague@company.com")
    assert result["risk_level"] == "low"
    assert len(result["flags"]) == 0

def test_phishing_email():
    result = analyze_email(
        "URGENT: Account Suspended",
        "Your account has been suspended. Click here to verify immediately or your account will be closed.",
        "security@bank-verify.com"
    )
    assert result["risk_level"] in ("medium", "high")
    assert len(result["flags"]) > 0
