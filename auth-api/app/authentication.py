import os
from base64 import decode
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from .model import token_schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(plain_password: str):
    return pwd_context.encrypt(plain_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, os.environ.get("SECRET_KEY"), os.environ.get("ALGORITHM")
    )
    return encoded_jwt


def decodeAndVerifyToken(access_token: str):
    decoded_token = jwt.decode(
        access_token, os.environ.get("SECRET_KEY"), os.environ.get("ALGORITHM")
    )
    if datetime.utcfromtimestamp(decoded_token["exp"]) >= datetime.utcnow():
        return decoded_token
    else:
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")


async def get_token_data(access_token: str = Depends(oauth2_scheme)):
    try:
        payload = decodeAndVerifyToken(access_token)
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_data = token_schemas.TokenData(username=username)
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token_data
