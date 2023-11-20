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
stage('Install Dependencies') {
    steps {
        script {
            if (isUnix()) {
                sh 'pip install -r requirements.txt'
            } else {
                bat 'pip install -r requirements.txt'
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
        script {
            if (isUnix()) {
                sh 'nohup python app.py &'
            } else {
                bat 'start python app.py'
            }
        }
    }
}


