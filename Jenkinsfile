pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/maciejszczykowski/flask_number_check.git']]])
            }
        }

        stage('Build') {
            steps {
                script {
                    // Install dependencies
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run pytest unit tests
                    bat 'pytest Lotto/flask_number_check/tests/test_app.py'
                }
            }
        }
    }
}
