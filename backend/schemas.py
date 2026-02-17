from pydantic import BaseModel, Field
from typing import Optional, List

class ExerciseBase(BaseModel):
    name: str
    description: Optional[str] = None
    difficulty: str
    muscle_group: str
    equipment: List[str] = Field(default_factory=list)
    video_url: Optional[str] = None
    
class ExerciseCreate(ExerciseBase):
    pass

class ExerciseUpdate(ExerciseBase):
    name: Optional[str] = None
    description: Optional[str] = None
    difficulty: Optional[str] = None
    muscle_group: Optional[str] = None
    equipment: List[str] = Field(default_factory=list)
    video_url: Optional[str] = None
    
class ExerciseResponse(ExerciseBase):
    object_id: str