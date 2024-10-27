ob1. Установите виртуальное окружение sudo apt install python3-venv
2. Активируйте виртуальное окружение source myenv/bin/activate
2. Скачать проект в папку на своем ПК git clone https://github.com/obeginin/Base.git
3. установить docker и docker-compose для запуска
sudo apt update
sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker $USER ( $USER поменять на своего)
собрать и запустить проект docker-compose up --build


мой небольшой локальный проект

Шаги выполнения проекта:

pip install --upgrade pip (обновляем менеджер пакетов pip до послдней верси)
pip install django (устанавливаем Django)
pip install djangorestframework (устанавиаем библиотеку REST для работ с API)
django-admin startproject loc (создаем Django приложени loc)
sudo apt install postgresql postgresql-contribib (устанавливаем PostgresSQL с дп модулями)
sudo apt install libpq-dev python3-dev (устанавливаем пакет необходимый для работы psycopg2 и другие модули)
pip install psycopg2 (Устанавливем библиотеку psycopg2, которая позволяет Python-приложению взаимодействовать с PostgreSQL)
создал базу данных: local_db, с таблицей local_table
python manage.py createsuperuser (Создаем супепользователя для полного доступа к БД логин:oleg пароль:oleg)
python manage.py migrate (Выполняем миграции БД) в данном случае для админки, аворизации
pip install django-environ (Устанавливаем библиотеку для работы с переменным окружением, файл .env)
pip install gunicorn (устанавливаем )
employees/models.py Создаём модель для хранения информаци о сотрудниках
employees/serializers.py (Создаём Сериализатор для преобразования данных модели в формат json дл API)
employees/views.py (создаем предствления которые обрабатывают запросы к API и возвращают соответствующие данные)
employees/urls.py (Добавляем маршруты для API)
loc/urls.py (Добавляем маршруты для API в основной файл проекта)
python manage.py makemigrations (создаём миграции)
python manage.py migrate (применяем их к базе данных)
gunicorn loc.wsgi:application --bind 0.0.0.0:8000 --log-level info (запускаем сервер)