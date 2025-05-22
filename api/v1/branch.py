# app/api/v1/branch.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4
from app.core.db import get_db
from app.models.chat import Conversation
from app.models.mongo_chat import MongoChat

router = APIRouter()

@router.post("/create-branch")
async def create_branch(payload: CreateBranchRequest, db: AsyncSession = Depends(get_db)):
    try:
        # 1. Add branch record to PostgreSQL
        new_branch = Conversation(
            id=uuid4(),
            chat_id=payload.chat_id,
            branch_id=payload.new_branch_id,
            parent_id=payload.from_branch_id
        )
        db.add(new_branch)
        await db.commit()

        # 2. Duplicate QA from Mongo + append the new message
        await MongoChat.create_branch(
            chat_id=payload.chat_id,
            from_branch_id=payload.from_branch_id,
            new_branch_id=payload.new_branch_id,
            fork_question=payload.fork_question,
            fork_answer=payload.fork_answer
        )

        return {"success": True, "message": "Branch created"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
