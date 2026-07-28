from flask import Blueprint, render_template
from models.leave_request import LeaveRequest
from models.employees import Employee
from models.payroll_run import PayrollRun
from datetime import datetime

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    template_folder="templates"
)


@dashboard_bp.route("/dashboard")
def dashboard():

    today = datetime.now().date()

    # Pending approvals
    pending_leaves = LeaveRequest.query.filter_by(
        status="Pending"
    ).all()


    # Employees currently on leave
    employees_on_leave = LeaveRequest.query.filter(
        LeaveRequest.status == "Approved",
        LeaveRequest.start_date <= today,
        LeaveRequest.end_date >= today
    ).all()


    # Leave balances
    employees = Employee.query.filter_by(
        is_active=True
    ).all()


    # Latest payroll runs
    payroll_runs = PayrollRun.query.order_by(
        PayrollRun.id.desc()
    ).limit(5).all()


    return render_template(
        "dashboard.html",
        pending_leaves=pending_leaves,
        employees_on_leave=employees_on_leave,
        employees=employees,
        payroll_runs=payroll_runs
    )