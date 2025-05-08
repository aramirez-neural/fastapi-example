import asyncpg
from app.core.config import settings

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
        )

    async def fetch(self, query: str):
        if self.pool is None:
            await self.connect()  # Conectar si no está conectado
        async with self.pool.acquire() as conn:
            return await conn.fetch(query)

    async def execute(self, query: str):
        if self.pool is None:
            await self.connect()  # Conectar si no está conectado
        async with self.pool.acquire() as conn:
            return await conn.execute(query)

# Instancia global
database = Database()
