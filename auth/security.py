from fastapi import Depends, HTTPException, Header

# Dummy token validation
API_TOKEN = "supersecrettoken"

async def token_verification(authorization: str = Header(...)):
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Invalid or missing token.")
    return {"user_id": "test-user"}  # Simulated user context
