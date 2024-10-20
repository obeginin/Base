#!/bin/bash

docker exec -t postgres pg_dump -U root -d test_db -f /tmp/backup.sql # создаём файл с резервной копией БД в контейнере
docker cp postgres:/tmp/backup.sql ./back/backup.sql # сохраняем данный файл с контейнера на хост машину
docker exec django_app python manage.py migrate users zero # Удаляем миграции