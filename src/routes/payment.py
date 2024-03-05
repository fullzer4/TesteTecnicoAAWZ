from fastapi import APIRouter

router = APIRouter()

@router.get("/payment")
async def read_item():
    return {"message": "This is an example route"}

