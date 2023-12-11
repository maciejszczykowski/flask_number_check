About: Project to train Dev and CI/CD
How it works: After entering a number on frontend, python backend is asking DB if entered number appears there or not and gives back the information

Stack and tools: VSC/Python/Flask/Html/Css/Postrgrsql/Git/Pytest/Selenium/Webdriver/Jenkins/Groovy/Sonarqube/SonarScanner/Ngrok/Webhooks/

To run project locally on VSC: python app.py

To run unit tests (Pytest) locally on VSC app must be first started: pytest 

To run virtual environment: .\venv\Scripts\Activate
After finishing: deactivate

Ngrok URL domain for Jenkins:  https://beetle-prepared-rodent.ngrok-free.app
To start ngrok from cmd: 
cd C:\Program Files\Ngrok-v3-stable-windows
ngrok http 8080 --domain beetle-prepared-rodent.ngrok-free.app

Jenkins locally runs on: http://localhost:8080/
Sonarqube locally runs on:  http://localhost:9000/
Ngrok: https://dashboard.ngrok.com/get-started/your-authtoken

Sequence: 
1. Start Sonarqube
2. Start Ngrok
3. Commit to main branch. Jenkins runs automaticaly 


Version 01 beta not automated

To run tests (Pytest): $env:PYTHONPATH = "C:\Users\macie\Desktop\Maciek\Dev\Lotto" pytest

To run sonarqube locally: Sonarqube - Turn on sonarqube locally, run cmd from project location cd C:\Users\macie\Desktop\Maciek\Dev\Lotto\flask_number_check
sonar-scanner.bat -D"sonar.projectKey=maciejszczykowski_flask_number_check_AYw0yvaGT7BuMOktAZzY" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_a4591d465b5af2ed385f1f478002759c69f19990"

wszytkie dependencies na virtualnym .venv musza byc zainstalowane
pytest, python, pluggy, selenium, flask
aby sprawdzic: pip show selenium
aby zainstalowac: pip install selenium
__init__.py dodac plik aby testy uruchamiac bez $env:...
