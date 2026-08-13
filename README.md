# Containerized NBA API Data Pipeline

A cloud-native infrastructure lab demonstrating secure application containerization, environmental variable decoupling, and automated data ingestion workflows.

## Technology Stack
* **Runtime Environment:** Docker (Linux Engine Backend)
* **Programming Language:** Python 3.9
* **External Core Libraries:** Requests
* **Data Provider:** RapidAPI (NBA Free Data Architecture Tier)

## Core Engineering Features
* **Credential Decoupling:** Securely isolated private API access tokens from the core source code by leveraging runtime environmental variable injections (`docker run -e`).
* **Dependency Isolation:** Packaged complete system dependencies cleanly inside an isolated Docker image layer, bypassing local host path conflicts.
* **Stream Real-time Data:** Automatically establishes secure network sockets across external web servers to fetch, parse, and output live sports data arrays.
