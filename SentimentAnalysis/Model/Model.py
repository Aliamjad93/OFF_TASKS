from pydantic import BaseModel

# Define a Pydantic model class to represent input data
class Model(BaseModel):
    # Define a field named 'text' with type annotation 'str'
    text: str
