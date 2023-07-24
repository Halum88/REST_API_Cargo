from fastapi import FastAPI
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from pydantic import BaseModel
import uvicorn
from tortoise.exceptions import DoesNotExist
from tortoise import Tortoise

app = FastAPI()

class Tariff(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=255)
    rate = fields.DecimalField(max_digits=8, decimal_places=4)


async def init():
    await Tortoise.init(
        db_url="sqlite://./db.sqlite3",
        modules={"models": ["__main__"]},
    )
    await Tortoise.generate_schemas()
    
    
async def create_tariff_table():
    
    tariffs_data = {
        "2020-06-01": [
            {
                "cargo_type": "Glass",
                "rate": "0.04"
            },
            {
                "cargo_type": "Other",
                "rate": "0.01"
            }
        ],
        "2020-07-01": [
            {
                "cargo_type": "Glass",
                "rate": "0.035"
            },
            {
                "cargo_type": "Other",
                "rate": "0.015"
            }
        ]
    }

    for date, tariffs in tariffs_data.items():
        print(date,'**',tariffs)
        for tariff_data in tariffs:
            tariff = Tariff(date=date, cargo_type=tariff_data["cargo_type"], rate=float(tariff_data["rate"]))
            await tariff.save()
            
class TariffSchema(BaseModel):
    rate: float

@app.get("/tariffs/{date}/{cargo_type}")
async def get_tariff(date: str, cargo_type: str):
    try:
        tariff = await Tariff.get(date=date, cargo_type=cargo_type)
        return {"rate": tariff.rate}
    except DoesNotExist:
        return {"error": "Tariff not found"}

register_tortoise(
    app,
    db_url="sqlite://./db.sqlite3",
    modules={"models": ["main"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_until_complete(create_tariff_table())
    uvicorn.run(app, host="0.0.0.0", port=8000)
