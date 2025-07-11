# 🏦 Loan Approval Prediction App

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/25d93efa-64a0-4290-ad39-bd930d9541b8" />

A ML application that predicts loan approval using a trained machine learning model. It utilizes a Flask API for model inference and Google Cloud Platform (Artifacts Registry, Cloud Run) for production deployment.

---

## Problem Statement

The goal is to predict whether a loan request will be **accepted** or **rejected** based on applicant information such as income, age, credit score, etc.

This project simulates a real-world deployment pipeline by combining:
- A trained machine learning model (`model.pkl`)
- REST API for prediction (Flask)
- Frontend interface (HTML, CSS, Javascript)
- Containerized deployment (Docker)
- CI/CD pipeline (GitHub Actions)

---

## Dataset

The model was trained on a structured dataset containing [loan applicant information](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data/data).  

**Note**: The model is already trained and saved as `model/model.pkl`.

---

## Tech Stack

- **Python**
- **Scikit-learn** – Model training
- **Flask** – REST API
- **HTML, CSS, Javascript** – Frontend UI
- **Docker** – Containerization
- **GitHub Actions** – CI/CD pipeline

---

## Features
- Predict loan approvals instantly
- Shows model confidence level
- Low-latency predictions
- Fully containerized
- Ready for deployment

---

## CI/CD – GitHub Actions
**The project includes a GitHub Actions workflow that:**
1. Lints Python code
2. Builds Docker image
3. Deploys to a target environment (Cloud Run)

**To enable CI/CD:**
1. Push code to GitHub
2. GitHub Actions will run .github/workflows/ci.yml automatically

---

## Local Development

Ensure you have installed Docker & Google Cloud CLI 

1. **Clone the Repository**
```bash
git clone https://github.com/roissyahf/loan-approval-deploy.git
cd loan-approval-deploy
```
2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependency**
```bash
pip install -r requirements.txt
```

### Run without Docker

```bash
python app.py
```

### Run with Docker (recommended)

```bash
docker-compose up --build
```

This will start both the app in container. Access the UI at: http://127.0.0.1:8080
