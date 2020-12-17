FROM python:3.8.5

WORKDIR /app
RUN adduser --uid 1000 --disabled-password --gecos '' --home /home/deploy deploy && \
    chown -R deploy:deploy /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gettext && \
    pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry==1.1.4
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

COPY --chown=deploy . /app
USER deploy

CMD ["python", "-m", "warden.main"]