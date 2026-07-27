from flask import Blueprint, render_template, request, redirect, url_for
from models.employees import Employee
from datetime import datetime
from database import db

employee_bp = Blueprint("employee", __name__, template_folder="templates")

@employee_bp.route("/employees")
def list_employees():
    employees = Employee.query.all()
    return render_template("employees.html", employees=employees)

@employee_bp.route("/employees/new", methods=["GET", "POST"])
def new_employee():
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]
        team = request.form["team"]
        salary = float(request.form["salary"])
        employment_type = request.form["employment_type"]
        start_date = datetime.strptime(request.form["start_date"], "%Y-%m-%d").date()
        manager_id = request.form.get("manager_id")
        if manager_id:
            manager_id = int(manager_id)
        else:
            manager_id = None

        employee = Employee(
            name=name,
            role=role,
            team=team,
            salary=salary,
            employment_type=employment_type,
            start_date=start_date,
            manager_id=manager_id
       )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for("employee.list_employees"))
    managers = Employee.query.all()
    return render_template("new_employee.html", managers=managers)