from fastapi import FastAPI

from app.api.routes import router as api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(api_router, prefix="/api")


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {"message": "Rutas Ocultas API lista 🚀"}
