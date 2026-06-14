# 🎓 Student Internship & Job Tracking System

A complete, containerized full-stack web application designed for university departments to track, manage, and analyze student placement opportunities, internships, and corporate recruitment pipelines.

## 👥 Team Members & Contributions
* **Ali Akbar:** DevOps & Database Architect (Docker, PostgreSQL Schema, SQLAlchemy Connection)
* **Ahmad Munir Sheikh:** Core Application Developer (Database Seeding, CRUD Operations)
* **Ali Sufyyan:** Advanced Features Engineer (Analytics Dashboard, CSV Handling, Duplicate Detection, Alerts)

---

## 🐳 1. Docker Compose Explanation
This application relies on Docker Compose to orchestrate a multi-container environment, ensuring total reproducibility. Our `docker-compose.yml` utilizes the following core concepts:
* **services:** We define three distinct microservices (`postgres_db`, `pgadmin`, and `streamlit_app`).
* **image / build:** `postgres` and `pgadmin` pull official pre-built images from Docker Hub, while `streamlit_app` builds a custom image from our local `Dockerfile`.
* **ports:** Maps internal container traffic to the host machine (e.g., `"8501:8501"` allows us to view Streamlit on our local browser).
* **environment:** Injects secure configuration variables (like `POSTGRES_USER` and `DB_PASSWORD`) directly into the containers at runtime.
* **depends_on:** Ensures the Streamlit app and pgAdmin GUI wait for the PostgreSQL database engine to initialize before booting.
* **volumes:** Persists data across container restarts (detailed below).

---

## 🗄️ 2. Database Design & Persistence
The backend is powered by **PostgreSQL 15**. 
* **Schema:** The database (`student_opportunities_db`) contains a primary table named `opportunities`, which tracks corporate data, required skills, salary metrics, and deadlines.
* **Data Persistence:** We utilize a named Docker Volume (`postgres_data`) mapped to `/var/lib/postgresql/data`. This guarantees that if the containers are destroyed or updated, the underlying job records remain completely intact. 
* **Initialization:** Upon the very first boot, Docker automatically executes `init.sql` to build the schema and `seed_data.sql` to populate 45 initial records.

---

## 🚀 3. App Setup & Installation

**Prerequisites:**
* [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.
* Git installed.

**Step 1: Clone the Repository**
```bash
git clone <your-repository-url>
cd <your-repository-folder>