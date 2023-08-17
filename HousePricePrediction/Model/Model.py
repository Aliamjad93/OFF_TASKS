# Importing the necessary library
from pydantic import BaseModel  # Required for defining data validation models

# Creating a Pydantic BaseModel called 'House'
class House(BaseModel):
    # Defining attributes with their types for data validation
    income: float       # Attribute for income (type: float)
    age: float          # Attribute for age (type: float)
    room: float         # Attribute for number of rooms (type: float)
    bath: float         # Attribute for number of baths (type: float)
    population: float   # Attribute for population (type: float)
