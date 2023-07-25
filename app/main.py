from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.tortoise_settings import TORTOISE_CONFIG
from fastapi import FastAPI, HTTPException
from app.models import Tariff


app = FastAPI()

register_tortoise(
    app,
    db_url= TORTOISE_CONFIG["connections"]["default"],
    modules={"models":["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
    )

#add tariffs in DB
@app.post("/tariffs/")
async def create_tariffs(data: dict):
    try:
        for date, tariffs in data.items():
            for tariff_data in tariffs:
                tariff = await Tariff.create(
                    date=date,
                    cargo_type=tariff_data["cargo_type"],
                    rate=tariff_data["rate"]
                )
        return {"message": "Tariffs successfully created."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#get insurance cost
@app.get("/tariffs/")
async def get_tariffs(date: str, cargo_type: str, cost: float):
    try:
        tariff = await Tariff.filter(date__lte=date, 
                                     cargo_type=cargo_type).order_by('-date').first() #take the last one by date, because the price may not be loaded on the day of the request.
                
        if tariff:
            calculated_cost = float(tariff.rate) * cost
            return {"calculated_cost": round(calculated_cost,2)}
        else:
            raise HTTPException(status_code=404, detail="Tariff not found for the provided date and cargo type.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
