# pull official base image
FROM python:3.12-alpine3.19

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install pipenv and project dependencies
RUN pip install -U pipenv
RUN apk add --no-cache gcc musl-dev zlib-dev
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --dev --system --deploy --ignore-pipfile

# copy all other fise in wotk direactory
COPY . /app/

# open by that port
EXPOSE 8000