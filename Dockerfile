# This Dockerfile is used for production deployments

FROM python:3.9.6-slim-buster
LABEL maintainer "Fiifi Krampah"

COPY requirements.txt requirements.txt

COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt

# Set Flask ENV to production mode
ENV FLASK_ENV=prod

# Set SECRET_KEY environment varaible
ENV SECRET_KEY=VerySecureKey
