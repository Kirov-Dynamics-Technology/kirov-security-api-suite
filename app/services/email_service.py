import re
from urllib.parse import urlparse

PHISHING_KEYWORDS = [
    "urgent", "suspended", "verify", "account", "login", "credential",
    "unusual activity", "security alert", "click here", "confirm",
    "restricted", "limited", "blocked", "unauthorized",
]

URGENCY_PATTERNS = [
    r"\bimmediately\b", r"\bwithin \d+ (hours?|days?)\b",
    r"\bfailure to\b", r"\byour account will be\b",
    r"\bact now\b", r"\bexpir(e|ed|ing)\b",
]

def analyze_email(subject: str, body: str, sender: str) -> dict:
    text = f"{subject} {body}".lower()
    flags = []

    keyword_hits = [kw for kw in PHISHING_KEYWORDS if kw in text]
    if keyword_hits:
        flags.append(f"Phishing keywords found: {', '.join(keyword_hits[:5])}")

    urgency_hits = [p for p in URGENCY_PATTERNS if re.search(p, text)]
    if urgency_hits:
        flags.append("Urgency language detected")

    urls = re.findall(r'https?://[^\s]+', text)
    suspicious_urls = 0
    for url in urls[:10]:
        domain = urlparse(url).netloc.lower()
        if domain.startswith("www."):
            domain = domain[4:]
        if domain.count(".") > 2:
            suspicious_urls += 1

    if suspicious_urls > 0:
        flags.append(f"Contains {suspicious_urls} suspicious URL(s)")

    risk_score = len(flags) * 25
    risk_score = min(risk_score, 100)

    risk_level = "low"
    if risk_score >= 75:
        risk_level = "high"
    elif risk_score >= 50:
        risk_level = "medium"
    elif risk_score >= 25:
        risk_level = "suspicious"

    return {
        "sender": sender,
        "subject": subject,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "flags": flags,
    }
