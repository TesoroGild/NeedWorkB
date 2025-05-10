from fastapi import FastAPI
from routers import usersRoute

app = FastAPI()

app.include_router(usersRoute.router)
