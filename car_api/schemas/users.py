from typing import Optional, List
from pydantic import BaseModel, EmailStr

#esquema para criar um usuário (cadatrar usuário: post)
class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

#Estrutura da resposta da Api para o usuários (Get) ->representa: router/users.py
class UserPublicSchema(BaseModel):
   id: int
   username: str
   email: EmailStr


class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

#Schema da classe list_users do arquivo router/users.py ->representa: router/users.py
class UserlistPublicSchema(BaseModel):
    users: List[UserPublicSchema]