# ./src/repositories/user_repository.py
from sqlalchemy.orm import Session
from src.db.tables import UserTable


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, account_code_hash: str) -> UserTable:
        user = UserTable(account_code_hash=account_code_hash)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all(self) -> list[UserTable]:
        return self.db.query(UserTable).all()

    def get_by_id(self, user_id: int) -> UserTable | None:
        return self.db.query(UserTable).filter(UserTable.id == user_id).first()

    def delete(self, user: UserTable) -> None:
        self.db.delete(user)
        self.db.commit()
