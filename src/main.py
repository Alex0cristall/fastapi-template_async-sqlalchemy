import uvicorn

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager

from core.config import settings
from core.models import db_helper
from api import router as api_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # startapp
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan
)
app.include_router(
    api_router
)



if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )
