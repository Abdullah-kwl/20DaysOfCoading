from pydantic import BaseModel

class StudentSchema(BaseModel):
    name: str
    roll_number: int
    age: int
    
    @property
    def is_adult(self) -> bool:
        return self.age >= 18