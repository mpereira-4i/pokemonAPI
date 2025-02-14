from pydantic import BaseModel, Field
from models.helpers import Name, BaseStats
from typing import List, Dict

class Pokemon(BaseModel):
    id: int
    name: Name
    type: List[str] = Field(..., example=["Grass", "Poison"])
    base: BaseStats
    
