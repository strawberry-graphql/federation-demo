FROM python:alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dev dependencies
RUN apk update \
    && apk add curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

RUN pip install -U pip \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock /usr/src/app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

CMD poetry run task server
