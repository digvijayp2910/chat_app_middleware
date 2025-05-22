from core.db import mongo_db


class MongoChat:
    collection = mongo_db.get_collection("chat_content")

    @staticmethod
    async def create_qa(chat_id: str, branch_id: str, question: str, answer: str):
        document = await MongoChat.collection.find_one({"chat_id": chat_id, "branch_id": branch_id})
        qa = {"question": question, "answer": answer}
        if document:
            await MongoChat.collection.update_one(
                {"_id": document["_id"]},
                {"$push": {"qa_pairs": qa}}
            )
        else:
            await MongoChat.collection.insert_one({
                "chat_id": chat_id,
                "branch_id": branch_id,
                "qa_pairs": [qa]
            })

    @staticmethod
    async def get_qa_pairs(chat_id: str, branch_id: str):
        doc = await MongoChat.collection.find_one({"chat_id": chat_id, "branch_id": branch_id})
        return doc["qa_pairs"] if doc else []

    @staticmethod
    async def create_branch(chat_id: str, from_branch_id: str, new_branch_id: str, fork_question: str, fork_answer: str):
        qa_pairs = await MongoChat.get_qa_pairs(chat_id, from_branch_id)
        new_doc = {
            "chat_id": chat_id,
            "branch_id": new_branch_id,
            "qa_pairs": qa_pairs + [{"question": fork_question, "answer": fork_answer}]
        }
        await MongoChat.collection.insert_one(new_doc)
