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
- approved_by
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