# 🧠 FastAPI Chat App with Branching Conversations

A simple but extensible FastAPI-based backend chat system using PostgreSQL for metadata and MongoDB for storing messages with branching logic.

---

## 📦 Features
- REST APIs to create chats and conversation branches
- Add Q&A messages per branch
- View full conversation for a specific branch
- MongoDB used to store dynamic chat content
- PostgreSQL used to store metadata (chats & branches)
- Secure routes with token-based auth

---

## 🚀 Tech Stack
- FastAPI
- PostgreSQL (via SQLAlchemy + Alembic)
- MongoDB (via Motor)
- Pydantic for validation
- JWT-style token authentication (custom)

---

## ⚙️ How to Run

### 1. Clone the project and create virtual env
```bash
git clone <repo-url>
cd chat_app
python -m venv venv
source venv/bin/activate  # venv\Scripts\activate on Windows
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables in `.env`
```env
POSTGRES_URL=postgresql+asyncpg://postgres:password@localhost:5432/chatdb
MONGO_URL=mongodb://localhost:27017
MONGO_DB=chat_content_db
```

### 4. Run Alembic migrations
```bash
alembic upgrade head
```

### 5. Start the server
```bash
uvicorn app.main:app --reload
```

---

## 🔐 Authentication
All protected routes require an `Authorization` header:
```
Authorization: Bearer supersecrettoken
```

---

## 📮 API Endpoints

### Chats
- `POST /api/v1/chats/create-chat` → Create a new chat
- `POST /api/v1/chats/create-conversation` → Create a branch record

### Messages
- `POST /api/v1/messages/add-message` → Add a Q&A message
- `GET /api/v1/messages/get-chat` → Get chat messages for a branch

### Branches
- `POST /api/v1/branches/create-branch` → Create a new conversation branch

---

## 🧪 Sample Test
Use Postman or cURL:
```json
POST /api/v1/chats/create-chat
{
  "title": "My first chat"
}
```

---

## 📁 Project Structure
```
app/
├── api/v1/              # API routes
├── auth/                # Auth validation
├── core/                # DB configs
├── models/              # SQL + Mongo models
├── schemas/             # Pydantic schemas
├── services/            # Business logic (optional)
└── main.py              # FastAPI app entry
```

---

## 🧰 Requirements
- Python 3.9+
- PostgreSQL
- MongoDB

---

## 📬 Contact
**Author:** Digvijaysing Patil  
**Email:** digvijayp2910@gmail.com
