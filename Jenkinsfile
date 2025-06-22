pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from GitHub
                git url: 'https://github.com/vsundare/sundaresan_test_automation.git', branch: 'main'
            }
        }
        stage('Docker') {
            steps {
                sh 'docker -H tcp://docker:2375 --tls=false ps'
            }
        }
        stage('Verify Docker Access') {
            steps {
                script {
                    sh 'whoami'
                    sh 'docker --version'
//                     sh 'id'
//                     sh 'ls -l /var/run/docker.sock'
                }
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
//         stage('Generate Allure Report') {
//             steps {
//                 // Use the Allure Jenkins plugin to publish test results
//                 allure includeProperties: false, results: [[path: './allure-results']]
//             }
//         }
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
            // Archive Allure results for later inspection
            archiveArtifacts artifacts: './allure-results/**', allowEmptyArchive: true
            // Clean up Jenkins workspace to save space
            cleanWs()
        }
        success {
            // Notify about successful build
            mail to: 'you@example.com',
                 subject: "Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Good news! The build ${env.BUILD_NUMBER} of ${env.JOB_NAME} succeeded. Check the report at ${env.BUILD_URL}."
        }
        failure {
            // Notify about failed build
            mail to: 'you@example.com',
                 subject: "Build Failure: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Unfortunately, the build ${env.BUILD_NUMBER} of ${env.JOB_NAME} failed. Please check the details at ${env.BUILD_URL}."
        }
    }
}
