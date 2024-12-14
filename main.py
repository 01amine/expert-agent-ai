from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import conversation_router, summary_router, learning_router, prompt_router
from fastapi import APIRouter
from typing import List

from app.controllers.conversation_controller import create_conversation_controller
from app.models.conversation.conversation import ConversationRequest
from app.models.interaction.interaction import InteractionResponse

from app.utils.response import interaction_as_response


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
)


@app.get("/", tags=["StartUp AI"])
async def storming_ai():
    return {"message": "StartUp AI is ready to help you start your amazing journey!"}


app.include_router(conversation_router.router, prefix="/conversation", tags=["Conversation"])

app.include_router(summary_router.router, prefix="/summary", tags=["Summary"])

app.include_router(learning_router.router, prefix="/learning", tags=["Learning"])

app.include_router(prompt_router.router, prefix="/prompt", tags=["prompt"])