# Todo List API

Простое API для управления списком задач.

## 🛠 Технологии
- FastAPI
- SQLAlchemy 2.0 (асинхронный)
- SQLite
- Pydantic

## 📋 Функционал
- ✅ Создание задачи
- ✅ Просмотр всех задач
- ✅ Просмотр одной задачи
- ✅ Отметка "выполнено"
- ✅ Удаление задачи

## 🚀 Установка и запуск

### 1. Клонировать репозиторий

    git clone https://github.com/Ashkelon1337/todo_list_API.git
    cd todo_list_API


### 2. Создать и активировать виртуальное окружение
    #Windows
    python -m venv venv
    venv\Scripts\activate

    #Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
### 3. Установить зависимости
    pip install -r requirements.txt
### 4. Запустить сервер
    python main.py
### 5. Открыть в браузере
    http://127.0.0.1:8000/docs

# Эндпоинты
### POST /tasks
    Создать задачу
### GET /tasks	
    Все задачи
### GET /tasks/{id}
	Задача по ID
### PUT /tasks/{id}	
    Отметить выполненной
### DELETE /tasks/{id}	
    Удалить задачу