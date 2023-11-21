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

        stage('Run Application') {
            steps {
                script {
                    // Run the Flask application
                    bat 'python app.py'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Set PYTHONPATH to include the project directory
                    bat '$env:PYTHONPATH = "${WORKSPACE}"'

                    // Run pytest unit tests
                    bat 'pytest tests'
                }
            }
        }
    }
}
