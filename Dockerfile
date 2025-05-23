FROM python:3.12-slim

RUN pip install uv uvicorn

WORKDIR /app

COPY pyproject.toml /app/

RUN pip install .

COPY ./app /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
