# 🏦 Loan Approval Prediction App

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/ee349b93-2bcb-42a6-89bb-6ac09f390917" />

A Machine Learning application that predicts loan approval using a trained machine learning model. It utilizes a Flask API for model inference and HEROKU app for quick and simple deployment.

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
3. Deploys to a target environment (Heroku)

**To enable CI/CD:**
1. Push code to GitHub
2. GitHub Actions will run .github/workflows/ci.yml automatically

---

## Local Development

Ensure you have installed Docker and HEROKU CLI

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

4. **Set up environment variable using dotenv**

Create `.env` file, then fill in the necessary keys

```bash
DOCKER_HUB_USERNAME=your_docker_hub_username
HEROKU_API_KEY=your_heroku_api_key
HEROKU_APP_NAME=your_heroku_app_name
HEROKU_EMAIL=your_heroku_email
```

### Run without Docker

```bash
python app.py
```

### Run with Docker (recommended)

```bash
docker-compose up --build
```

This will start both the app in container. Access the UI at: http://localhost:8000
