from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import logging

logger = logging.getLogger(__name__)  # __name__ = "routers.users"

# Создаем роутер для пользователей
router = APIRouter(prefix="/users", tags=["Пользователи"])

class User(BaseModel):
    name: str = Field(..., json_schema_extra={"example": "Иван Петров"})
    age: int = Field(..., json_schema_extra={"example": 30})
    email: str = Field(..., json_schema_extra={"example": "ivan@example.com"})

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    email: Optional[str] = None

# Все маршруты теперь будут с префиксом /users
@router.get("/")
def get_users():
    return {"message": "Все пользователи"}

@router.get(
        "/{user_id}",
        response_model=User,
        responses={404: {"description": "Пользователь не найден"}},
        summary="Получение информации о пользователе",
        description="Возвращает данные пользователя и его ID")
def get_user(user_id: int):
    logger.info(f"Запрошен пользователь ID: {user_id}")
    if user_id != 1:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return {"user_id": user_id}

@router.post("/")
def create_user(user: User):
    logger.info(f"Создан новый пользователь: {user.name}")
    logger.debug(f"Детали: {user.model_dump()}")  # Более подробно
    return {"message": f"Пользователь {user.name} создан", "data": user}

@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_id": user_id, "updated_data": user}

@router.patch("/{user_id}")
def update_partial_user(user_id: int, user: UpdateUser):
    return {"user_id": user_id, "updated_fields": user.dict(exclude_none=True)}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    logger.warning(f"Пользователь {user_id} удаляется!")
    return {"message": f"Пользователь с ID {user_id} удалён"}