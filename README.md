# PolicyPulse — AI Governance + Audit Ledger for Real Decisions
**Educational Purpose & Skills Showcase:** This repository is a portfolio project designed to demonstrate production-grade engineering practices including security-by-design, AI governance, observability, and enterprise-grade type safety. It is not intended for real-world regulatory use without independent security review, legal review, and domain validation.
---
## Overview
PolicyPulse is a RegTech-style decisioning service that records an audit-grade provenance trail for each decision.
The current **Day Zero implementation** demonstrates:
- Django backend with REST endpoints
- OpenAPI documentation via drf-spectacular
- Health endpoint for operational readiness
- Angular frontend using strict TypeScript
- Typed API contracts between frontend and backend
- AI governance scaffolding for prompt management and evaluation
---
## Architecture
### Backend
- Django
- Django REST Framework
- drf-spectacular (OpenAPI schema + Redoc)
- SQLite for local development
- PostgreSQL-ready via `DATABASE_URL`
- Redis-ready cache configuration
### Frontend
- Angular
- strict TypeScript configuration
- standalone Angular bootstrap
- typed service layer calling the API
### Governance and Operations
- pre-commit hooks
- secret scanning mock
- dependency vulnerability scanning
- prompt catalog scaffolding
- evaluation artifact scaffolding
- correlation ID middleware
- health check endpoint
---
## Repository Layout
```
policypulse/
│
├── api/ # Django backend
├── client/ # Angular frontend
├── ai_governance/ # Prompt catalog + evaluation artifacts
├── docs/adr/ # Architecture decision records
├── infra/ # Docker / Kubernetes scaffolding
├── scripts/ # Developer automation scripts
│
├── docker-compose.yml
└── README.md
````
---
## Local Development
### Backend
Run the Django backend:
```powershell
cd api
.\.venv\Scripts\Activate.ps1
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py runserver
````
Backend URLs:
```
http://127.0.0.1:8000/api/docs/redoc/
http://127.0.0.1:8000/api/ops/health
```
---
### Frontend
Run the Angular client:
```powershell
cd client\policypulse-client
npm run lint
ng serve --proxy-config proxy.conf.json
```
Frontend URL:
```
http://localhost:4200
```
---
## Current Day Zero Behavior
### Decision endpoint
```
POST /api/decisions/submit
```
Current behavior:
* accepts a typed JSON payload
* writes a decision record
* returns deterministic outcome `"review"`
* includes provenance data
* includes a correlation ID
Example response:
```json
{
"decision_id": "...",
"product": "loan_precheck",
"applicant_id": "applicant-token-123",
"outcome": "review",
"reason_codes": ["INSUFFICIENT_EVIDENCE"]
}
```
---
### Health endpoint
```
GET /api/ops/health
```
Checks:
* database connectivity
* Redis connectivity
Example response:
```json
{
"service": "policypulse-api",
"database": true,
"redis": false
}
```
A `503` status may occur locally if Redis is not running.
---
## Security-by-Design
The repository demonstrates several defensive engineering practices:
* pre-commit hooks blocking obvious credential patterns
* dependency scanning using `pip-audit` and `safety`
* correlation ID tracing for requests
* configurable environment variables for secrets and infrastructure
---
## AI Governance
The repository includes governance scaffolding:
* prompt catalog
* evaluation artifacts
* PII restrictions
* governance ownership and review placeholders
These files demonstrate how LLM systems can be managed with auditability and structured governance.
---
## Current Project Status
Day Zero includes:
* monorepo scaffold
* Django API
* Angular frontend
* API documentation
* typed contracts
* Git workflow
* governance scaffolding
* developer security tooling
---
## Planned Next Steps
Future improvements include:
* Docker-based local infrastructure
* PostgreSQL and Redis containers
* improved health semantics for local demos
* CI/CD pipeline
* automated prompt evaluation
* GitHub publishing
---
## License
This repository is intended for educational and portfolio purposes.
