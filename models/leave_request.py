from database import db
from datetime import datetime, timezone

class LeaveRequest(db.Model):
    __tablename__ = "leave_requests"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    leave_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default="Pending", nullable=False)
    reason = db.Column(db.Text, nullable=True)
    approved_by_manager_id = db.Column(
        db.Integer, db.ForeignKey("employees.id"), nullable=True)
    approved_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    employee = db.relationship(
        "Employee", foreign_keys=[employee_id], backref="leave_requests")
    approved_by_manager = db.relationship(
        "Employee", foreign_keys=[approved_by_manager_id],
          backref="approved_leave_requests")
    
    
    

