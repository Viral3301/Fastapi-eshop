FROM python:3.11

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv

RUN pipenv install --system

COPY . .


CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
