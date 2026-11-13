from fastapi import APIRouter
from app.agents.intent_agent import detect
router=APIRouter()
@router.post("/chat")
def chat(data:dict): return detect(data.get("mensagem",""))