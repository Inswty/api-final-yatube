Yatube API
Позволяет создавать посты, комментировать их, подписываться на авторов и получать JWT-токены для аутентификации.

Возможности

Посты:

Создание, редактирование, удаление
Просмотр всех постов или конкретного


Поиск по группам:

Комментарии
Посты
Подписки

Подписки:

Подписка/отписка на авторов
Просмотр своих подписок


Аутентификация:

Получение JWT-токена
Обновление токена
JWT-аутентификация

Технологический стек:
Python 3.12.7
Django 5.1.1
Django REST Framework 5.4.0
Simple JWT (JWT-аутентификация)
SQLite
Swagger/ReDoc (документация API)

Как запустить?
Клонировать репозиторий:

bash
```
git clone https://github.com/ваш-username/api-final-yatube.git
```
```
cd api-final-yatube
```
Установить зависимости:
```
pip install -r requirements.txt
```
Применить миграции:
```
python manage.py migrate
```
Запустить сервер:
```
python manage.py runserver
```
Документация API
Доступна по адресу:
```
http://localhost:8000/redoc/ (ReDoc)
```
Примеры запросов
Получение токена:
bash
```
POST http://localhost:8000/api/v1/jwt/create/
'{"username":"ваш_username", "password":"ваш_пароль"}'
```
Создание поста:
```
POST http://localhost:8000/api/v1/posts/
'{"text":"Текст поста", "group":1}'
```
Тестирование
Запуск тестов:
```
pytest -v
```
Автор
Проект разработан [Павел Куличенко]
GitHub: https://github.com/Inswty