from fastapi import FastAPI, Depends
from .database import get_db
from . import schemas, crud

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/exercise")
async def create_exercise(exercise: schemas.ExerciseCreate, db=Depends(get_db)):
    return await crud.create_exercise(db, exercise)
