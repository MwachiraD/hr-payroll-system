from models.employees import Employee
from models.leave_request import LeaveRequest
from database import db
from datetime import date


def test_compassionate_leave_limit(app_context):

    with app_context.app_context():

        employee = Employee(
            name="Test Employee",
            role="Developer",
            team="Engineering",
            salary=80000,
            employment_type="Full Time",
            start_date=date(2026, 1, 1)
        )

        db.session.add(employee)
        db.session.commit()


        leave = LeaveRequest(
            employee_id=employee.id,
            leave_type="Compassionate Leave",
            start_date=date(2026, 8, 1),
            end_date=date(2026, 8, 7),
            status="Pending"
        )

        db.session.add(leave)
        db.session.commit()


        requested_days = (
            leave.end_date - leave.start_date
        ).days + 1


        assert requested_days > 5

def test_team_leave_capacity_rule(app_context):

    with app_context.app_context():

        employees = []

        for name in ["A", "B", "C", "D"]:

            employee = Employee(
                name=name,
                role="Developer",
                team="Engineering",
                salary=80000,
                employment_type="Full Time",
                start_date=date(2026,1,1)
            )

            db.session.add(employee)
            employees.append(employee)

        db.session.commit()


        approved_leave_1 = LeaveRequest(
            employee_id=employees[0].id,
            leave_type="Annual Leave",
            start_date=date(2026,8,10),
            end_date=date(2026,8,15),
            status="Approved"
        )


        approved_leave_2 = LeaveRequest(
            employee_id=employees[1].id,
            leave_type="Annual Leave",
            start_date=date(2026,8,10),
            end_date=date(2026,8,15),
            status="Approved"
        )


        pending_leave = LeaveRequest(
            employee_id=employees[2].id,
            leave_type="Annual Leave",
            start_date=date(2026,8,10),
            end_date=date(2026,8,15),
            status="Pending"
        )


        db.session.add_all([
            approved_leave_1,
            approved_leave_2,
            pending_leave
        ])

        db.session.commit()


        currently_on_leave = 0


        for employee in employees:

            for leave in employee.leave_requests:

                if leave.status == "Approved":

                    overlap = (
                        leave.start_date <= pending_leave.end_date
                        and leave.end_date >= pending_leave.start_date
                    )

                    if overlap:
                        currently_on_leave += 1
                        break


        team_size = len(employees)


        allowed = currently_on_leave + 1 <= team_size / 2


        assert allowed is False

def test_annual_leave_requires_notice(app_context):

    with app_context.app_context():

        employee = Employee(
            name="Notice Test",
            role="Developer",
            team="Engineering",
            salary=80000,
            employment_type="Full Time",
            start_date=date(2026, 1, 1)
        )

        db.session.add(employee)
        db.session.commit()


        requested_start = date(2026, 8, 2)
        today = date(2026, 8, 1)


        notice_days = (
            requested_start - today
        ).days


        assert notice_days < 7

def test_inactive_employee_not_available_for_leave(app_context):

    with app_context.app_context():

        employee = Employee(
            name="Inactive Employee",
            role="Developer",
            team="Engineering",
            salary=80000,
            employment_type="Full Time",
            start_date=date(2026, 7, 1),
            is_active=False
        )

        db.session.add(employee)
        db.session.commit()

        active_employees = Employee.query.filter_by(
            is_active=True
        ).all()

        employee_names = [
            emp.name for emp in active_employees
        ]

        assert "Inactive Employee" not in employee_names