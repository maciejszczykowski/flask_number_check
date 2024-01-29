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

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Invoke SonarQube Scanner with user token from Github App settings and token generated in sonarqube
                    // Sonarqube1 is also used in jenkins settings (sonar user token) and sonar project token is used here and in sonar-project.properties file
                    // Token below has no expiry date.
                    withSonarQubeEnv('Sonarqube1') {
                        bat 'sonar-scanner -D"sonar.projectKey=maciejszczykowski_flask_number_check_AYw0yvaGT7BuMOktAZzY" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=sqp_505bb2a1b7b9316152b2a7798f1110af5923c7b4"'
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // Wait for the quality gate status with a maximum timeout of 5 minutes
                timeout(time: 5, unit: 'MINUTES') {
                    script {
                        // Check the quality gate status and abort the pipeline if it's not OK
                        // webhook is needed in Sonarqube to check the qualitygate
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        }
                    }
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Set the working directory to the location of your Dockerfile
                    dir('C:\\Users\\macie\\Desktop\\Maciek\\Dev\\Lotto\\flask_number_check') {
                        // Build and tag the Docker image
                        bat 'docker build -t dockermacdaw/flask-number-check-docker-image:latest .'

                        // Push the Docker image to Docker Hub
                        bat 'docker push dockermacdaw/flask-number-check-docker-image:latest'
                    }
                }
            }
        }
    }
}
    
