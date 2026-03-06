# ADR 0001: OpenAPI-First API Documentation

## Status

Accepted

## Context

This project aims to demonstrate production-grade engineering practices. API clarity is important for:

- frontend/backend contract alignment
- faster onboarding
- easier integration
- future schema validation and client generation
- portfolio evidence of API maturity

A documented API is especially important because the Angular frontend depends on typed backend responses.

## Decision

Use `drf-spectacular` to generate an OpenAPI schema from Django REST Framework views and serializers, and expose documentation through Redoc.

## Consequences

### Positive

- API contracts are visible through browser-based documentation
- serializers and views directly shape the public API
- frontend typed contracts can mirror backend response structures
- future schema export and contract testing become easier

### Negative

- schema quality depends on serializer/view discipline
- documentation can drift if endpoints are implemented without proper serializer structure

## Follow-up

Future improvements may include:

- exporting OpenAPI artifacts during CI
- automatic TypeScript client generation from schema
- schema diff checks for breaking API changes
