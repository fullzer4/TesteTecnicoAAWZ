from fastapi import APIRouter

router = APIRouter()

@router.get("/partnership")
async def read_item():
    return {"message": "This is an example route"}

