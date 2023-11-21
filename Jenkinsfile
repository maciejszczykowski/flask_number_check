pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/maciejszczykowski/flask_number_check.git'
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
                    // Run tests
                    bat 'pytest Lotto/flask_number_check/tests'
                }
            }
        }
    }
}
