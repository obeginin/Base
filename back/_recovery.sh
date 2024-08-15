#!/bin/bash


docker exec django_app python manage.py makemigrations # делаем мигрции
docker exec django_app python manage.py migrate # применяем миграции
docker exec -i postgres psql -U root -d test_db -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;" # очищаем базу данных от всех записей
docker cp ./backup.sql postgres:/tmp/backup.sql
docker exec -i postgres psql -U root -d test_db -f /tmp/backup.sql #восстанавливаем из файла