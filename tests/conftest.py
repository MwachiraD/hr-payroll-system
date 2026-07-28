import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

import pytest
from app import app
from database import db


@pytest.fixture
def app_context():

    app.config["TESTING"] = True

    with app.app_context():

        db.drop_all()
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:

        with app.app_context():

            db.drop_all()
            db.create_all()

            yield client

            db.session.remove()
            db.drop_all()