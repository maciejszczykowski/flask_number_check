# Test to check the DB Connection. Function sends a GET request to URL and asserts that the response is code 200.

import pytest
from flask_number_check.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_db_connection(client):
    response = client.get('/')
    assert response.status_code == 200
