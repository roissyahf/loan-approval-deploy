# 🏦 Loan Approval Prediction App

A ML application that predicts loan approval using a trained machine learning model. It utilizes a Flask API for model inference and a Streamlit UI for user interaction, using HEROKU app for quick and simple deployment.

---

## Problem Statement

The goal is to predict whether a loan request will be **accepted** or **rejected** based on applicant information such as income, age, credit score, etc.

This project simulates a real-world deployment pipeline by combining:
- A trained machine learning model (`model.pkl`)
- REST API for prediction (Flask)
- Frontend interface (Streamlit)
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
- **Streamlit** – Frontend UI
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

In two separate terminals:

**Terminal 1: Run Flask API**

```bash
python api\server.py
```

**Terminal 2: Run Streamlit UI**

```bash
python ui\app.py
```

### Run with Docker (recommended)

```bash
docker-compose up --build
```

This will start both the Flask API and Streamlit app in containers. Access the UI at: http://localhost:8501
