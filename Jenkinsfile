pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/maciejszczykowski/flask_number_check.git']]])
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
                    // Set PYTHONPATH to include the project directory
                    bat 'set PYTHONPATH= C:\Users\macie\Desktop\Maciek\Dev\Lotto'

                    // Run pytest with the updated Python path
                    bat 'pytest'
                }
            }
        }
    }
}
