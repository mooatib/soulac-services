import os
from datetime import timedelta
from http.client import HTTPException

from ..authentication import create_access_token, get_token_data, hash_password
from ..database import get_db
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..model import token_schemas, user_schemas
from ..service.auth import authenticate_user
from ..service.users import create_user, get_user
from sqlalchemy.orm import Session

auth_router = APIRouter(tags=["auth"])

@auth_router.post("/signup", response_model=user_schemas.UserEncrypted, status_code=201)
def auth_signup(userSchema: user_schemas.UserEncrypted, db: Session = Depends(get_db)):
    userSchema.password = hash_password(userSchema.password)
    user = create_user(db, userSchema)
    return user


@auth_router.post("/token", response_model=token_schemas.Token)
async def auth_login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    access_token = create_access_token(
        data={"username": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get("/users/me/", response_model=user_schemas.User)
async def read_users_me(
    db: Session = Depends(get_db),
    token_data: user_schemas.User = Depends(get_token_data),
):
    current_user = get_user(db, email=token_data.username)
    return current_user
