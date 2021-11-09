# pull from bas image

FROM python:3.7

#set environment  variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1


# Set work directory
WORKDIR /code

# Install dependencies

COPY Pipfile pipfile.lock /code/

RUN pip install pipenv && pipenv install --system


#copy project

COPY . /code/

