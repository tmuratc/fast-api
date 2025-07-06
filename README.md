# 🛡️ Clans API

Basit, güvenli ve ölçeklenebilir bir REST API. Clans (klanlar) kaydını tutmak için geliştirilmiştir. FastAPI + PostgreSQL + GCP (Cloud Run & Cloud SQL) altyapısı üzerine kuruludur.

## 🚀 Özellikler

- `GET/clans`: Tüm klanları listeler  
- `POST/clans`: Yeni bir klan kaydı oluşturur  
- Swagger UI otomatik olarak entegre (`/docs`)  
- Cloud Run üzerinden **public erişime açık**  
- Cloud SQL (PostgreSQL) veritabanı bağlantısı  
- Middleware üzerinden uzun veri girişleri engellenmiştir  
- GCP Artifact Registry üzerinden container build yapılmıştır  

## 🏗️ Kullanılan Teknolojiler

- [FastAPI](https://fastapi.tiangolo.com/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [PostgreSQL (Cloud SQL)](https://cloud.google.com/sql)  
- [Google Cloud Run](https://cloud.google.com/run)  
- [Docker](https://www.docker.com/)  
- [Uvicorn](https://www.uvicorn.org/)  

## ⚙️ Kurulum

### 1. .env dosyasını oluştur

```
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<db_name>
```

### 2. Docker image oluştur ve push et

```bash
docker build -t gcr.io/<PROJECT_ID>/clans-api .
docker push gcr.io/<PROJECT_ID>/clans-api
```

### 3. Cloud Run’a deploy et

```bash
gcloud run deploy clans-api \
  --image gcr.io/<PROJECT_ID>/clans-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --update-env-vars DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<db_name>
```

## 🌐 API Dokümantasyonu

Swagger UI:  
```
https://<YOUR_CLOUD_RUN_URL>/docs
```

## 🔐 Güvenlik & Limitler

- `type` ve `name` alanlarına **maksimum uzunluk** sınırı kondu.  
- Middleware ile çok uzun body’ler reddediliyor.  
- İleride auth, rate limit vb. kolayca entegre edilebilir.  

## 👨‍💻 Geliştirici

**Talha Murat Çamlı**  
[LinkedIn](https://www.linkedin.com/in/tmuratc)  
📍 Powered by FastAPI & GCP  