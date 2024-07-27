from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .routes.routes import router
from .database.dbconnection import connect_db, close_db

# decorator used for manage lifespan asynchronous
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global db
    db = await connect_db()
    # running
    yield
    # Shutdown
    await close_db()

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = create_app()