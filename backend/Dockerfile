# syntax=docker/dockerfile:1
FROM python:3.9.14-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# install deps
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 80

# copy source
COPY . .