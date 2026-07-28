import sqlite3

conn = sqlite3.connect("hr_payroll.db")

with open("database_dump.sql", "w", encoding="utf-8") as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")

conn.close()

print("Database dump created")