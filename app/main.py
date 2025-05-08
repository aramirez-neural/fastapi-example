from fastapi import FastAPI
from app.db.database import database
from app.routers import todo

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Conectamos a la base de datos cuando la aplicación se inicie
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    # Cerramos la conexión cuando la aplicación se cierre
    await database.pool.close()

app.include_router(todo.router)
