from fastapi import APIRouter
import httpx


router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


