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

This document defines the vision and scope of IESCP and serves as the foundation for further planning, prioritization, and architectural decisions.