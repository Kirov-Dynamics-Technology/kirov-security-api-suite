# Kirov Security API Suite

Cybersecurity • AI Analysis • Risk Scoring

A production-ready security microservice API for analyzing passwords, URLs, hashing, and email risk classification.

## Features

- **Password Strength Analysis** — entropy scoring with weakness detection
- **URL Risk Checker** — phishing domain detection and risk scoring
- **Hashing Service** — bcrypt, argon2, and SHA-256
- **Email Phishing Classifier** — rule-based risk analysis

## Quick Start

```bash
docker compose up -d
curl http://localhost:8000/health
```

## API Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/password/analyze` | Analyze password strength |
| POST | `/url/analyze` | Check URL for risk indicators |
| POST | `/hash/generate` | Hash a password |
| POST | `/hash/verify` | Verify a password against a hash |
| POST | `/email/analyze` | Analyze email for phishing risk |
| GET | `/health` | Service health check |

## Stack

- **FastAPI** (Python 3.12)
- **Docker** / Docker Compose
- **pytest** for testing
- **passlib** for bcrypt/argon2

## Built by Kirov Dynamics Technology

Cybersecurity + AI Engineering Systems

[GitHub](https://github.com/Raphasha27)

## Deployment & Architecture

This project is designed with cloud-ready principles:

- **Containerized** using Docker for consistent deployment
- **Environment-based configuration** — no hardcoded secrets
- **Modular structure** for independent scaling
- **Stateless design** where applicable
- **Separation of concerns** for maintainability

### Run Locally

`ash
docker-compose up --build
`

---

*Part of the Kirov Dynamics Technology portfolio — backend engineering focused on security, scalability, and system design.*
