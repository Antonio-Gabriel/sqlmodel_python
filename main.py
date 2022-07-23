from fastapi import FastAPI, Depends, status, HTTPException

from src.models import *

from src.schema.EmployeeSchema import EmployeeSchema

from src.config.engine import create_db_and_tables, get_dependencie, Session, select


app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "The app is run"}


@app.post("/employee", status_code=status.HTTP_201_CREATED)
async def create(employee: EmployeeSchema, session: Session = Depends(get_dependencie)):
    """Create an employee with address"""
    employee_model = Employee(
        name=employee.name, email=employee.email, phone=employee.phone
    )

    session.add(employee_model)
    session.commit()

    session.refresh(employee_model)

    employee_address = Address(
        country=employee.address.country,
        county=employee.address.county,
        streat=employee.address.streat,
        employee=employee_model,
        employee_id=employee_model.id,
    )

    session.add(employee_address)
    session.commit()

    # session.refresh(employee_model)
    # session.refresh(employee_address)

    return {"msg": "Employee successfully created"}


@app.get("/employees")
async def get(session: Session = Depends(get_dependencie)):
    """Get all employees"""
    statement = select(Employee)
    return {"employees": session.exec(statement).all()}


@app.get("/employee")
async def get_by_id(employee_id: int, session: Session = Depends(get_dependencie)):
    """Get employees by id"""

    employee = session.get(Employee, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


if __name__ == "__main__":
    create_db_and_tables()
