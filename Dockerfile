# This Dockerfile is used for production deployments

FROM python:3.9.6-slim-buster
LABEL maintainer "Fiifi Krampah"

COPY requirements.txt requirements.txt
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev && \
    rm -rf /var/cache/apk/*

RUN pip install -r requirements.txt

COPY . /code
WORKDIR /code

# Set Flask ENV to production mode
ENV FLASK_ENV=prod

EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:5000", "--log-level", "INFO", "manage:app" ]