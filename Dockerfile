# Pull from base image
FROM python:3.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory inside docker container
# if we need to run any command inside container,
# docker will run from this directory
WORKDIR /code

# Install dependencies
RUN pip install django==2.2.3
RUN pip install psycopg2-binary==2.8.3
RUN pip install django-crispy-forms==1.7.1
RUN pip install django-allauth==0.38.0
RUN pip install pillow==5.4.1 django-debug-toolbar==1.11
RUN pip install whitenoise==4.1.2 gunicorn==19.9.0
RUN pip install dj-database-url==0.5.0

# Copy project from local folder where Dockerfile is (.) to
# /code/ directory inside container
COPY . /code/