import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
path = "/bot/"
routers_name = "router"

DB_URL = f"postgresql+asyncpg://postgres:postgres@{DB_HOST}:{DB_PORT}/qrcoffee_db"
# DB_URL_SYNC = "postgresql://postgres:postgres@{DB_HOST}:{DB_PORT}/qrcoffee_db"