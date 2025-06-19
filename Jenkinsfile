pipeline {
    agent any

    environment {
        ALLURE_RESULTS_DIR = 'allure-results'
        ALLURE_REPORT_DIR = 'allure-report'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/username/flask-area-calculator.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("flask-area-calculator")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    dockerImage.inside {
                        // Ensure the allure results directory exists
                        sh "mkdir -p ${env.ALLURE_RESULTS_DIR}"

                        // Run tests with allure reporting
                        sh "pytest --alluredir=${env.ALLURE_RESULTS_DIR} test_app.py"
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                // Generate the Allure report
                allure commandline: true, installation: 'allure', results: [[path: "${env.ALLURE_RESULTS_DIR}"]]
            }
        }

        stage('Archive Allure Report') {
            steps {
                // Archive the Allure report directory
                archiveArtifacts artifacts: "${env.ALLURE_RESULTS_DIR}/**", allowEmptyArchive: true
            }
        }

        stage('Upload to Artifactory') {
            steps {
                // Define Artifactory server (assuming configuration is already done in Manage Jenkins)
                script {
                    def server = Artifactory.server('Artifactory-Server-ID')
                    def uploadSpec = """{
                        "files": [
                            {
                                "pattern": "${env.ALLURE_RESULTS_DIR}/*.*",
                                "target": "allure-reports/"
                            }
                        ]
                    }"""
                    // Uploading to Artifactory using the defined spec
                    server.upload(uploadSpec)
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker stop flask-area || true && docker rm flask-area || true'
                    sh 'docker run -d -p 5000:5000 --name flask-area flask-area-calculator'
                }
            }
        }
    }
}
