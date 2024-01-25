Version 01 beta not automated

To run tests (Pytest): $env:PYTHONPATH = "C:\Users\macie\Desktop\Maciek\Dev\Lotto" pytest

To run sonarqube locally: Sonarqube - Turn on sonarqube locally, run cmd from project location cd C:\Users\macie\Desktop\Maciek\Dev\Lotto\flask_number_check
sonar-scanner.bat -D"sonar.projectKey=maciejszczykowski_flask_number_check_AYw0yvaGT7BuMOktAZzY" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=squ_617281ed857d09b665beed83a81c0b41dae23642"

wszytkie dependencies na virtualnym .venv musza byc zainstalowane
pytest, python, pluggy, selenium, flask
aby sprawdzic: pip show selenium
aby zainstalowac: pip install selenium
__init__.py dodac plik aby testy uruchamiac bez $env:...

Qualitygate step: need to add webhook in sonarqube.

