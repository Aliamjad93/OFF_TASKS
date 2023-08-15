from pydantic import BaseModel

class House(BaseModel):
    income: float
    age: float
    room: float
    bath:float
    population:float