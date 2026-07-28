from database import db
from datetime import datetime


class Payslip(db.Model):
    __tablename__ = "payslips"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    payroll_run_id = db.Column(
        db.Integer,
        db.ForeignKey("payroll_runs.id"),
        nullable=False
    )

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    gross_pay = db.Column(
        db.Float,
        nullable=False
    )

    unpaid_leave_days = db.Column(
        db.Integer,
        default=0
    )

    tax = db.Column(
        db.Float,
        default=0
    )

    housing_levy = db.Column(
        db.Float,
        default=0
    )

    net_pay = db.Column(
        db.Float,
        nullable=False
    )

    generated_at = db.Column(
        db.DateTime,
        default=datetime.now
    )


    payroll_run = db.relationship(
        "PayrollRun",
        backref="payslips"
    )

    employee = db.relationship(
        "Employee",
        backref="payslips"
    )