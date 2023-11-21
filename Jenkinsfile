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

        stage('Debug') {
            steps {
                script {
                    // Print directory structure for debugging
                    bat 'dir Lotto\\flask_number_check\\tests'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run pytest unit tests
                    bat 'pytest Lotto\\flask_number_check\\tests\\test_app.py'
                }
            }
        }
    }
}
