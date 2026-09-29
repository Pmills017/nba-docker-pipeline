# NBA API Data Pipeline with Docker and Kubernetes

A hands-on project practicing containerization and Kubernetes fundamentals by building a small Python app that pulls live NBA stats from an API and runs it as a Kubernetes pod.

## Technology Stack
* **Containerization:** Docker
* **Orchestration:** Kubernetes (local single-node cluster)
* **Programming Language:** Python 3.9
* **Libraries:** Requests
* **Data Source:** RapidAPI's free-tier NBA stats API

## What This Project Demonstrates
* **Keeping secrets out of the code:** The API key is passed in as an environment variable at runtime (`docker run -e API_KEY="..."`) instead of being written directly into the code, so it's never exposed if the code is shared publicly.
* **Packaging with Docker:** All the dependencies the script needs are bundled inside the Docker image, so it runs the same way regardless of what's installed on the host machine.
* **Running it with Kubernetes:** Deployed the container as a pod on a local Kubernetes cluster using `kubectl`.
* **Clean exit:** The Python script is written to finish its work and exit on its own once it's pulled the data, so Kubernetes marks the pod as `Completed` instead of it running indefinitely.

---

## Verification

### 1. Kubernetes Pod Status
The local cluster accepted the container image, ran the Python script inside it, and marked the pod `Completed` once the data pull finished.

<img width="815" height="231" alt="kubernetes" src="https://github.com/user-attachments/assets/9b4a35e1-7f3f-403f-9aac-135326fed308" />

### 2. Data Output
The logs show the script connecting to the RapidAPI endpoint, authenticating with the API key, and successfully pulling the live NBA data.

<img width="1460" height="657" alt="nba-data" src="https://github.com/user-attachments/assets/7e1b0260-b2c9-4ca2-9d62-be8dce92dcc9" />
