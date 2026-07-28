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


    # =========================
    # Managers
    # =========================

    dennis = Employee(
        name="Dennis",
        role="SALES Manager",
        team="SALES",
        salary=80000,
        employment_type="Full Time",
        start_date=date(2026, 7, 1)
    )


    wachira = Employee(
        name="Wachira",
        role="IT Manager",
        team="IT",
        salary=80000,
        employment_type="Contract",
        start_date=date(2026, 7, 1),
        manager=dennis
    )


    db.session.add_all([
        dennis,
        wachira
    ])

    db.session.commit()


    # =========================
    # Employees
    # =========================

    mwangi = Employee(
        name="Mwangi",
        role="Developer",
        team="Engineering",
        salary=90000,
        employment_type="Contract",
        start_date=date(2026, 8, 15),
        manager=wachira
    )


    wendy = Employee(
        name="Wendy",
        role="Developer",
        team="Engineering",
        salary=120000,
        employment_type="Contract",
        start_date=date(2026, 7, 16),
        manager=wachira
    )


    wangari = Employee(
        name="Wangari",
        role="Developer",
        team="Engineering",
        salary=140000,
        employment_type="Contract",
        start_date=date(2026, 7, 28),
        manager=wachira
    )


    tabby = Employee(
        name="Tabby",
        role="Sales",
        team="Sales",
        salary=70000,
        employment_type="Full Time",
        start_date=date(2026, 7, 28),
        manager=dennis,
        is_active=False
    )


    db.session.add_all([
        mwangi,
        wendy,
        wangari,
        tabby
    ])

    db.session.commit()


    # =========================
    # Leave Requests
    # =========================


    # Pending annual leave
    annual_pending = LeaveRequest(
        employee_id=wendy.id,
        leave_type="Annual Leave",
        start_date=date(2026, 8, 10),
        end_date=date(2026, 8, 14),
        status="Pending",
        reason="Family holiday"
    )


    # Approved annual leave
    annual_approved = LeaveRequest(
        employee_id=wangari.id,
        leave_type="Annual Leave",
        start_date=date(2026, 8, 17),
        end_date=date(2026, 8, 19),
        status="Approved",
        reason="Personal commitment",
        approved_by_manager_id=wachira.id
    )


    # Sick leave
    sick_leave = LeaveRequest(
        employee_id=wendy.id,
        leave_type="Sick Leave",
        start_date=date(2026, 7, 30),
        end_date=date(2026, 7, 31),
        status="Approved",
        reason="Medical appointment",
        approved_by_manager_id=wachira.id
    )


    # Compassionate leave
    compassionate_leave = LeaveRequest(
        employee_id=mwangi.id,
        leave_type="Compassionate Leave",
        start_date=date(2026, 8, 20),
        end_date=date(2026, 8, 22),
        status="Approved",
        reason="Family emergency",
        approved_by_manager_id=wachira.id
    )


    # Unpaid leave - important for payroll deduction testing
    unpaid_leave = LeaveRequest(
        employee_id=wendy.id,
        leave_type="Unpaid Leave",
        start_date=date(2026, 7, 20),
        end_date=date(2026, 7, 24),
        status="Approved",
        reason="Extended personal leave",
        approved_by_manager_id=wachira.id
    )


    db.session.add_all([
        annual_pending,
        annual_approved,
        sick_leave,
        compassionate_leave,
        unpaid_leave
    ])

    db.session.commit()


    # =========================
    # Payroll
    # =========================

    payroll = PayrollRun(
        month=7,
        year=2026,
        status="Completed"
    )

    db.session.add(payroll)

    db.session.commit()


    # Generate payslips only for active employees
    active_employees = Employee.query.filter_by(
        is_active=True
    ).all()


    for employee in active_employees:

        generate_payslip(
            employee,
            payroll
        )


    db.session.commit()


    print("Sample data inserted successfully!")