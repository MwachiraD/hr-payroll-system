import sqlite3


connection = sqlite3.connect("hr_payroll.db")

with open("database_dump.sql", "w") as file:
    for line in connection.iterdump():
        file.write(f"{line}\n")

connection.close()

print("Database dump created successfully.")