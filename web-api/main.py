from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from route.users import users_router

app = FastAPI(
    title="Soulac Web API",
    version="0.0.1"
)

origins = ["*"]  
app.add_middleware(     CORSMiddleware,     allow_origins=origins,     allow_credentials=True,     allow_methods=["*"],     allow_headers=["*"], )

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    if request.client.host in ["127.0.0.1"] :
        response = await call_next(request)
        return response
    else:
        return None

app.include_router(users_router)