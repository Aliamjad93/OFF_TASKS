from pydantic import BaseModel

class Student(BaseModel):
    name: str
    description: str
    age: int