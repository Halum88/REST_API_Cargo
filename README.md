## REST API Service for Cargo Insurance Cost Calculation(test task)

## Description
This is a REST API service developed using FastAPI and Tortoise ORM. It provides the ability to calculate the cost of cargo insurance based on the type of cargo and the declared value.

## Technologies
**FastAPI** - <https://fastapi.tiangolo.com/>\
**Uvicorn** - <https://www.uvicorn.org/>\
**asynco** - <https://docs.python.org/3/library/asyncio.html>\
**PostgreSQL** - <https://postgresql.org/>\
**Docker** - <https://docker.com/>\
**Tortoise ORM**  - <https://tortoise.github.io/>

## Docker
**In order to get all the services started make sure you have an environment variables required to this project. place .env file with the variables below to the root directory of the project**
```
POSTGRES_USER = <user_name>
POSTGRES_PASSWORD = <user_password>
POSTGRES_DB = <name_db>
POSTGRES_HOST = <name_host>
POSTGRES_PORT = <port>
```
**To up and run the docker-compose use commands below**
```
docker-compose build
```
```
docker-compose up -d
```

**Located at the link**
*http://localhost:8000/*   
To view the result, you can use *http://localhost:8000/docs*

**Endpoint**
- date: YYYY-MM-DD
- cargo_type: Glass/Other
- cost: float

**Example answer**
```
{"calculated_cost":40.00}
```

**To disable docker-compose use command bellow**
```
docker-compose down -v
```