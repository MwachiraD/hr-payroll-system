from flask import Flask, render_template

from config import Config
from database import db, migrate
from models.employees import Employee
from routes.employee_routes import employee_bp


app = Flask(__name__)
app.config.from_object(Config)

migrate.init_app(app, db)
app.register_blueprint(employee_bp)

db.init_app(app)
migrate.init_app(app, db)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)