from dataclasses import dataclass
from datetime import date

# These classes simulates a database model


@dataclass
class Address:
    country: str
    city: str


@dataclass
class User:
    name: str
    age: str
    email: str
    birth_date: date
    profile_url: str
    tags: str
    address: Address
    id: int = 0
