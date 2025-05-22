from fastapi import APIRouter, HTTPException

from schemas.mongo_chat import MongoChat

router = APIRouter()

@router.post("/add-message")
async def add_message(payload: AddMessageRequest):
    try:
        await MongoChat.create_qa(
            chat_id=payload.chat_id,
            branch_id=payload.branch_id,
            question=payload.question,
            answer=payload.answer
        )
        return {"success": True, "message": "Message added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get-chat", response_model=QAPairsResponse)
async def get_chat(chat_id: str, branch_id: str):
    try:
        qa_pairs = await MongoChat.get_qa_pairs(chat_id, branch_id)
        return QAPairsResponse(chat_id=chat_id, branch_id=branch_id, qa_pairs=qa_pairs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
