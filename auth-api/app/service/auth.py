from ..authentication import verify_password
from ..model import models
from requests import Session

from ..service.users import get_user


def authenticate_user(email: str, password: str, db: Session):
    user: models.User = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
