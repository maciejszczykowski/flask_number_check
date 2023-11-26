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
                    // Change directory to the root of the project
                    bat "cd ${WORKSPACE}/flask_number_check"  // Update the path accordingly

                    // Activate the virtual environment
                    bat 'venv\\Scripts\\activate'
                    
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
                    // Install dependencies (if needed)
                    // bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Change directory to the root of the project
                    bat "cd ${WORKSPACE}/flask_number_check"  // Update the path accordingly

                    // Run tests
                    bat 'pytest'
                }
            }
        }
    }
}
