FROM python:3.10-slim-buster as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update -qq \
    && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
        apt-transport-https \
        apt-transport-https \
        build-essential \
        ca-certificates \
        curl \
        git \
        gnupg \
        jq \
        less \
        libpcre3 \
        libpcre3-dev \
        openssh-client \
        telnet \
        unzip \
        vim \
        wget \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && truncate -s 0 /var/log/*log

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="${PATH}:/root/.local/bin"

RUN poetry config virtualenvs.create false

RUN mkdir -p /app
WORKDIR /app

COPY . /app/

RUN poetry install  --no-interaction --no-ansi

ADD . /app
ENV DJANGO_SETTINGS_MODULE="django_celery.settings"

EXPOSE 8000

CMD python django_celery.manage.py runserver 0.0.0.0:8000