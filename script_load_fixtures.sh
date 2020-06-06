#!/bin/bash
docker-compose exec django python manage.py load_fixtures --file=$1