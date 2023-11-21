pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                script {
                    if (isUnix()) {
                        // Update this path accordingly for Unix systems
                        sh 'export PYTHONPATH=/C/Users/macie/Desktop/Maciek/Dev/Lotto:$PYTHONPATH'
                    } else {
                        // Update this path accordingly for Windows systems
                        bat '$env:PYTHONPATH="C:\\Users\\macie\\Desktop\\Maciek\\Dev\\Lotto";' + $env:PYTHONPATH
                    }
                    // Add more commands for other dependencies as needed
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
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
                script {
                    bat 'start python app.py'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pytest'
                    } else {
                        bat '$env:PYTHONPATH = "C:\Users\macie\Desktop\Maciek\Dev\Lotto"
pytest'
                    }
                }
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
