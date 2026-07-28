from models.leave_request import LeaveRequest
from models.payroll_run import PayrollRun
from models.payslip import Payslip
from database import db
from datetime import datetime


def calculate_employee_payroll(employee):

    gross_pay = employee.salary

    unpaid_leave_days = 0

    # Find approved unpaid leave
    for leave in employee.leave_requests:

        if (
            leave.leave_type == "Unpaid Leave"
            and leave.status == "Approved"
        ):
            days = (leave.end_date - leave.start_date).days + 1
            unpaid_leave_days += days


    # Deduct unpaid leave
    daily_salary = gross_pay / 30

    unpaid_deduction = (
        daily_salary * unpaid_leave_days
    )

    taxable_pay = gross_pay - unpaid_deduction


    # Temporary tax rules
    tax = taxable_pay * 0.10

    housing_levy = taxable_pay * 0.015


    net_pay = (
        taxable_pay
        - tax
        - housing_levy
    )


    return {
        "gross_pay": gross_pay,
        "unpaid_leave_days": unpaid_leave_days,
        "tax": tax,
        "housing_levy": housing_levy,
        "net_pay": net_pay
    }

def generate_payslip(employee, payroll_run):

    payroll_data = calculate_employee_payroll(employee)

    payslip = Payslip(
        payroll_run_id=payroll_run.id,
        employee_id=employee.id,
        gross_pay=payroll_data["gross_pay"],
        unpaid_leave_days=payroll_data["unpaid_leave_days"],
        tax=payroll_data["tax"],
        housing_levy=payroll_data["housing_levy"],
        net_pay=payroll_data["net_pay"]
    )

    db.session.add(payslip)

    return payslip

def generate_payroll(month, year):

    from models.payroll_run import PayrollRun
    from models.employees import Employee
    from database import db

    existing_payroll = PayrollRun.query.filter_by(
        month=month,
        year=year
    ).first()

    if existing_payroll:
        return existing_payroll


    payroll_run = PayrollRun(
        month=month,
        year=year,
        status="Completed"
    )

    db.session.add(payroll_run)
    db.session.commit()


    employees = Employee.query.filter_by(
        is_active=True
    ).all()


    for employee in employees:
        generate_payslip(
            employee,
            payroll_run
        )


    db.session.commit()


    return payroll_run