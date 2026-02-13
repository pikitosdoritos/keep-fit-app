from pydantic import BaseModel
from typing import List, Optional 

class Excercise(BaseModel):
    name: str
    description: Optional[str] = None
    difficulty: str
    muscle_group: str
    equipment: List[str] = []
    video_url: Optional[str] = None