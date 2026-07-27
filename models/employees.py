from database import db
from sqlalchemy.orm import relationship


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    role = db.Column(db.String(100), nullable=False)

    team = db.Column(db.String(100), nullable=False)

    salary = db.Column(db.Float, nullable=False)

    employment_type = db.Column(db.String(50), nullable=False)

    leave_balance = db.Column(
    db.Integer,
    nullable=False,
    default=21
)

    start_date = db.Column(db.Date, nullable=False)

    manager_id = db.Column(
    db.Integer,
    db.ForeignKey("employees.id"),
    nullable=True
)
    manager = relationship(
        "Employee",
        remote_side=[id],
        backref="subordinates"
    )

    is_active = db.Column(db.Boolean, default=True)