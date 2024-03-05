from fastapi import FastAPI
from src.routes.payment import router as payment
from src.routes.partnership import router as partnership
from src.routes.comissions import router as comissions

app = FastAPI()

app.include_router(payment)
app.include_router(comissions)
app.include_router(partnership)

@app.get("/")
async def root():
    return {"message": "See the docs for how to consume this api"}
