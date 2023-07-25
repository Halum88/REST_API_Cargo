from tortoise import Tortoise
import asyncio
import os

DB_USER=os.environ['POSTGRES_USER']
DB_PASSWORD=os.environ['POSTGRES_PASSWORD']
DB_NAME=os.environ['POSTGRES_DB']
DB_HOST=os.environ['POSTGRES_HOST']
DB_PORT=os.environ['POSTGRES_PORT']



TORTOISE_CONFIG = {
    "connections": {
        "default": f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        }
    }
}

async def init():
    await Tortoise.init(config=TORTOISE_CONFIG)
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())

