## REST API Service for Cargo Insurance Cost Calculation(test task)

## Description
This is a REST API service developed using FastAPI and Tortoise ORM. It provides the ability to calculate the cost of cargo insurance based on the type of cargo and the declared value.

## Technologies
**FastAPI** - *fastapi.tiangolo.com/*
**Uvicorn** - *uvicorn.org/*
**asynco** - *docs.python.org/3/library/asyncio.html*
**PostgreSQL** - *postgresql.org/*
**Docker** - *docker.com/*
**Tortoise ORM** 

## Docker
**Create file .env and add the next:**
POSTGRES_USER = <user_name>
POSTGRES_PASSWORD = <user_password>
POSTGRES_DB = <name_db>
POSTGRES_HOST = <name_host>
POSTGRES_PORT = <port>

**Run docker-compose**
- docker-compose build
- docker-compose up -d

**Located at the link**
*http://localhost:8000/*
To view the result, you can use */docs*

**Endpoint**
- date: YYYY-MM-DD
- cargo_type: Glass/Other
- cost: integer

**Example answer**
   {
    "calculated_cost":40.00
   }

**Down docker-compose**
docker-compose down


