# pull official base image
FROM python:3.9-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
# prevents python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevents python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# flask app environment variable
ENV FLASK_APP app.py

# open port 5000 for requests
EXPOSE 5000

ARG scrape

# start server
ENTRYPOINT ["./entrypoint.sh"]
