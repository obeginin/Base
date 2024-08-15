#!/bin/bash
docker-compose stop
docker-compose up -d
docker exec -t postgres pg_dump -U root -d test_db -f /tmp/backup.sql # создаём файл с резервной копией БД в контейнере
docker cp postgres:/tmp/backup.sql ./backup.sql # сохраняем данный файл с контейнера на хост машину
docker exec django_app python manage.py migrate users zero # Удаляем миграции
docker-compose stop  # Останавливаем контейнеры
docker-compose build # пересобираем
docker-compose up -d
docker exec django_app python manage.py makemigrations # делаем мигрции
docker exec django_app python manage.py migrate # применяем миграции
docker exec -i postgres psql -U root -d test_db -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;" # очищаем базу данных от всех записей
docker cp ./backup.sql postgres:/tmp/backup.sql  # копируем файл с копией в контейнер
docker exec -i postgres psql -U root -d test_db -f /tmp/backup.sql #восстанавливаем из файла
docker-compose stop
docker-compose up



