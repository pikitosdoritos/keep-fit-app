from sqlalchemy.orm import Session
from . import schemas, models

async def create_exercise(db, exercise):
    result = await db.exercises.insert_one(exercise.model_dump())
    return {"id": str(result.inserted_id)}
