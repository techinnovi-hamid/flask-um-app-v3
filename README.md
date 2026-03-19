🚀 Flask User Management App

A simple and clean Flask + SQLite web application to manage users.

This project is intentionally built simple so beginners can:

Understand backend basics

Practice database integration

Use it as a playground for DevOps tools (Docker, Kubernetes, CI/CD, etc.)

📌 Features

Add new users

Delete users

SQLite database integration

Auto table creation

Clean and beginner-friendly UI

Ready for DevOps practice

🛠 Tech Stack

Python 3

Flask

SQLAlchemy

SQLite

Gunicorn (for production use later)

▶️ How To Run Locally

Follow these simple steps:

1️⃣ Clone the Repository

git clone <your-repo-url>

cd flask-sqlite-app

2️⃣ Create Virtual Environment

python3 -m venv venv

source venv/bin/activate


Windows:

venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Application

python app.py

5️⃣ Open in Browser

Go to:

http://localhost:5000

📁 What Happens Automatically?

app.db SQLite database file will be created

User table will be created automatically

You can start adding and deleting users

🧠 Why This Project Is Useful for DevOps Learners

This simple app is perfect for practicing:

🐳 Docker

Write a Dockerfile

Build image

Run container

Use Docker Compose

☸ Kubernetes

Create Deployment

Create Service

Use ConfigMaps & Secrets

🔁 CI/CD

GitHub Actions pipeline

Jenkins pipeline

Build → Test → Deploy automation

🔐 Security

Trivy image scanning

SonarQube code analysis

🏗 Infrastructure as Code

Provision EC2 using Terraform

Automate configuration using Ansible

📊 Monitoring

Add Prometheus metrics

Visualize with Grafana

🎯 Learning Goal

This project is designed to help beginners:

Move from Developer → DevOps mindset

Understand how applications run in production

Practice real-world DevOps tools step-by-step

🚀 Next Steps

After running locally, try:

Containerizing the app with Docker

Deploying it to Kubernetes

Building a CI/CD pipeline

If you're learning DevOps, this is your playground.

Clone it. Break it. Improve it. Deploy it.
