# django-worldclock
A website that shows the CURRENT time clock of 5 to 10 different countries in the world. 
Updated by the second. (Postgres database and dockerized). 
The user can also choose which countries he prefers to see and how the time format is showed. 23:30:23, 11:30PM, etc, etc

to run locally:

docker-compose up -d

docker-compose exec django python manage.py migrate


admin credentials: admin/admin