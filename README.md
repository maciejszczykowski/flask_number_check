ABOUT: Project to train Dev and CI/CD
How it works: After entering a number on frontend, python backend is asking DB if entered number appears there or not and gives back the information

Stack and tools: VSC/Python/Flask/Html/Css/Postrgrsql/Git/Pytest/JavaJDK-17/Selenium/Webdriver/Jenkins/Groovy/Sonarqube/SonarScanner/Ngrok/Webhooks/Docker

To run project locally on VSC: python app.py
PS C:\Users\macie\Desktop\Maciek\Dev\Lotto\flask_number_check> python app.py
To run unit tests (Pytest) locally on VSC app must be first started: pytest 

To run virtual environment: .\venv\Scripts\Activate
After finishing: deactivate

SEQUENCE: 

1. Start Sonarqube from pulpit
Sonarqube locally runs on:  http://localhost:9000/

2. Start Ngrok from cmd 
cd C:\Program Files\Ngrok-v3-stable-windows
ngrok http 8080 --domain beetle-prepared-rodent.ngrok-free.app

Jenkins runs online on: https://beetle-prepared-rodent.ngrok-free.app
Jenkins runs on premise on: http://localhost:8080/

3. Start Docker Desktop from pulpit

4. Commit and push to main branch. Jenkins runs automaticaly. 



---------------------------------------------------------------------------------------------------------------------------------------------------------------

VM: Virtualbox/Ubuntu

------------------------------------------------------------------------------------------------------------------------------------------------
Docker
