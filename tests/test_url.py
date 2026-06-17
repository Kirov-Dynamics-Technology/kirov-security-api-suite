from app.services.url_service import analyze_url

def test_valid_safe_url():
    result = analyze_url("https://github.com")
    assert result["valid"] is True
    assert result["risk"] == "low"

def test_http_url():
    result = analyze_url("http://example.com")
    assert result["valid"] is True
    assert "Uses HTTP instead of HTTPS" in result["flags"]

def test_invalid_url():
    result = analyze_url("not a url")
    assert result["valid"] is False
    assert result["risk"] == "invalid"
