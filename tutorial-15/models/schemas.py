from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from typing import Optional, Annotated
import re

class Student(BaseModel):
    roll_number : Annotated[str, Field(description="Student's roll number", example="A26-101")]
    name : Annotated[str, Field(description="Student's name, add Junior before name if age is less than 18", example="Ali Khan or Junior Ali")]
    age : Annotated[int, Field(description="Student's age", example=20)]
    city : Annotated[str, Field(description="Student's city", example="Karachi")] 

    @field_validator('roll_number')
    def validate_roll_number(cls, value):
        errors = []
        # Must start with A, B, or C
        if not value or value[0] not in {'A', 'B', 'C'}:
            errors.append("roll number must start with A, B, or C")
        # Year must be 26
        if len(value) < 3 or value[1:3] != "26":
            errors.append("roll number year must be '26'")
        # Last part must be exactly 3 digits after '-'
        if not re.match(r'^[ABC]26-\d{3}$', value):
            errors.append("roll number must end with exactly 3 digits after '-'")
        # If any errors found, raise combined ValueError
        if errors:
            raise ValueError("; ".join(errors))
        return value
    
    @field_validator('name')
    def validate_name(cls, value):
        value = value.strip()  # Remove leading/trailing whitespaces
        if not value:
            raise ValueError("name cannot be empty")
        if len(value) < 3:
            raise ValueError("name must be at least 3 characters long")
        if any(char.isdigit() for char in value):
            raise ValueError("name must not contain numbers")
        return value
    
    @field_validator('age')
    def validate_age(cls, value):
        if value < 16 or value > 30:
            raise ValueError("age must be between 16 and 30")
        return value
    
    @model_validator(mode='after')
    def cross_field_validation(cls, model):
        if model.age < 18 and not ("Student" in model.name or "Junior" in model.name):
            raise ValueError("If age is less than 18, name must contain 'Student' or 'Junior'")
        return model
    
    @computed_field(return_type=bool)
    @property
    def is_adult(self):
        return self.age >= 18
    
    @computed_field(return_type=int)
    @property
    def roll_numeric_part(self):
        # Extract the numeric part from roll_number
        match = re.match(r'^[ABC]26-(\d{3})$', self.roll_number)
        if match:
            return int(match.group(1))
        return None
    
class StudentUpdate(BaseModel):
    name : Optional[Annotated[str, Field(description="Student's name, add Junior before name if age is less than 18", example="Ali Khan or Junior Ali")]] = None
    age : Optional[Annotated[int, Field(description="Student's age", example=20)]] = None
    city : Optional[Annotated[str, Field(description="Student's city", example="Karachi")]] = None