from pydantic import BaseModel

class SignUpResponse(BaseModel):
    account_code: str
    message: str

class SignInRequest(BaseModel):
    account_code: str

class SignInResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class DeleteAccountRequest(BaseModel):
    account_code: str
