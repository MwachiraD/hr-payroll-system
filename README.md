# HR & Payroll System

## Overview

The HR & Payroll System is a Flask-based internal business application developed for the Vunoh Global Software & AI Engineering practical assessment.

The system helps organizations manage core HR operations that are commonly handled through spreadsheets and manual processes:

- Employee records
- Organizational reporting structure
- Leave requests and approvals
- Leave balance tracking
- Monthly payroll generation
- Payslip generation

The focus of this project was implementing realistic business rules and workflows rather than building simple CRUD functionality.

---

# Technology Stack

## Backend

- Flask
- SQLAlchemy ORM
- SQLite Database

## Frontend

- HTML
- CSS
- Jinja2 Templates

---

# Implemented Features

## 1. Employee Management

The system supports:

- Creating employee records
- Viewing employees
- Assigning employees to teams
- Assigning managers through reporting relationships
- Tracking salary and employment type
- Viewing organization structure
- Deactivating employees without deleting historical payroll data

Employee fields include:

- Name
- Role
- Team
- Manager
- Start date
- Salary
- Employment type
- Active status

---

# 2. Leave Management

Employees can submit leave requests which managers can approve or reject.

Implemented leave workflow:

1. Employee submits leave request
2. Manager reviews request
3. Request is approved or rejected
4. Approved leave affects relevant business processes

---

# Leave Business Rules

The system includes safeguards commonly required in real HR systems.

## Annual Leave

Rules:

- Employees start with 21 annual leave days
- Leave cannot exceed the available balance
- Requires at least 7 days notice
- Approved leave reduces the employee leave balance
- Team coverage rules apply

---

## Sick Leave

Rules:

- Sick leave can start immediately or the following day
- No fixed maximum duration is enforced because illness duration varies
- In a production environment, longer absences could require medical documentation

---

## Compassionate Leave

Rules:

- Can start immediately or the following day
- Maximum duration: 5 days

---

## Unpaid Leave

Rules:

- Requires at least 7 days notice
- Maximum duration: 30 days
- Does not reduce annual leave balance
- Approved unpaid leave affects payroll calculations

---

## Team Coverage Protection

To prevent departments from becoming under-staffed:

- Annual Leave and Unpaid Leave approvals check team availability
- The system prevents approval when more than 50% of an active team would be unavailable during the same period

Sick Leave and Compassionate Leave are excluded because they are generally unexpected situations.

---

## Approval Escalation

Pending leave requests are monitored.

Requests pending for more than 14 days are flagged as overdue for attention.

---

# 3. Payroll System

The system generates monthly payroll runs and creates payslips for employees.

Each payslip contains:

- Gross pay
- Unpaid leave days
- Tax deductions
- Housing levy deduction
- Net pay

---

# Payroll Formula

- The payroll calculations use simplified assumptions for demonstration purposes.
- Monthly salary is prorated for employees who join during the payroll month.
- Daily salary is calculated using the actual number of days in that month.
- Gross pay = Monthly salary ÷ Days in month × Eligible working days.
- Unpaid leave deductions are calculated using the same daily salary approach.

## Gross Pay

```
Gross Pay = Employee Monthly Salary
```

---

## Unpaid Leave Deduction

```
Daily Salary = Gross Salary / 30

Unpaid Leave Deduction =
Daily Salary × Approved Unpaid Leave Days
```

---

## Taxable Pay

```
Taxable Pay =
Gross Pay - Unpaid Leave Deduction
```

---

## Tax

```
Tax = 10% of Taxable Pay
```

---

## Housing Levy

```
Housing Levy = 1.5% of Taxable Pay
```

---

## Net Pay

```
Net Pay =
Taxable Pay - Tax - Housing Levy
```

---

# Additional Payroll Handling

The payroll module supports:

- Monthly payroll generation
- Payslip creation for each active employee
- Payroll history preservation
- Unpaid leave salary deductions
- Salary rounding for accurate payslip display

---

# Dashboard

The application includes an HR dashboard showing:

- Pending leave approvals
- Employees currently on leave
- Employee leave balances
- Recent payroll runs

A shared navigation layout allows access to:

- Dashboard
- Employees
- Leave Management
- Organization View
- Payroll
- Payslips

---

# Project Structure

```
hr-payroll-system/

├── models/
│   ├── employees.py
│   ├── leave_request.py
│   ├── payroll_run.py
│   └── payslip.py
│
├── services/
│   └── payroll_service.py
│
├── routes/
│   ├── employee_routes.py
│   ├── leave_routes.py
│   ├── payroll_routes.py
│   └── dashboard_routes.py
│
├── templates/
│
├── database.py
├── app.py
└── requirements.txt
```

---

# Running Locally

## Clone repository

```bash
git clone https://github.com/MwachiraD/hr-payroll-system.git
```

## Create virtual environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---


## Configure database

flask db upgrade
```
## Run application
## Load sample data

python seed.py

```bash
flask run

The application will be available at:


http://127.0.0.1:5000
```
Database Backup

A SQL dump is included:

database_dump.sql

To recreate the database manually:

sqlite3 hr_payroll.db < database_dump.sql
---

# Design Decisions

## Authentication

Authentication was intentionally excluded to prioritize the core HR workflows and business rules within the challenge timeframe.

Manager approval is simulated through the approval interface.

In a production system, authentication and role-based permissions would be added.

---

## Database Choice

SQLite was selected because it is lightweight and suitable for demonstrating the application's functionality.

For production deployment, PostgreSQL would be a suitable replacement.

---

# Future Improvements

Given more time, the following improvements would be considered:

- User authentication and role-based access control
- Email notifications for leave approvals
- Automated payroll reports
- Employee self-service portal
- More advanced tax brackets
- Audit logs for HR actions
- PostgreSQL deployment
- Automated test coverage expansion

---

# Testing

The project includes automated tests covering the core HR and payroll business rules.

Implemented test cases include:

- Unpaid leave salary deduction
- Mid-month employee salary proration
- Payroll calculation with no unpaid leave deductions
- Compassionate leave maximum duration validation
- Annual leave notice period validation
- Team coverage protection during leave approvals
- inactive employee filtering
- Payroll exclusion of inactive employees while preserving historical payroll records

Run tests with:

```bash
pytest