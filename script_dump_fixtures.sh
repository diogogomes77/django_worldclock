#!/bin/sh
docker-compose exec django python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > fixtures_$(date +%d%m%Y).json