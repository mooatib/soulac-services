import os
from fastapi import Depends, HTTPException
import requests
from fastapi.security import HTTPBearer, HTTPBasicCredentials

auth_api_url = os.environ.get("AUTH_API_URL") + "/token"
security = HTTPBearer()


def call_auth_api(credentials: HTTPBasicCredentials = Depends(security)):
    headers = {"Authorization": "Bearer " + credentials.credentials}
    access_token = requests.get(auth_api_url, headers=headers)
    if access_token.status_code != 200:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
