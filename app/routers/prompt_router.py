from fastapi import APIRouter

from app.models.prompt.prompt import Prompt

router = APIRouter()

@router.post("/", response_model = str)
async def reply_prompt(request : str) -> str:
        return request