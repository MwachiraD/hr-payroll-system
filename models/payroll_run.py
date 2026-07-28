from database import db
from datetime import datetime


class PayrollRun(db.Model):
    __tablename__ = "payroll_runs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    month = db.Column(
        db.Integer,
        nullable=False
    )

    year = db.Column(
        db.Integer,
        nullable=False
    )

    generated_at = db.Column(
        db.DateTime,
        default=datetime.now
    )

    status = db.Column(
        db.String(20),
        default="Completed"
    )