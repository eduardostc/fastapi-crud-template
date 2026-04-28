from fastapi import APIRouter, status
from car_api.db import USERS

from car_api.schemas.users import (
    UserSchema,
    UserlistPublicSchema,
    UserPublicSchema,
)

router = APIRouter()

@router.post(
        path='/',
        status_code=status.HTTP_201_CREATED,
        response_model=UserPublicSchema, #Esse endpoint vai retornar o userPublicSchema
)
async def create_user(user: UserSchema):
    user_with_id = UserPublicSchema(
        **user.model_dump(),
        id=len(USERS) + 1,
    )
    USERS.append(user_with_id)
    return user_with_id


@router.get(
        path='/',
        status_code=status.HTTP_200_OK,
        response_model=UserlistPublicSchema) #Esse endpoint vai retornar lista de usuário
async def list_users():
    return { 'users': USERS
        # 'users': [
        #     {
        #         'id': 1,
        #         'username': 'pycodebr',
        #         'email': 'pycodebr@gmail.com',
        #     },
        #     {
        #         'id': 2,
        #         'username': 'joão',
        #         'email': 'joao@gmail.com',
        #     },
        #     {
        #         'id': 3,
        #         'username': 'Mario',
        #         'email': 'mario@gmail.com',
        #     }
        # ]
    }

