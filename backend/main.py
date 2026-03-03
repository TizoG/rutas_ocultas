"""Application entrypoint."""

from fastapi import FastAPI

from app.api import api_router

app = FastAPI(title="rutas_ocultas", version="1.0.0")
app.include_router(api_router, prefix="/api")


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}
