# Importing necessary libraries
from pydantic import BaseModel  # Required for defining data validation models
from typing import Optional  # Required for using the Optional type

# Creating a Pydantic BaseModel called 'lstm'
class lstm(BaseModel):
    # Defining attributes with their types for data validation
    input_text: str  # Attribute for input text (type: str)
    optional_param: Optional[str]  # Optional attribute (type: str)

# In this Pydantic model, 'optional_param' is marked as Optional, which means it can be omitted from input data.

