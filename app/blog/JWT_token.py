from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from blog import schemas

SECRET_KEY = "7f0a6d10160e57bcfdf43d639bf9dab9c3d7967744c1374b85d5c26a18c7e09b7f0a6d10160e57bcfdf43d639bf9dab9c3d7967744c1374b85d5c26a18c7e09b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str,credentials_exception):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception