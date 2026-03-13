from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Для кроссплатформенной работы с другими доменами
from routers import users  # Импортируем роутер
# from fastapi_swagger_ui import SwaggerUI
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Мой API на FastAPI",
    description="Простое API для демонстрации возможностей FastAPI",
    version="1.0.0",
    contact={
        "name": "Разработчик",
        "email": "developer@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensourse.org/license/MIT",
    },
    openapi_url="/api/openapi.json",     # Изменённый путь к OpenAPI JSON
    docs_url="/api/docs",               # Изменённый путь к Swagger UI
    redoc_url=None                      # Отключение ReDoc
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # Разрешить все источники
    allow_credentials=True, 
    allow_methods=["*"],     # Разрешить методы POST, GET, DELETE
    allow_headers=["*"],     # Разрешить все заголовки

)

# Подключаем роутер
app.include_router(users.router)

@app.get("/")
def home():
    logger.info("Обработан запрос к корневому маршруту!")
    return {"message": "Добро пожаловать в FastAPI!"}