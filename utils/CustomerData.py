from pydantic import BaseModel,Field
from typing import Literal






class CustomerData(BaseModel):
    CreditScore:int =Field(description="credit score",ge=0)
    Geography:Literal['France', 'Spain', 'Germany']
    Gender:Literal['Female', 'Male']
    Age:int=Field(description="Age of client",ge=18,le=100)
    Tenure:int=Field(description="number of years dealing with the client",ge=0,le=10)
    Balance:float=Field(description="the balance of client",ge=0)
    NumOfProducts:int=Field(description="number of product",ge=1,le=4)
    HasCrCard:Literal[0, 1]=Field(description="only Yes[1] or No[0]")
    IsActiveMember:Literal[0, 1]=Field(description="only Yes[1] or No[0]")
    EstimatedSalary:float=Field(description="the salary of client",ge=0)