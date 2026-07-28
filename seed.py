from app import app
from database import db

from models.employees import Employee
from models.leave_request import LeaveRequest
from models.payroll_run import PayrollRun
from models.payslip import Payslip

from services.payroll_service import generate_payslip

from datetime import date


with app.app_context():

    print("Adding sample data...")

    # Clear existing demo data
    Payslip.query.delete()
    LeaveRequest.query.delete()
    PayrollRun.query.delete()
    Employee.query.delete()

    db.session.commit()


    # Managers
    dennis = Employee(
        name="Dennis",
        role="SALES Manager",
        team="SALES",
        salary=80000,
        employment_type="Full Time",
        start_date=date(2026, 7, 28)
    )

    wachira = Employee(
        name="Wachira",
        role="IT Manager",
        team="IT",
        salary=80000,
        employment_type="Contract",
        start_date=date(2026, 7, 28),
        manager=dennis
    )


    db.session.add_all([
        dennis,
        wachira
    ])

    db.session.commit()


    # Employees
    employees = [
        Employee(
            name="Mwangi",
            role="Developer",
            team="Engineering",
            salary=90000,
            employment_type="Contract",
            start_date=date(2026,8,15),
            manager=wachira
        ),

        Employee(
            name="Wendy",
            role="Developer",
            team="Engineering",
            salary=120000,
            employment_type="Contract",
            start_date=date(2026,7,16),
            manager=wachira
        ),

        Employee(
            name="Wangari",
            role="Developer",
            team="Engineering",
            salary=140000,
            employment_type="Contract",
            start_date=date(2026,7,28),
            manager=wachira
        ),

        Employee(
            name="Tabby",
            role="Sales",
            team="Sales",
            salary=70000,
            employment_type="Full Time",
            start_date=date(2026,7,28),
            manager=dennis,
            is_active=False
        )
    ]


    db.session.add_all(employees)
    db.session.commit()


    # Leave request example
    leave = LeaveRequest(
        employee_id=employees[1].id,
        leave_type="Annual Leave",
        start_date=date(2026,8,9),
        end_date=date(2026,8,14),
        status="Pending",
        reason="Personal leave"
    )

    db.session.add(leave)


    # Payroll run
    payroll = PayrollRun(
        month=7,
        year=2026,
        status="Completed"
    )

    db.session.add(payroll)
    db.session.commit()


    print("Sample data inserted successfully!")