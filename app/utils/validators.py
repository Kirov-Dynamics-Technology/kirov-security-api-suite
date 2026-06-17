import re

def validate_url(url: str) -> bool:
    return bool(re.match(r'^https?://[^\s/$.?#].[^\s]*$', url))

def is_suspicious_domain(domain: str) -> bool:
    suspicious_patterns = [
        r'secure-', r'login-', r'verify-', r'update-', r'account-',
        r'\.xyz$', r'\.top$', r'\.click$', r'\.gq$', r'\.ml$', r'\.cf$',
    ]
    domain_lower = domain.lower()
    return any(re.search(p, domain_lower) for p in suspicious_patterns)

def count_entropy(password: str) -> float:
    from math import log2
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset += 32
    return len(password) * log2(charset) if charset else 0
