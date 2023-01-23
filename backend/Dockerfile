# syntax=docker/dockerfile:1

FROM python:3.10-alpine

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

RUN apk update \
    && apk upgrade \
    && apk add --no-cache curl

# Copy the project
COPY . .

# Install Poetry and dependencies
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry install --no-interaction --no-ansi --no-root

WORKDIR /app/simple_budget

CMD [ "poetry", "run", "uvicorn", "main:app" , "--reload"]
# CMD [ "/bin/ash" ]
