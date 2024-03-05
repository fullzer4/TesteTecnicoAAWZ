from fastapi import APIRouter

router = APIRouter()

@router.get("/comissions")
async def read_item():
    return {"message": "This is an example route"}

