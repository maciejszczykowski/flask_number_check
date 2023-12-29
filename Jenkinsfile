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
                    // Sonarqube1 is also connected to jenkins settings
                    // Token below has no expiry date
                    withSonarQubeEnv('Sonarqube1') {
                        bat 'sonar-scanner -D"sonar.projectKey=maciejszczykowski_flask_number_check_AYw0yvaGT7BuMOktAZzY" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.login=ssqu_617281ed857d09b665beed83a81c0b41dae23642"'
                    }
                }
            }
        }

        stage('Quality Gate Check') {
            steps {
                script {
                    // Retrieve SonarQube Quality Gate status
                    def qualityGateStatus = sh(script: "curl -s -u admin:admin http://localhost:9000/api/qualitygates/project_status?projectKey=maciejszczykowski_flask_number_check_AYw0yvaGT7BuMOktAZzY | jq -r .status", returnStatus: true).trim()
                    
                    // Fail the pipeline if Quality Gate status is not "OK"
                    if (qualityGateStatus != "OK") {
                        error "SonarQube Quality Gate check failed."
                    }
                }
            }
        }
    }
}
