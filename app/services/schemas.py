from typing import List
from pydantic import BaseModel

class StudentResponse(BaseModel):
    topic_title: str
    definition: str
    explanation: str
    examples: List[str]