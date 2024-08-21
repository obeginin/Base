import requests

# Json-запросы для добавления новых задач
url = "http://127.0.0.1:8001/api/tasks/"  # Замените на ваш URL

data_1 = {
    "category": "EGE_01",
    'resour': 'Demo_24',
    "number": "1001",
}

data_2 = {
    "category": "EGE_01",
    'resour': 'Demo_23',
    "number": "1002",
}

data_3 = {
    "category": "EGE_01",
    'resour': 'tester_24',
    "number": "1003",
}

data_4 = {
    "category": "EGE_01",
    'resour': 'Base(main)_24',
    "number": "1004",
}

data_5 = {
    "category": "EGE_01",
    'resour': 'Statgrad_24',
    "number": "1005",
}

data_6 = {
    "category": "EGE_01",
    'resour': 'Kabanov',
    "number": "1006",
}

data_7 = {
    "category": "EGE_01",
    'resour': 'Polyakov',
    "number": "1007",
}

data_8 = {
    "category": "EGE_01",
    'resour': 'Other',
    "number": "1008",
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
print(response.status_code, response.json())
response = requests.post(url, json=data_5, headers=headers)
print(response.status_code, response.json())
response = requests.post(url, json=data_6, headers=headers)
print(response.status_code, response.json())
response = requests.post(url, json=data_7, headers=headers)
print(response.status_code, response.json())
response = requests.post(url, json=data_8, headers=headers)

# Печать ответа от сервера
print(response.status_code, response.json())

