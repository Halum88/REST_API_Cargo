
# REST API Service for Cargo Insurance Cost Calculation

## Description
This is a REST API service developed using FastAPI and Tortoise ORM. It provides the ability to calculate the cost of cargo insurance based on the type of cargo and the declared value.

## Dependencies
Before running the service, make sure you have the following dependencies installed:

1. Python 3.7 and above
2. FastAPI
3. Tortoise ORM
4. uvicorn

## Running the Service
To run the service, follow these steps:

1. Install the required dependencies:
pip install fastapi tortoise-orm uvicorn


2. Start the server using uvicorn:
uvicorn main:app --host 0.0.0.0 --port 8000


3. The API will be available at `http://localhost:8000`.

## Data Model
The service uses the Tariff data model, which represents a table in the database with the following fields:

- id (integer, primary key)
- date (date when the tariff was applied)
- cargo_type (type of cargo)
- rate (insurance rate)

## Endpoints

### GET /tariffs/{date}/{cargo_type}
Get the insurance cost for the specified cargo type and date.

Parameters:
- `date`: date in the format YYYY-MM-DD
- `cargo_type`: type of cargo (e.g., "Glass" or "Other")

Response:
- If the tariff is found, it returns a JSON object with the `rate` key containing the insurance cost for the specified parameters.
- If the tariff is not found, it returns a JSON object with the `error` key containing the message "Tariff not found".

## Loading Tariffs
Cargo insurance tariffs can be loaded into the database when the service is started. The `create_tariff_table()` function in the code defines tariffs for different dates and cargo types. When the service is launched, this function will automatically add the tariffs to the database.

## Database
The service uses an SQLite database. The database will be created automatically when the service is started if it does not exist. The tariff data is stored in the Tariff table.

## Docker
For the convenience of deploying the service in a Docker environment, a `Dockerfile` is provided. You can create a Docker image and run the container using the following commands:

1. Build the Docker image:
docker build -t my_tariff_api .


2. Run the container:
docker run -d -p 8000:8000 my_tariff_api


After that, the service will be available at `http://localhost:8000`.

