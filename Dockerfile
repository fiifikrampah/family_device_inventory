# This Dockerfile is used for production deployments

FROM python:3.9.6-slim-buster
LABEL maintainer "Fiifi Krampah"

# Copy all necessary files into the container
COPY . /code

# Set the working directory to/code
WORKDIR /code

# Install all dependencies
RUN pip install -r requirements.txt

# Set Flask ENV to production mode
ENV FLASK_ENV=prod

# Set SECRET_KEY environment varaible
ENV SECRET_KEY=VerySecureKey

# Expose the port needed for the app
EXPOSE 5000
