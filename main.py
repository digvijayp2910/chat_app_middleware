# app/main.py
from fastapi import FastAPI

from api.v1 import chat, message, branch

app = FastAPI(title="Chat App")

app.include_router(chat.router, prefix="/api/v1/chats")
app.include_router(message.router, prefix="/api/v1/messages")
app.include_router(branch.router, prefix="/api/v1/branches")
