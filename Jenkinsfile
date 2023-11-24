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
                    bat ' pip install pytest'
                }
            }
        }

     

        stage('Test') {
            steps {
                script {
            
                    bat 'pytest'
                }
            }
        }
    }
}
