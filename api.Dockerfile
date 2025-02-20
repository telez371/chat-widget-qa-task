FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install "poetry==1.7.1"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./

ARG POETRY_GROUP=api
RUN poetry install --no-root --with ${POETRY_GROUP}

RUN curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

WORKDIR /app

COPY . .

ENV GIT_PYTHON_REFRESH=quiet