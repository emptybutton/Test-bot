FROM sunpeek/poetry:py3.12-slim

WORKDIR /calculator

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PATH "/root/.local/bin:$PATH"

COPY pyproject.toml .
COPY poetry.lock .
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install --no-root

COPY . .

ENTRYPOINT ["poetry", "run"]
CMD ["uvicorn", "src.presentation.app:app"]
