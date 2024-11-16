from pydantic import BaseModel

class EmployeeData(BaseModel):

    education_level: str
    joining_year:int
    city:str
    PaymentTier:int
    age: int
    gender:str
    EverBenched:str
    ExperienceInCurrentDomain:int
    LeaveOrNot:int
   
   
