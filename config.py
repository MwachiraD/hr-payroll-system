import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "9c64dfe912d89e3b0e6d3d2b1cbba3cce98d2b42efb4d8b95d7f2d6d31d3d73a"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'hr_payroll.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False