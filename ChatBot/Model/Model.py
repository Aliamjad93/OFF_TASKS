from pydantic import BaseModel
from typing import Optional

class Model(BaseModel):
    # Define a Pydantic model for input data
    
    text: str  # 'text' field to hold the user's input text
    type_of_text: Optional[str]  # 'type_of_text' field is optional and holds additional information
