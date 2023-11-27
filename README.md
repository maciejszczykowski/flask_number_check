About: Project to train python/flask/html/css/postgresqlDB and CI/CD
How it works: After entering a number on html frontend, python backend is asking DB if provided number appears there or not and gives back the information to frontend.

To run project: python app.py

Folders:
Lotto/flask_number_check/static/css/style.css
Lotto/flask_number_check/templates/index.html
Lotto/flask_number_check/app.py
Lotto/flask_number_check/tests/test_444 and test_app.py and test_frontend.py
Lotto/flask_number_check/drivers/

VSC/Python/Flask/Html/Css/Postrgrsql/Git/Pytest/Selenium/Webdriver/Jenkins/Groovy/

To run unit tests (Pytest): $env:PYTHONPATH = "C:\Users\macie\Desktop\Maciek\Dev\Lotto"
pytest
.\venv\Scripts\Activate
To run virtual environment use: 
After finishing: deactivate

27.11.2023 - Pytest dziala bez $env, jenkins dziala front+back, wlacza aplikacje w tle. Zey puscic testy w VSC trzeba najpierw odpalic aplikacje

wszytkie dependencies na virtualnym .venv musza byc
pytest, python, pluggy, selenium, flask
aby sprawdzic: pip show selenium
aby zainstalowac: pip install selenium
__init__.py dodac plik aby testy uruchamiac bez $env:...