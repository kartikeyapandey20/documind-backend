# Documind Backend

A powerful backend service for managing and processing documents using Python FastAPI

## 🌟 Features

- Document processing and analysis
- FastAPI-based REST API endpoints
- Secure file storage and management
- PDF and text document support

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Document Storage:** AWS S3
- **Authentication:** JWT
- **Documentation:** Swagger

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL
- AWS S3 Account

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/kartikeyapandey20/documind-backend.git
cd documind-backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
alembic upgrade head
```

## 🔧 Configuration

Create a `.env` file with the following variables:

```env
DATABASE_URL=postgresql://user:password@localhost/documind
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_BUCKET_NAME=your_bucket_name
JWT_SECRET_KEY=your_jwt_secret
```

## 🏃‍♂️ Running the Application

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation:
```
http://localhost:8000/docs
```

## 📚 API Documentation

### Authentication Endpoints
- `POST /auth/register`: Register new user
- `POST /auth/login`: User login

### Document Endpoints
- `POST /documents/upload`: Upload new document
- `GET /documents/{doc_id}`: Get document details


## 🔒 Security

- JWT-based authentication
- Rate limiting
- Input validation
- Secure file handling
- Environment variable protection

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👥 Authors

- Kartikeya Pandey - [GitHub](https://github.com/kartikeyapandey20)

## 🙏 Acknowledgments

- FastAPI team for the amazing framework

## ⚠️ Troubleshooting

Common issues and their solutions:

1. **Database Connection Issues**
   - Verify PostgreSQL is running
   - Check database credentials in .env
   - Ensure database exists

2. **File Upload Issues**
   - Check AWS credentials
   - Verify S3 bucket permissions
   - Ensure proper file size limits
