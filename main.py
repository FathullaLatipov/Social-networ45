from fastapi import FastAPI

from user.user_api import user_router
from posts.post_api import post_router

# для запуска БД
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(post_router)