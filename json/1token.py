import requests

url = "http://127.0.0.1:8001/api/token/"  # Замени на URL конечной точки
data = {

# Проблема опять что у меня вместо username используется login
    "username": "root",
    "password": "root"
}

response = requests.post(url, data=data)

# Проверка успешности получения токена
if response.status_code == 200:
    token = response.json().get("access_token")  # Токен доступа
    print("Access Token:", token)
else:
    print("Error:", response.status_code, response.text)