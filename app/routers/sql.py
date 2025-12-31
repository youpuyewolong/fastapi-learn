from fastapi import APIRouter
from app.model.hero import Hero
from sqlmodel import Session, SQLModel, create_engine
router = APIRouter()


@router.get("/hello")
async def hello_world():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    engine = create_engine("sqlite:///database.db")

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()

    return {"message": "Hello World"}