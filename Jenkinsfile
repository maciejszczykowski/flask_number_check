pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/maciejszczykowski/flask_number_check.git']]])
            }
        }

        stage('Run App and Tests') {
            parallel {
                stage('Run App') {
                    steps {
                        script {
                            // Set the working directory to the location of your app
                            dir('C:\\Users\\macie\\Desktop\\Maciek\\Dev\\Lotto\\flask_number_check') {
                                // Print Python path for debugging
                                bat 'python -c "import sys; print(sys.path)"'

                                // Install dependencies
                                bat 'pip install -r requirements.txt'

                                // Run the Flask app in the background
                                bat 'start python app.py'
                            }
                        }
                    }
                }

                stage('Run Tests') {
                    steps {
                        script {
                            // Set the working directory to the location of your tests
                            dir('C:\\Users\\macie\\Desktop\\Maciek\\Dev\\Lotto\\flask_number_check') {
                                // Install dependencies
                                bat 'pip install -r requirements.txt'

                                // Run the tests.
                                bat 'pytest'
                            }
                        }
                    }
                }
            }
        }
    }
}
