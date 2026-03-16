# ./src/services/auth_service.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.core.security import (
    generate_account_code,
    hash_account_code,
    verify_account_code,
    create_access_token,
)
from src.repositories.user_repository import UserRepository
from src.schemas.auth import SignUpResponse, SignInResponse


class AuthService:

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def sign_up(self) -> SignUpResponse:
        account_code = generate_account_code()
        hashed = hash_account_code(account_code)
        self.repo.create(account_code_hash=hashed)
        return SignUpResponse(
            account_code=account_code,
            message="Guarda este código. Es la única forma de acceder a tu cuenta.",
        )

    def sign_in(self, account_code: str) -> SignInResponse:
        all_users = self.repo.get_all()
        matched = next(
            (u for u in all_users if verify_account_code(account_code, u.account_code_hash)),
            None,
        )
        if not matched:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Código de cuenta inválido",
            )
        return SignInResponse(access_token=create_access_token(matched.id))

    def delete_account(self, account_code: str) -> None:
        all_users = self.repo.get_all()
        matched = next(
            (u for u in all_users if verify_account_code(account_code, u.account_code_hash)),
            None,
        )
        if not matched:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cuenta no encontrada",
            )
        self.repo.delete(matched)
