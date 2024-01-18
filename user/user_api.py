from fastapi import APIRouter
from user import LoginValidator, RegisterValidator
from database.userservice import login_user_db, add_new_user_db

# создадим компонент
user_router = APIRouter(prefix='/user', tags=['Управления пользователями'])


# Запрос на вход в аккаунт
@user_router.post('/login')
async def login_user(data: LoginValidator):
    result = login_user_db(**data.model_dump())

    return {'message': result}


# Запрос на регистрацию пользователя
@user_router.post('/register')
async def register_user(data: RegisterValidator):
    result = add_new_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Пользователь уже имеется'}

@user_router.get('/all-users')
async def all_users():
    pass