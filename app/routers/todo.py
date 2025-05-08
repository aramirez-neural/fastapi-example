from fastapi import APIRouter
from app.repositories.todo_repository import get_all_todos

router = APIRouter()

@router.get("/todos")
async def get_todos():
    todos = await get_all_todos()
    return {"todos": todos}
