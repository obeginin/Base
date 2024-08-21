import requests

# Json-запросы для добавления новых пользователей
url = "http://127.0.0.1:8001/api/register/"  # Замените на ваш URL

data_1 = {
    "login": "begininov",
    'last_name': 'Бегинин',
    "first_name": "Олег",
    "phone_number": "89264764925",
    "email": "beginin-oleg@yandex.ru",
    "password": "zaqwsx123",
    "password2": "zaqwsx123",

}

data_2 = {
    "login": "adminic",
    'last_name': 'Администратор',
    "first_name": "Админ",
    "phone_number": "89456758722",
    "email": "adminic@yandex.ru",
    "password": "zaqwsx123",
    "password2": "zaqwsx123",

}

data_3 = {
    "login": "student_1",
    'last_name': 'Петров',
    "first_name": "Вадим",
    "phone_number": "87776665544",
    "email": "student_1@yandex.ru",
    "password": "zaqwsx123",
    "password2": "zaqwsx123",
}

data_4 = {
    "login": "student_2",
    'last_name': 'Иванов',
    "first_name": "Иван",
    "phone_number": "85556668822",
    "email": "student_2@yandex.ru",
    "password": "zaqwsx123",
    "password2": "zaqwsx123",
}

headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, json=data_1, headers=headers)
print(response.status_code, response.json())
response = requests.post(url, json=data_2, headers=headers)
print(response.status_code, response.json())
response = requests.post(url, json=data_3, headers=headers)
print(response.status_code, response.json())
response = requests.post(url, json=data_4, headers=headers)
# Печать ответа от сервера
print(response.status_code, response.json())

