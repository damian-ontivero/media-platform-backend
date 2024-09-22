FROM python:3.12.3-alpine

RUN apk add --no-cache ffmpeg

WORKDIR /app

COPY ./src/apps/backoffice ./apps/backoffice
COPY ./src/apps/shared ./apps/shared

COPY ./src/contexts/backoffice ./contexts/backoffice
COPY ./src/contexts/shared ./contexts/shared

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "apps.backoffice.api.v0.main:app", "--host", "0.0.0.0", "--port", "8000"]
