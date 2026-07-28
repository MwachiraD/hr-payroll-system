BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO "alembic_version" VALUES('61dc0dfbed48');
CREATE TABLE employees (
	id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	role VARCHAR(100) NOT NULL, 
	team VARCHAR(100) NOT NULL, 
	salary FLOAT NOT NULL, 
	employment_type VARCHAR(50) NOT NULL, 
	start_date DATE NOT NULL, 
	manager_id INTEGER, 
	is_active BOOLEAN, leave_balance INTEGER DEFAULT '21' NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(manager_id) REFERENCES employees (id)
);
INSERT INTO "employees" VALUES(1,'Dennis','SALES Manager','SALES',80000.0,'Full Time','2026-07-28',NULL,1,21);
INSERT INTO "employees" VALUES(2,'Wachira','IT Manager','IT',80000.0,'Contract','2026-07-28',1,1,21);
INSERT INTO "employees" VALUES(3,'Mwangi','Developer','Engineering',90000.0,'Contract','2026-08-15',2,1,21);
INSERT INTO "employees" VALUES(4,'Wendy','Developer','Engineering',120000.0,'Contract','2026-07-16',2,1,21);
INSERT INTO "employees" VALUES(5,'Wangari','Developer','Engineering',140000.0,'Contract','2026-07-28',2,1,21);
INSERT INTO "employees" VALUES(6,'Tabby','Sales','Sales',70000.0,'Full Time','2026-07-28',1,0,21);
CREATE TABLE leave_requests (
	id INTEGER NOT NULL, 
	employee_id INTEGER NOT NULL, 
	start_date DATE NOT NULL, 
	end_date DATE NOT NULL, 
	leave_type VARCHAR(50) NOT NULL, 
	status VARCHAR(20) NOT NULL, 
	reason TEXT, 
	approved_by_manager_id INTEGER, 
	approved_at DATETIME, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(approved_by_manager_id) REFERENCES employees (id), 
	FOREIGN KEY(employee_id) REFERENCES employees (id)
);
INSERT INTO "leave_requests" VALUES(1,4,'2026-08-09','2026-08-14','Annual Leave','Pending','Personal leave',NULL,NULL,'2026-07-28 22:13:10.533876');
CREATE TABLE payroll_runs (
	id INTEGER NOT NULL, 
	month INTEGER NOT NULL, 
	year INTEGER NOT NULL, 
	generated_at DATETIME, 
	status VARCHAR(20), 
	PRIMARY KEY (id)
);
INSERT INTO "payroll_runs" VALUES(1,7,2026,'2026-07-29 01:13:10.540089','Completed');
CREATE TABLE payslips (
	id INTEGER NOT NULL, 
	payroll_run_id INTEGER NOT NULL, 
	employee_id INTEGER NOT NULL, 
	gross_pay FLOAT NOT NULL, 
	unpaid_leave_days INTEGER, 
	tax FLOAT, 
	housing_levy FLOAT, 
	net_pay FLOAT NOT NULL, 
	generated_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(employee_id) REFERENCES employees (id), 
	FOREIGN KEY(payroll_run_id) REFERENCES payroll_runs (id)
);
COMMIT;
