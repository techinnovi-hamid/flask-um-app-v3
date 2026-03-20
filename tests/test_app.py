import pytest
from app.app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_add_user(client):
    response = client.post("/", data={"name": "DevOps"}, follow_redirects=True)
    assert b"User added successfully" in response.data
