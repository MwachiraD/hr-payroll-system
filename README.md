# HR & Payroll System

## Overview

This project is an internal HR & Payroll system built as part of the Vunoh Global Software & AI Engineering practical assessment.

The application aims to help small and growing organizations manage:

- Employee records
- Leave requests and approvals
- Monthly payroll generation
- In a production system, sick leave could require a medical certificate for absences longer than three consecutive days. This was noted but left out due to the scope of the challenge
- For simplicity, each employee starts with an annual leave balance of 21 days. This value can easily be made configurable in a production system."

The focus of this project is implementing realistic business logic rather than simple CRUD operations.

- Authentication was intentionally omitted to prioritize implementing the core HR workflows. Manager approval is simulated through the approval interface, allowing the business logic to be evaluated independently of user authentication.
 
## Technology Stack

- Backend: Flask
- Frontend: HTML, CSS, JavaScript
- Database: SQLite

## Current Status

Project initialized.

Implementation will be developed incrementally with regular commits.

## Planned Features

### Employee Records
- Employee profiles
- Reporting structure
- Employee deactivation

### Leave Management
- Leave requests
- Manager approvals
- Leave balance validation
- Team coverage checks

### Payroll
- Monthly payslips
- Tax calculations
- Social security deductions
- Pro-rated salary calculations

## Testing

Unit tests will cover payroll calculations and leave business rules.

## Future Improvements

These will be documented as development progresses.