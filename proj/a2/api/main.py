import uvicorn
from config import settings
from fastapi import FastAPI
from routers.router import api_router

from api.database import Base, engine


def create_app():
    app = FastAPI()
    app.include_router(api_router, prefix="/api/v1")
    Base.metadata.create_all(engine, checkfirst=True)

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        "api.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.app_debug,
    )
