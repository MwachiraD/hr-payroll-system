from database import db


class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    role = db.Column(db.String(100), nullable=False)

    team = db.Column(db.String(100), nullable=False)

    salary = db.Column(db.Float, nullable=False)

    employment_type = db.Column(db.String(50), nullable=False)

    start_date = db.Column(db.Date, nullable=False)

    is_active = db.Column(db.Boolean, default=True)