from __future__ import annotations
from typing import List
import uuid
from data.models import User
from schemas import Address

USERS = [
    User(
        id=1,
        name="Ivan Bicalho",
        age=22,
        email="ivan.bicalho@carta.com",
        birth_date="1990-01-25",
        profile_url="https://carta.com",
        tags="engineer dev python",
        address=Address(country="Brasil", city="Belo Horizonte"),
    ),
    User(
        id=2,
        name="John Silva",
        age=33,
        email="john@carta.com",
        birth_date="1980-10-21",
        profile_url="https://carta.com",
        tags="engineer python",
        address=Address(country="USA", city="New York"),
    ),
    User(
        id=3,
        name="Emma Jones",
        age=44,
        email="emma@carta.com",
        birth_date="1970-09-30",
        profile_url="https://carta.com",
        tags="python",
        address=Address(country="USA", city="Chicago"),
    ),
]


class UserRepository:
    @classmethod
    def factory(cls) -> UserRepository:
        return cls()

    def get(self, id: uuid.UUID) -> User:
        try: 
            return next(filter(lambda u: u.id == id, USERS))
        except StopIteration:
            return None

    def list(self) -> List[User]:
        return USERS

    def add(self, user: User) -> User:
        user.id = 1
        return user

    def update(self, user: User) -> User:
        return user
