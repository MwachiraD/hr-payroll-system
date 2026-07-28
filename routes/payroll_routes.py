from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.payroll_run import PayrollRun
from services.payroll_service import generate_payroll
from datetime import datetime
from models.payslip import Payslip


payroll_bp = Blueprint(
    "payroll",
    __name__,
    template_folder="templates"
)


@payroll_bp.route("/payroll")
def payroll_dashboard():

    payroll_runs = PayrollRun.query.all()

    return render_template(
        "payroll_dashboard.html",
        payroll_runs=payroll_runs
    )

@payroll_bp.route("/payroll/generate", methods=["POST"])
def create_payroll():

    month = int(request.form["month"])
    year = int(request.form["year"])

    payroll = generate_payroll(month, year)

    flash(
        f"Payroll for {month}/{year} generated successfully.",
        "success"
    )

    return redirect(url_for("payroll.payroll_dashboard"))


@payroll_bp.route("/payroll/<int:payroll_id>/payslips")
def view_payslips(payroll_id):

    payroll = PayrollRun.query.get_or_404(payroll_id)

    return render_template(
        "payslips.html",
        payroll=payroll
    )