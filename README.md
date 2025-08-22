# 🛡️ Clans API

A simple, secure, and scalable REST API. It was developed to keep records of Clans. Built on FastAPI + PostgreSQL + GCP (Cloud Run & Cloud SQL) infrastructure.

## 🚀 Features

- `GET/clans`: Lists all clans  
- `POST/clans`: Creates a new clan record  
- Swagger UI automatically integrated (`/docs`)  
- Publicly accessible via Cloud Run  
- Cloud SQL (PostgreSQL) database connection  
- Long data entries are blocked through middleware  
- Container build is done via GCP Artifact Registry  

## 🏗️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [PostgreSQL (Cloud SQL)](https://cloud.google.com/sql)  
- [Google Cloud Run](https://cloud.google.com/run)  
- [Docker](https://www.docker.com/)  
- [Uvicorn](https://www.uvicorn.org/)  

## ⚙️ Setup

### 1. Create the .env file

```
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<db_name>
```

### 2. Build and push the Docker image

```bash
docker build -t gcr.io/<PROJECT_ID>/clans-api .
docker push gcr.io/<PROJECT_ID>/clans-api
```

### 3. Deploy to Cloud Run

```bash
gcloud run deploy clans-api \
  --image gcr.io/<PROJECT_ID>/clans-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --update-env-vars DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<db_name>
```

## 🌐 API Documentation

Swagger UI:  
```
https://<YOUR_CLOUD_RUN_URL>/docs
```

## 🔐 Security & Limitations

- **Maximum length** are set for `type` ve `name` fields.  
- Very long bodies are rejected by middleware.  
- Auth, rate limiting, etc. can be easily integrated in the future. 

## 👨‍💻 Developer

**Talha Murat Çamlı**  
[LinkedIn](https://www.linkedin.com/in/talhamuratcamli)  
📍 Powered by FastAPI & GCP  
