import uvicorn
from fastapi import FastAPI

from app.api import router as api_router
from app.core.config import settings


app = FastAPI()
app.include_router(
        api_router,
        prefix=settings.api.prefix
)


if __name__ == '__main__':
    uvicorn.run(
            "main:app",
            host=settings.run.host,
            port=settings.run.port,
            reload=True,
    )
