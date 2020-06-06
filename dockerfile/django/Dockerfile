FROM python:3.8.2-buster

ENV PYTHONUNBUFFERED 1
WORKDIR /code

RUN apt-get update && apt-get install -y \
postgresql-client \
&& rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD . /code/
RUN mkdir -p /code/static
