# 🎓 Student Internship & Job Tracking System

A complete, containerized full-stack web application designed for university departments to track, manage, and analyze student placement opportunities, internships, and corporate recruitment pipelines.

## 👥 Team Members & Contributions
* **Ali Akbar:** DevOps & Database Architect (Docker, PostgreSQL Schema, SQLAlchemy Connection)
* **Ahmad Munir Sheikh:** Core Application Developer (Database Seeding, CRUD Operations)
* **Ali Sufyyan:** Advanced Features Engineer (Analytics Dashboard, CSV Handling, Duplicate Detection, Alerts)

---

## 🏗️ System Architecture
This project is built for absolute reproducibility using an isolated multi-container Docker architecture:
* **Frontend:** Python 3.10 / Streamlit (Port `8501`)
* **Database:** PostgreSQL 15 (Port `5432`) - *Pinned to v15 for stable volume mounting.*
* **Database GUI:** pgAdmin 4 (Port `5050`)
* **Infrastructure:** Docker Compose with a persistent external volume (`postgres_data`).

---

## 🚀 Setup & Installation Instructions

**1. Prerequisites**
* [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running in the background.
* Git installed on your local machine.

**2. Clone the Repository**
```bash
git clone <your-repository-url>
cd <your-repository-folder>