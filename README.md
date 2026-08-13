# Containerized NBA API Data Pipeline & Kubernetes Workload

A cloud-native infrastructure lab demonstrating secure application containerization, environmental variable decoupling, and automated cluster orchestration workflows.

## Technology Stack
* **Runtime Environment:** Docker (Linux Engine Backend Engine via WSL 2)
* **Orchestration Layer:** Kubernetes (Local Single-Node Cluster Engine)
* **Programming Language:** Python 3.9
* **External Core Libraries:** Requests
* **Data Provider:** RapidAPI (NBA Free Data Architecture Tier)

## Core Engineering Features Verified
* **Credential Decoupling:** Securely isolated private API access tokens from the core source code by leveraging runtime environmental variable injections (`docker run -e API_KEY="..."`).
* **Dependency Isolation:** Packaged complete system dependencies cleanly inside an isolated Docker image layer, bypassing local host path conflicts or missing runtime utilities.
* **Orchestration Lifecycle:** Successfully deployed the custom image configuration as an active pod workload inside a local Kubernetes cluster manager using the `kubectl` CLI tool.
* **Self-Terminating Design:** Configured the underlying Python execution scripts to gracefully exit upon completing the remote data payload stream, allowing the cluster scheduler to mark the node lifecycle state as cleanly `Completed`.

---

## Technical Deployment Verification Logs

### 1. Local Kubernetes Cluster Pod Execution Status
The Single-Node cluster accepted the container image deployment, provisioned the operational pod, executed the underlying python ingestion layers, and shifted the state to `Completed` once the data cycle finished.

<img width="815" height="231" alt="kubernetes" src="https://github.com/user-attachments/assets/9b4a35e1-7f3f-403f-9aac-135326fed308" />


### 2. Streamed Container Data Ingestion Payload Output
The internal logs verify that the application successfully opened a network socket across the web, authenticated the runtime environment variables against the RapidAPI gateway, and extracted the live data payload.

<img width="1460" height="657" alt="nba-data" src="https://github.com/user-attachments/assets/7e1b0260-b2c9-4ca2-9d62-be8dce92dcc9" />



