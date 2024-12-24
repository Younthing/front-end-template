from fastapi import FastAPI
from src.app.api.v1.endpoints import users, items
from src.app.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description=settings.description,
        version=settings.version,
    )

    # Include routers
    app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
    app.include_router(items.router, prefix="/api/v1/items", tags=["items"])

    @app.get("/")
    async def root():
        return {"message": f"Welcome to {settings.app_name}"}

    @app.get("/api/hello")
    async def hello():
        return {"message": "Hello World"}
    return app

app = create_app()

