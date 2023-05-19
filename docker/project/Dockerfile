FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /temp/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /temp/requirements.txt
COPY . /code/
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000