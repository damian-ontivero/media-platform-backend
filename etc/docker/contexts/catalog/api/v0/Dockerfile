FROM python:3.12.3-alpine

WORKDIR /app

COPY ./src/apps/catalog ./apps/catalog
COPY ./src/apps/shared ./apps/shared

COPY ./src/contexts/catalog ./contexts/catalog
COPY ./src/contexts/shared ./contexts/shared

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "apps.catalog.api.v0.main:app", "--host", "0.0.0.0", "--port", "8000"]
