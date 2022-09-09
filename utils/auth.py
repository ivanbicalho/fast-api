from jose.exceptions import JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from utils.exceptions import UnauthorizedException
import jose.jwt as jwt

# This is just an example of login using JWT with HS256 (symmetric key)

SECRET_KEY = "59fc2476d6f44cccadb246d0ddb2489e"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def generate_access_token(username: str) -> str:
    data = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES),
    }
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def get_logged_username(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise UnauthorizedException
        return username
    except JWTError:
        raise UnauthorizedException
