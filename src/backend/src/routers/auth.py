# ./src/routers/auth.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.schemas.auth import SignUpResponse, SignInRequest, SignInResponse, DeleteAccountRequest
from src.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/sign_up", response_model=SignUpResponse, status_code=status.HTTP_201_CREATED)
def sign_up(db: Session = Depends(get_db)):
    return AuthService(db).sign_up()


@router.post("/sign_in", response_model=SignInResponse)
def sign_in(body: SignInRequest, db: Session = Depends(get_db)):
    return AuthService(db).sign_in(body.account_code)


@router.delete("/delete_account", status_code=status.HTTP_204_NO_CONTENT)
def delete_account(body: DeleteAccountRequest, db: Session = Depends(get_db)):
    AuthService(db).delete_account(body.account_code)
