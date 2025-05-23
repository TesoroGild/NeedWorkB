from fastapi import FastAPI
from routers import users_Route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(users_Route.router)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)