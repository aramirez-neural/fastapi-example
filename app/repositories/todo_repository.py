from app.db.database import database

async def get_all_todos():
    query = "SELECT * FROM todos"
    rows = await database.fetch(query)
    return rows
