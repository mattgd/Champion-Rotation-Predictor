# pull official base image
FROM python:3.9-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# flask app environment variable
ENV FLASK_APP app.py

# start server
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
