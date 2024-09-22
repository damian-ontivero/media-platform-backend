# Media Platform Backend

This repository is a learning hub dedicated to backend development using Python

## Installation

Requirements:

- `python~=3.12`

To install and run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/damian-ontivero/media-platform-backend.git`

2. Install dependencies:
    - `python -m pip install --upgrade pip`
    - `pip install pdm`
    - `pdm install`
3. Start PostgreSQL:
    - `docker compose -f .\etc\docker\postgres\compose.yaml up -d --build`
4. Start RabbitMQ:
    - `docker compose -f .\etc\docker\rabbitmq\compose.yaml up -d --build`
5. Start APIs:
    - With PDM:
        - `pdm run bo-api`
        - `pdm run ca-api`
    - With docker:
        - `docker compose -f .\etc\docker\contexts\backoffice\api\v0\compose.yaml up -d --build`
        - `docker compose -f .\etc\docker\contexts\catalog\api\v0\compose.yaml up -d --build`

It is also possible to start everything from a docker compose:
- `docker compose -f ./etc/docker/compose.yaml up -d --build`

## Usage

Once the server is running, you can access to:

- Backoffice:
    - Swagger: http://127.0.0.1:8001/swagger
    - Documentation: http://127.0.0.1:8002/documentation

- Catalog:
    - Swagger: http://127.0.0.1:8002/swagger
    - Documentation: http://127.0.0.1:8002/documentation


## About

Software design:

- Domain-Driven Design (DDD)
- Clean Architecture
- Command and Query Responsibility Segregation (CQRS)

Stack:

- FastAPI (https://fastapi.tiangolo.com)
- PostgreSQL (https://www.postgresql.org)
- SQLAlchemy (https://www.sqlalchemy.org)
- Alembic (https://alembic.sqlalchemy.org)
- RabbitMQ (https://www.rabbitmq.com)
- Docker (https://www.docker.com)
- ditainer (https://test.pypi.org/project/ditainer propietario)

Another RDBMS could be used.
As the project implements the repository pattern and clean architecture, the decision to change the
DBMS should not be a problem. At the moment the migrations are running in the docker build and this is not the best aproach.
If we would be using a CI/CD pipeline, de CD should be in charge of run migrations and the CI should deploy the env vars also.


## Filter in API

To filter the retrieved data, the API implements the Criteria pattern.
The criteria must be a base64-encoded JSON string with the following structure:

```json
{
    "filter": {
        "conjunction": "AND",
        "conditions": [
            {
                "field": "title",
                "operator": "CONTAINS",
                "value": "Amazing"
            }
        ]
    },
    "sort": [
        {
            "field": "title",
            "direction": "ASC"
        }
    ],
    "page_size": 15,
    "page_number": 1
}
```

To convert the JSON in one line you can use: https://www.text-utils.com/json-formatter/

To convert the JSON into base64 you can use: https://www.base64encode.org/
