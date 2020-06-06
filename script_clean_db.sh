#!/bin/bash
DB='django'
docker-compose stop django
docker-compose exec db psql -U postgres -c "DROP DATABASE $DB";
docker-compose exec db psql -U postgres -c "CREATE DATABASE $DB";
docker-compose start django