pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                script {
                    echo 'Running on Windows OS'
                    bat 'python --version'
                    bat 'pip --version'
                    bat 'flask --version'
                    bat 'pytest --version'
                    // Add more commands for other dependencies as needed
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
                    bat 'pip install pytest'
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
        dir('C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Lottery pipeline') {
            script {
                    bat '\'$env:PYTHONPATH="C:\\Users\\macie\\Desktop\\Maciek\\Dev\\Lotto"\' pytest'
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
