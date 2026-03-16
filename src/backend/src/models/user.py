# ./src/models/user.py
from dataclasses import dataclass


@dataclass
class User:
    id: int
    account_code_hash: str
