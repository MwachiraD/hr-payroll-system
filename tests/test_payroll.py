from models.employees import Employee
from models.leave_request import LeaveRequest
from services.payroll_service import calculate_employee_payroll
from database import db
from datetime import date


def test_unpaid_leave_deduction(app_context):

    with app_context.app_context():

        employee = Employee(
            name="Test Employee",
            role="Developer",
            team="Engineering",
            salary=90000,
            employment_type="Full Time",
            start_date=date(2026,1,1)
        )

        db.session.add(employee)
        db.session.commit()


        leave = LeaveRequest(
            employee_id=employee.id,
            leave_type="Unpaid Leave",
            start_date=date(2026,8,1),
            end_date=date(2026,8,10),
            status="Approved"
        )


        db.session.add(leave)
        db.session.commit()


        payroll = calculate_employee_payroll(
            employee,
            8,
            2026
        )


        assert payroll["unpaid_leave_days"] == 10
        assert payroll["gross_pay"] == 90000
        assert payroll["net_pay"] < 90000

def test_mid_month_joiner_prorated_salary(app_context):

    with app_context.app_context():

        employee = Employee(
            name="New Employee",
            role="Developer",
            team="Engineering",
            salary=90000,
            employment_type="Full Time",
            start_date=date(2026, 8, 15)
        )

        db.session.add(employee)
        db.session.commit()


        payroll = calculate_employee_payroll(
            employee,
            8,
            2026
        )


        assert round(payroll["gross_pay"], 2) == 49354.84

def test_employee_with_no_unpaid_leave(app_context):

    with app_context.app_context():

        employee = Employee(
            name="Clean Payroll Employee",
            role="Developer",
            team="Engineering",
            salary=80000,
            employment_type="Full Time",
            start_date=date(2026, 1, 1)
        )

        db.session.add(employee)
        db.session.commit()


        payroll = calculate_employee_payroll(
            employee,
            8,
            2026
        )


        assert payroll["unpaid_leave_days"] == 0

        assert payroll["gross_pay"] == 80000

        assert payroll["net_pay"] > 0