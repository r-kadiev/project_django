FROM python:3.9-alpine3.16
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /temp/requirements.txt
COPY . /code
WORKDIR /code
EXPOSE 8000

RUN python -m pip install --upgrade pip
RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r requirements.txt
RUN adduser --disabled-password code-user

USER code-user
