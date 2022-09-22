FROM python:3.10-slim as builder

RUN apt update && apt install -y gcc python3-dev gcc
RUN pip install -U pip setuptools wheel pdm

WORKDIR /app
COPY pyproject.toml pdm.lock /app/

RUN pdm export -o requirements.txt

FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y gcc python3-dev gcc

COPY --from=builder /app/requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["uvicorn", "app:app", "--port", "4000", "--host", "0.0.0.0", "--reload"]
