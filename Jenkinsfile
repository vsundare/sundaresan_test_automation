pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vsundare/sundaresan_test_automation.git'
            }
        }
        stage('Build and Run Application') {
            steps {
                sh 'docker-compose up --build -d app'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh 'docker-compose run test'
                    } catch (Exception e) {
                        // Log the error and allow the flow to continue for reporting purposes
                        echo "Tests failed: ${e}"
                    }
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                // Publish Allure test report using Allure Jenkins plugin
                allure([
                    results: [[path: './allure-results']]
                ])
            }
        }
        stage('Clean Up') {
            steps {
                sh 'docker-compose down --volumes'
            }
        }
        stage('Build Docker Image for Production') {
            when { branch 'main' }
            steps {
                script {
                    docker.build("myrepo/myapp:latest", "-f Dockerfile.app .")
                }
            }
        }
        stage('Push Docker Image') {
            when { branch 'main' }
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        sh 'docker push myrepo/myapp:latest'
                    }
                }
            }
        }
        stage('Deploy to Production') {
            when { branch 'main' }
            steps {
                script {
                    // SSH into the production server to deploy the new Docker image
                    sh '''
                      ssh -o StrictHostKeyChecking=no user@production-server << EOF
                        docker pull myrepo/myapp:latest
                        docker stop myapp || true
                        docker rm myapp || true
                        docker run -d --name myapp -p 80:5000 myrepo/myapp:latest
                      EOF
                    '''
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/allure-results/*', allowEmptyArchive: true
            cleanWs()
        }
    }
}
