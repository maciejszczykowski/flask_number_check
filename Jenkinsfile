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
                    // Install dependencies, including flask_number_check
            bat 'pip install -r requirements.txt'
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
