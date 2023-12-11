About: Project to train python/flask/html/css/postgresqlDB and CI/CD
How it works: After entering a number on html frontend, python backend is asking DB if provided number appears there or not and gives back the information to frontend.

To run project: python app.py

Stack: VSC/Python/Flask/Html/Css/Postrgrsql/Git/Pytest/Selenium/Webdriver/Jenkins/Groovy/Sonarqube/SonarScanner/Ngrok/Webhooks/

To run unit tests (Pytest): $env:PYTHONPATH = "C:\Users\macie\Desktop\Maciek\Dev\Lotto"
pytest

To run virtual environment use: .\venv\Scripts\Activate
After finishing: deactivate

27.11.2023 - Pytest dziala bez $env, jenkins dziala front+back, wlacza aplikacje w tle. Zey puscic testy w VSC trzeba najpierw odpalic aplikacje.
06.12.2023 - Sonarqube - Turn on sonarqube locally, run cmd from project location cd C:\Users\macie\Desktop\Maciek\Dev\Lotto\flask_number_check
sonar-scanner.bat -D"sonar.projectKey=maciejszczykowski_flask_number_check_AYw0yvaGT7BuMOktAZzY" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_a4591d465b5af2ed385f1f478002759c69f19990"

Ngrok URL domain for Jenkins:  https://beetle-prepared-rodent.ngrok-free.app
To start ngrok from cmd: 
cd C:\Program Files\Ngrok-v3-stable-windows: 
ngrok http 8080 --domain beetle-prepared-rodent.ngrok-free.app

wszytkie dependencies na virtualnym .venv musza byc
pytest, python, pluggy, selenium, flask
aby sprawdzic: pip show selenium
aby zainstalowac: pip install selenium
__init__.py dodac plik aby testy uruchamiac bez $env:...


Sequence: 
1. Start Sonarqube
2. Start Ngrok
