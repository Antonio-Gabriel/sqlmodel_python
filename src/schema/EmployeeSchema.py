from typing import Optional
from pydantic import BaseModel


class AddressSchema(BaseModel):
    country: str
    county: str
    streat: str


class EmployeeSchema(BaseModel):
    name: str
    email: str
    phone: Optional[str]
    address: AddressSchema
