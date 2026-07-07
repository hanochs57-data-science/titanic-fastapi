# Titanic Survival Prediction using Decision Tree, FastAPI & Docker

A full-stack Machine Learning web application that predicts whether a passenger would survive the Titanic disaster using a **Decision Tree Classifier**. The project is built with **FastAPI**, **Jinja2**, **HTML/CSS**, containerized using **Docker**, and is deployment-ready on **Render**.

---

# Project Overview

This project demonstrates the complete deployment lifecycle of a Machine Learning model, from training to cloud deployment.

The application allows users to enter passenger details and predicts whether the passenger would have survived the Titanic disaster.

---

# Features

- Decision Tree Classification
- FastAPI Backend
- Responsive User Interface
- Jinja2 Template Rendering
- Model Serialization using Joblib
- Docker Containerization
- Render Deployment Ready
- Prediction Probability using `predict_proba()`
- Clean Project Structure

---

# Tech Stack

## Machine Learning

- Python
- Scikit-learn
- Decision Tree Classifier
- Joblib

## Backend

- FastAPI
- Jinja2
- Uvicorn

## Frontend

- HTML5
- CSS3

## Deployment

- Docker
- Git
- GitHub
- Render

---

# Project Structure

```text
titanic-survival/

│
├── app.py
├── model.pkl
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│      index.html
│
└── static/
       style.css
```

---

# Application Workflow

```text
Passenger Details
        │
        ▼
HTML Form
        │
        ▼
FastAPI Backend
        │
        ▼
Load Trained Model
        │
        ▼
Decision Tree Prediction
        │
        ▼
Prediction & Probability
        │
        ▼
Display Result
```

---

# Input Features

The application accepts the following passenger information:

| Feature | Description |
|----------|-------------|
| Passenger Class | Ticket Class |
| Gender | Male / Female |
| Age | Passenger Age |
| Fare | Ticket Fare |
| Siblings/Spouses | Number of SibSp |
| Parents/Children | Number of Parch |

---

# Output

The application predicts:

- Survived
- Did Not Survive

It also displays the model's confidence using prediction probabilities.

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/titanic-survival.git

cd titanic-survival
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

# Docker

## Build the Docker Image

```bash
docker build -t titanic-survival .
```

## Run the Docker Container

```bash
docker run -p 8000:8000 titanic-survival
```

Open:

```
http://localhost:8000
```

---

# Deployment on Render

1. Push the project to GitHub.
2. Sign in to Render.
3. Create a new Web Service.
4. Connect the GitHub repository.
5. Select Docker as the deployment method.
6. Deploy the application.

Render automatically builds and deploys the application using the Dockerfile.

---

# API Endpoints

## Home

```
GET /
```

Displays the prediction interface.

---

## Predict

```
POST /predict
```

Processes passenger information and returns the prediction along with the confidence score.

---

# Machine Learning Pipeline

```text
Titanic Dataset
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Decision Tree Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Serialization (model.pkl)
        │
        ▼
FastAPI Application
        │
        ▼
Docker Container
        │
        ▼
Render Deployment
```

---

# Skills Demonstrated

- Machine Learning Model Deployment
- Decision Tree Classification
- FastAPI Development
- HTML Form Handling
- Jinja2 Template Rendering
- Docker Containerization
- REST API Development
- Git & GitHub Version Control
- Cloud Deployment using Render
- Production-ready Project Structure

---

# Future Enhancements

- User Authentication
- Prediction History
- PostgreSQL Integration
- React Frontend
- Feature Importance Visualization
- SHAP Explainability
- Dark and Light Themes
- CI/CD using GitHub Actions
- Kubernetes Deployment
- AWS Deployment

---

# Screenshots

Include screenshots of:

- Home Page
- Prediction Result
- Docker Container Running
- Render Deployment

---

# License

This project is intended for educational purposes and portfolio demonstration.

---

# Author

**Hanoch Shetty**

B.Sc. Information Technology Student

Interested in Artificial Intelligence, Machine Learning, Data Science, Full-Stack Development, and Cloud Technologies.
