pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/maciejszczykowski/flask_number_check.git']]])
            }
        }

        stage('Test Setup') {
            steps {
                script {
                    // Add debugging information
                    bat 'pip show -v flask_number_check'
                    bat 'echo %PATH%'
                }
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

        stage('Run Tests') {
            steps {
                script {
                    // Run the tests
                    bat 'pytest'
                }
            }
        }
    }
}
