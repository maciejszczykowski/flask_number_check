pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'echo "Running on Unix-like OS"'
                        sh 'echo "Python Version: $(python --version)"'
                        sh 'echo "Pip Version: $(pip --version)"'
                        sh 'echo "Flask Version: $(flask --version)"'
                        // Add more commands for other dependencies as needed
                    } else {
                        echo 'Running on Windows OS'
                        bat 'python --version'
                        bat 'pip --version'
                        bat 'flask --version'
                        // Add more commands for other dependencies as needed
                    }
                }
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if the build and tests are successful'
            // You can trigger deployment or other actions here
        }
    }
}
