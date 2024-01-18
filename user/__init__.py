from pydantic import BaseModel


# Валидатор для входа в аккаунт
class LoginValidator(BaseModel):
    phone_number: int
    password: str


# Валидатор для регистрации
class RegisterValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: int
    city: str
    password: str
