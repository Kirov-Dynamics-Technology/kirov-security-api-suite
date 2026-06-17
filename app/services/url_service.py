from urllib.parse import urlparse
from app.utils.validators import validate_url, is_suspicious_domain

SUSPICIOUS_KEYWORDS = ["login", "verify", "secure", "account", "update", "banking", "paypal", "password"]

def analyze_url(url: str) -> dict:
    if not validate_url(url):
        return {"url": url, "valid": False, "risk": "invalid", "flags": ["Not a valid URL"]}

    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    flags = []

    if domain.startswith("www."):
        domain = domain[4:]

    if parsed.scheme == "http":
        flags.append("Uses HTTP instead of HTTPS")

    if is_suspicious_domain(domain):
        flags.append("Suspicious domain pattern detected")

    subdomain_count = domain.count(".") - (1 if domain.endswith(".com") or domain.endswith(".org") else 0)
    if subdomain_count > 2:
        flags.append(f"Unusual number of subdomains ({subdomain_count})")

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in domain:
            flags.append(f"Contains suspicious keyword: '{keyword}'")
            break

    risk_level = "low"
    if len(flags) >= 3:
        risk_level = "high"
    elif len(flags) >= 1:
        risk_level = "medium"

    return {
        "url": url,
        "valid": True,
        "domain": domain,
        "risk": risk_level,
        "flags": flags,
    }
