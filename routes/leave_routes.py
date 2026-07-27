from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.leave_request import LeaveRequest
from models.employees import Employee
from database import db
from datetime import datetime

leave_bp = Blueprint("leave", __name__, template_folder="templates")

@leave_bp.route("/leave_requests")
def list_leave_requests():
    leave_requests = LeaveRequest.query.all()
    return render_template("leave_requests.html", leave_requests=leave_requests)

@leave_bp.route("/leave_requests/new", methods=["GET", "POST"])
def new_leave_request():
    if request.method == "POST":
        employee_id = int(request.form["employee_id"])
        leave_type = request.form["leave_type"]
        start_date = datetime.strptime(request.form["start_date"], "%Y-%m-%d").date()
        end_date = datetime.strptime(request.form["end_date"], "%Y-%m-%d").date()
        reason = request.form.get("reason")
        if end_date < start_date:
            flash("End date cannot be before start date.", "error")
            return redirect(url_for("leave.new_leave_request"))
        today = datetime.now().date()
        if leave_type in ["Annual Leave", "Unpaid Leave"]:
            if start_date < today:
                flash(f"Start date cannot be in the past for {leave_type}.", "error")
                return redirect(url_for("leave.new_leave_request"))
            notice_days = (start_date - today).days
            if notice_days < 7:
                flash(f"You must give at least 7 days' notice for {leave_type}.", "error")
                return redirect(url_for("leave.new_leave_request"))

        if leave_type in ["Sick Leave", "Compassionate Leave"]:
            notice_days = (start_date - today).days
            if notice_days < 0 or notice_days > 1:
                flash(f"{leave_type} can only start today or tomorrow.", "error")
                return redirect(url_for("leave.new_leave_request"))

        existing_leave = LeaveRequest.query.filter(
            LeaveRequest.employee_id == employee_id,
            LeaveRequest.status.in_(["Pending", "Approved"]),
        
        ).all()

        for leave in existing_leave:
            if (start_date <= leave.end_date and end_date >= leave.start_date):
                flash("You already have a leave request that overlaps with this period.", 
                      "error")
                return redirect(url_for("leave.new_leave_request"))

        requested_days = (end_date - start_date).days + 1
        employee = Employee.query.get(employee_id)
        if leave_type == "Annual Leave":
            if employee.leave_balance < requested_days:
                flash(
                    f"you only have {employee.leave_balance} days of annual leave remaining.",
                       "error")
                return redirect(url_for("leave.new_leave_request"))
        
        
        leave_request = LeaveRequest(
            employee_id=employee_id,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )
        db.session.add(leave_request)
        db.session.commit()
        return redirect(url_for("leave.list_leave_requests"))

    employees = Employee.query.all()
    return render_template("new_leave_request.html", employees=employees)


@leave_bp.route("/leave_requests/<int:leave_id>/approve", methods=["POST"])
def approve_leave(leave_id):
    return " Approve leave functionality to be implemented"

@leave_bp.route("/leave_requests/<int:leave_id>/reject", methods=["POST"])
def reject_leave(leave_id):
    return "Reject route works"