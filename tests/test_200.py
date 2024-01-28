import pytest
from flask_number_check.app import app

def test_run_app():
    # This test checks if the application runs successfully without errors
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

if __name__ == '__main__':
    pytest.main()
