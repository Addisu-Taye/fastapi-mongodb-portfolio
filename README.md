# FastAPI + MongoDB Portfolio API with JWT Authentication

This is a simple backend API built with FastAPI and MongoDB, featuring JWT-based user registration and login. It provides secure CRUD operations on items, designed for integration with React Native or any frontend.

---

## 🚀 Features

- ✅ User registration and login with JWT authentication  
- ✅ Password hashing with bcrypt  
- ✅ MongoDB with async access using Motor  
- ✅ Protected CRUD endpoints for item management  
- ✅ Swagger/OpenAPI interactive docs  

---

## 🛠️ Technologies Used

- Python 3.8+
- FastAPI
- MongoDB
- Motor
- Uvicorn
- Pydantic
- Passlib (bcrypt)
- Python-Jose (JWT)
- Python-Dotenv
- Email-validator

---

## 📁 Project Structure

```
fastapi-mongodb-portfolio/
├── main.py             # Main FastAPI app
├── .env                # Environment variables (not committed)
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── venv/               # Python virtual environment (excluded)
```

---

## 📦 Requirements

Here are the main dependencies used in the project:

```
fastapi
uvicorn
motor
pydantic
passlib[bcrypt]
python-jose[cryptography]
python-dotenv
email-validator
```

Install all at once:

```bash
pip install -r requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-mongodb-portfolio.git
cd fastapi-mongodb-portfolio
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Create `.env` File

```env
MONGO_URI=mongodb://localhost:27017
SECRET_KEY=your-very-secret-key
```

Replace `SECRET_KEY` with a secure random value.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the App

```bash
uvicorn main:app --reload
```

Swagger docs:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔐 API Authentication Flow

1. **POST /register** – Register a new user  
2. **POST /token** – Log in to get a JWT access token  
3. **Authorize in Swagger UI** with `Bearer <token>`  
4. Use `/items` endpoints securely  

---

## 🧪 Example Auth Request

**POST** `/register`

```json
{
  "email": "user@example.com",
  "password": "yourpassword",
  "full_name": "Addisu Taye"
}
```

**POST** `/token`  
Form data:
- username: user@example.com
- password: yourpassword

---

## 📌 License

MIT License – free to use and modify.

---
