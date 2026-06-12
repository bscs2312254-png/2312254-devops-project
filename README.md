# DevOps Final Project (2312254)

**Student ID:** 2312254
**Course:** DevOps Fundamentals (BSCS 6th Semester)

## Introduction

This project implements a Student Management REST API using FastAPI and PostgreSQL. The application is packaged with Docker containers and hosted on an AWS EC2 instance. GitHub Actions is configured to automate code validation, testing, and deployment processes.

## System Workflow

```text
GitHub Repository
        |
        | Code Push
        v
   GitHub Actions
      |      |
      |      ├── Execute flake8 checks
      |      └── Execute pytest tests
      |
      v
   AWS EC2 Instance
         |
         └── Docker Compose
                ├── FastAPI Service
                └── PostgreSQL Service
```

### Components

* **web** → FastAPI backend service running on port 8000
* **db** → PostgreSQL database configured with persistent volume storage

---

## Installation and Setup

### Prerequisites

Before running the project, ensure the following are installed:

* Python 3.12
* Docker
* Docker Compose

### Setup Instructions

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/2312254-devops-project.git
cd 2312254-devops-project
```

Create an environment file:

```bash
cp .env.example .env
```

Modify the `.env` file according to your environment settings.

Start all services:

```bash
docker compose up --build
```

Verify API functionality:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/students
```

---

## Available API Routes

### Application Health Status

```http
GET /health
```

Provides the current status of both the application and database.

### Add New Student

```http
POST /students
```

Stores a new student record in the database.

### Retrieve All Students

```http
GET /students
```

Displays all student entries.

### Retrieve Student by Registration Number

```http
GET /students/{reg_no}
```

Returns details of a specific student using the registration number.

---

## AWS EC2 Deployment Guide

Connect to your EC2 server:

```bash
ssh -i your-key.pem ubuntu@YOUR_EC2_IP
```

Install Docker packages:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin
sudo usermod -aG docker ubuntu
```

Download the project:

```bash
git clone https://github.com/YOUR_USERNAME/2312254-devops-project.git
cd 2312254-devops-project
```

Generate the environment file:

```bash
cp .env.example .env
```

Launch the production environment:

```bash
docker compose -f docker-compose.prod.yml up -d --build
```

---

## Required GitHub Secrets

For automated deployment, configure the following repository secrets:

* `EC2_HOST` — Public IP address of the EC2 server
* `EC2_SSH_KEY` — Private SSH key content used for EC2 access

---

## Executing Tests

Install project dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
pytest app/tests/ -v
```

---

## Application URL

```text
http://YOUR_EC2_IP:8000
```

---

## Project Submission Details

**Student ID:** 2312254
**Course:** DevOps Fundamentals
**Semester:** BSCS 6th Semester
