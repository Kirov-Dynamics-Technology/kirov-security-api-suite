# Kirov Security API Suite — Documentation

## Endpoints

### Password Analysis
`POST /password/analyze`
- Request: `{ "password": "..." }`
- Response: `{ "entropy_score": 72.5, "strength": "strong", "length": 16, "weaknesses": [] }`

### URL Risk Analysis
`POST /url/analyze`
- Request: `{ "url": "https://..." }`
- Response: `{ "url": "...", "valid": true, "domain": "...", "risk": "low", "flags": [] }`

### Hash Generation
`POST /hash/generate`
- Request: `{ "password": "...", "algorithm": "bcrypt" }`
- Response: `{ "algorithm": "bcrypt", "hash": "$2b$12$..." }`
- Algorithms: bcrypt, argon2, sha256

### Hash Verification
`POST /hash/verify`
- Request: `{ "password": "...", "hash": "...", "algorithm": "bcrypt" }`
- Response: `{ "algorithm": "bcrypt", "valid": true }`

### Email Risk Analysis
`POST /email/analyze`
- Request: `{ "subject": "...", "body": "...", "sender": "..." }`
- Response: `{ "risk_score": 75, "risk_level": "high", "flags": [...] }`

### Health
`GET /health`
- Response: `{ "status": "UP", "service": "kirov-security-api-suite" }`
