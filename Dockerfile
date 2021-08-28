FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/space
COPY . .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev curl

# Install and setup poetry.
RUN pip install -U pip \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

# Install requirements.
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

