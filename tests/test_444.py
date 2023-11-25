# Unit test to check if when posted 44444444 to the DB it receives success.

import pytest
from flask_number_check.app import app, check_number_in_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_check_number_in_db(client):
    # Assuming you have a test database set up for testing purposes
    # Ensure this test database is configured in your app or modify the test accordingly
    result = check_number_in_db('44444444')
    assert result == "Congratulations! You win!"
