from fastapi import FastAPI
from src.routes.partnership import router as partnership
from src.routes.verify import router as verify
from src.routes.payment import router as payment

app = FastAPI()

app.include_router(verify)
app.include_router(partnership)
app.include_router(payment)

@app.get("/")
async def root():
    return {"message": "See the docs for how to consume this api"}
