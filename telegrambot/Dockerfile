FROM sunpeek/poetry:py3.12-slim

WORKDIR /telegrambot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ../pyproject.toml .
COPY ../poetry.lock .
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install --no-root

COPY . .

ENTRYPOINT ["poetry", "run"]
CMD ["python", "main.py"]
