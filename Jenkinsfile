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
                    echo 'Current Directory: ' + pwd()
                    echo 'Python Path: ' + sh(script: 'echo $PYTHONPATH', returnStdout: true).trim()
                    sh 'ls -R' // Print directory structure for debugging
                    sh 'pytest'
                }
            }
        }
    }
