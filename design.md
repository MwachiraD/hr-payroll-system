# Database Design

## Employee

- id
- name
- role
- team
- manager_id
- salary
- employment_type
- start_date
- is_active

## LeaveRequest

- id
- employee_id
- start_date
- end_date
- leave_type
- reason
- status
- approved_by_manager_id
- approved_at
- created_at

## Business Rules 

- Employee cannot request leave in the past 
- End date of leave cannot be before Start date
- Only pending requests can be approved
- Only the employee's manager can approve leave 
- Leave balance cannot go beyond zero 
- Employee cannot have an overlapping leave , cannot request leave twice in the same period
- Not more than Half of the team should be on leave simultaneously to avoid understaffing
- Only approved leave affects payroll
- Leave requests older than 14 days without a decision are flagged as overdue on the dashboard.
- Annual Leave and Unpaid Leave require at least 7 days' notice to allow workforce planning. Sick Leave and Compassionate Leave may begin immediately because they represent unplanned events.
- An employee cannot request more Annual Leave than their remaining leave balance. which I have set to a maximum 21 days an year
- Sick and compassionate leave may start immediately or the following day.
- Approved annual leave reduces employee leave balance.
- Rejected and pending leave requests do not affect payroll.
- Pending leave requests older than 14 days are flagged as overdue.
- Team capacity checks apply only to planned leave types.
- Annual leave cannot exceed the employee's available leave balance.
- Sick leave has no fixed maximum duration; extended sick leave may require medical documentation.
- Compassionate leave is limited to 5 days per request.
- Unpaid leave is limited to 30 days per request.

## PayrollRun

- id
- month
- year
- generated_at
- generated_by
- status

## Payslip

- id
- payroll_run_id
- employee_id
- gross_pay
- unpaid_leave_days
- tax
- housing_levy
- net_pay
- generated_at

### Edge Cases Handled

- Duplicate payroll generation is prevented.
- Mid-month employee joining is prorated automatically.
- Payroll only deducts unpaid leave that belongs to the selected payroll month.