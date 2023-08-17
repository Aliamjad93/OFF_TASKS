# Importing the necessary library
from pydantic import BaseModel

# Creating a Pydantic BaseModel called 'Student'
class Student(BaseModel):
    # Defining attributes with their types for data validation and serialization
    name: str  # Attribute for the student's name (type: str)
    description: str  # Attribute for the student's description (type: str)
    age: int  # Attribute for the student's age (type: int)
