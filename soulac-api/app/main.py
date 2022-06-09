from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .route import soulacais, drinks, alcohols
from .service.auth import call_auth_api

app = FastAPI(
    title="Soulac Web API",
    version="0.0.1",
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(soulacais.soulacais_router, dependencies=[Depends(call_auth_api)])
app.include_router(drinks.drinks_router, dependencies=[Depends(call_auth_api)])
app.include_router(alcohols.alcohols_router, dependencies=[Depends(call_auth_api)])
