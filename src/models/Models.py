from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class Employee(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    phone: Optional[str]

    addresses: List["Address"] = Relationship()


class Address(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    country: str
    county: str
    streat: str
    employee_id: Optional[int] = Field(default=None, foreign_key="employee.id")
    employee: Optional[Employee] = Relationship()
