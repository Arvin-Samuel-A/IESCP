# IESCP – Influencer–Sponsor Engagement & Campaign Platform

## Project Overview

IESCP (Influencer–Sponsor Engagement & Campaign Platform) is a role‑based web application designed to facilitate structured, transparent, and governed collaborations between sponsors (brands) and influencers (content creators). The platform enables sponsors to create advertising campaigns, discover suitable influencers, negotiate campaign terms, and track outcomes, while influencers can evaluate opportunities, negotiate compensation, and manage their earnings. An administrator oversees the ecosystem to ensure trust, moderation, and platform integrity.

The system formalizes influencer marketing workflows that are otherwise fragmented and informal, converting them into auditable, secure, and well‑defined digital processes.

---

## Problem It Solves

Influencer marketing today is largely managed through informal channels such as emails or direct messages, which leads to:

* Lack of transparency in negotiations and payments
* No standardized workflow for campaign assignment
* Difficulty in tracking campaign progress and outcomes
* Absence of platform‑level governance and moderation

IESCP addresses these issues by providing a centralized platform where campaigns, negotiations, and collaborations are managed through controlled workflows with clear role boundaries and backend‑enforced rules.

---

## Target Users (Personas)

### 1. Sponsor (Brand / Advertiser)

* Wants to promote products or services through influencers
* Needs visibility into influencer profiles and reach
* Requires controlled budget management and campaign tracking

### 2. Influencer (Content Creator)

* Wants access to brand collaboration opportunities
* Needs transparency in campaign requirements and payment
* Seeks autonomy to accept, reject, or negotiate offers

### 3. Admin (Platform Operator)

* Responsible for maintaining platform integrity
* Needs tools for moderation, monitoring, and governance
* Manages industry classifications and flags inappropriate activity

---

## Vision Statement

To create a transparent, secure, and governed digital marketplace that streamlines influencer–brand collaborations through structured workflows, mutual negotiation, and platform‑level accountability.

---

## Key Features / Goals

* Role‑based access control for Admin, Sponsor, and Influencer
* Campaign creation and lifecycle management
* Influencer discovery and filtering by industry and reach
* Structured negotiation through ad requests
* Backend‑enforced acceptance and assignment logic
* Admin moderation with flagging and industry management
* Dashboard views with meaningful statistics for each role

---

## Success Metrics

* Successful creation and completion of campaigns
* Number of negotiated and accepted ad requests
* Reduction in ambiguous or failed collaborations
* Consistent role‑based access enforcement
* Stable system operation with correct state transitions

---

## Assumptions & Constraints

### Assumptions

* Users provide accurate profile and campaign information
* Negotiations occur exclusively through the platform
* Admin acts as a neutral platform authority

### Constraints

* PostgreSQL is used as the database for simplicity and local deployment
* Session‑based authentication is used instead of JWT
* The platform is designed as a monolithic web application
* Payments are tracked logically but not processed through an external payment gateway

---

## Technology Stack (Summary)

* **Frontend:** Vue.js (SPA)
* **Backend:** Flask (REST API)
* **Database:** PostgreSQL with SQLAlchemy ORM
* **Authentication:** Session‑based with role validation
* **Deployment (Local):** Docker‑based setup

---

## Branching Strategy and GitHub Flow

This project follows the **GitHub Flow** branching strategy to keep development simple, structured, and traceable.

### Main Branch
- The `main` branch always represents a **stable and deployable** version of the project.
- All documentation, architecture diagrams, and verified features are merged into `main`.

### Feature Branches
- New work is developed in **feature branches** created from `main`.
- Each feature branch focuses on a single task or improvement, such as:
  - documentation updates
  - UI changes
  - backend enhancements
  - DevOps setup

### Workflow
1. Create a new feature branch from `main`
2. Implement the required changes
3. Commit changes with clear messages
4. Merge the feature branch back into `main` after verification

This workflow ensures:
- Clean commit history
- Isolation of incomplete work
- Easier collaboration and review

---

## Development Workflow Summary

- Branching Model: **GitHub Flow**
- Default Branch: `main`
- Feature Branch Naming Convention: `feature/<short-description>`
- Merge Strategy: Fast-forward or squash merge for clarity

---

## Quick Start – Local Development

This section explains how to run **IESCP** locally using **Docker** and **Docker Compose**. The setup runs the frontend, backend, and database as isolated containers, closely simulating a real deployment environment.

---

### Prerequisites

Ensure the following tools are installed on your system:

- **Git** (for cloning the repository)
- **Docker Desktop** (includes Docker Engine and Docker Compose)

Verify installation:

```bash
docker --version
docker-compose --version
```

---

### Clone the Repository

```bash
git clone https://github.com/<your-username>/IESCP.git
cd IESCP
```

---

### Project Structure (Relevant to Docker)

```text
IESCP/
├── backend/              # Flask backend (Dockerized)
│   ├── app.py
│   ├── orm.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/             # Vue.js frontend (Dockerized)
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
├── docker-compose.yml    # Multi-container orchestration
└── README.md
```

---

### Build and Run the Application

From the **root of the repository**, run:

```bash
docker-compose build
docker-compose up
```

This command will:
- Build Docker images for the frontend and backend
- Start the PostgreSQL database container
- Start all services on a shared Docker network

---

### Access the Application

Once all containers are running:

- **Frontend (Vue.js SPA):** http://localhost:3000
- **Backend API (Flask):** http://localhost:5000
- **PostgreSQL Database:** localhost:5432

Logs for each service will be visible in the terminal.

---

### Stopping the Application

To stop all running containers:

```bash
docker-compose down
```

To stop containers and remove volumes:

```bash
docker-compose down -v
```

---

### Notes

- This setup is intended for **local development and demonstration purposes**.
- Docker ensures consistent behavior across different systems.
- Environment variables for database connectivity are managed via `docker-compose.yml`.

## Local Development Tools

This section documents the tools and environment used for developing **IESCP**. Listing these tools ensures the project can be reproduced consistently and demonstrates adherence to standard software engineering practices.

---

### Operating System

- **macOS Tahoe**

---

### Core Development Tools

- **Docker Desktop** – Used for containerizing and running the frontend, backend, and database services via Docker Compose
- **Git** – Used for version control and branch management following GitHub Flow

---

### Programming Languages & Runtimes

- **Node.js (LTS)** – Used for building and bundling the Vue.js frontend
- **Python 3.x** – Used for implementing the Flask backend API

---

### Frameworks & Technologies

- **Vue.js (with Vite)** – Frontend single-page application framework
- **Flask** – Backend REST API framework
- **SQLAlchemy** – ORM for database interactions
- **PostgreSQL** – Relational database used in the Dockerized environment

---

### Development Environment

- **Kiro IDE** – Primary code editor used for frontend, backend, and configuration development

---

These tools collectively support a clean, reproducible, and container-friendly development workflow for the IESCP project.