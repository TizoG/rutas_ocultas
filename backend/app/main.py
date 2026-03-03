from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router as api_router
from app.core.config import settings
from app.db.migrations import DatabaseMigrationError, ensure_database_migrated


@asynccontextmanager
async def lifespan(_: FastAPI):
    try:
        ensure_database_migrated()
    except DatabaseMigrationError as exc:
        raise RuntimeError(str(exc)) from exc
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api")


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {"message": "Rutas Ocultas API lista 🚀"}
