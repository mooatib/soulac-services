import os
from fastapi import FastAPI
from .route.auth import auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Auth Service",
    version="0.0.1",
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
)

origins = [os.environ.get("SOULAC_API_URL")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
