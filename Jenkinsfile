pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "prediction-service:${env.BUILD_NUMBER}"
        K8S_DEPLOYMENT = 'prediction_service-deployment.yaml'
        K8S_SERVICE = 'prediction_service-service.yaml'
        REGISTRY_CREDENTIALS_ID = 'dockerhub-credentials'
        KUBE_CONFIG = credentials('kube-config')
    }

    stages {
        stage('Validate Environment') {
            steps {
                script {
                    sh 'docker --version'
                    sh 'kubectl version --client'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE ./prediction_service'
                }
            }
        }

        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "$REGISTRY_CREDENTIALS_ID") {
                        sh 'docker push $DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig([credentialsId: 'kube-config']) {
                        sh 'kubectl apply -f ./prediction_service/k8s/$K8S_DEPLOYMENT'
                        sh 'kubectl apply -f ./prediction_service/k8s/$K8S_SERVICE'
                    }
                }
            }
        }
    }

    post {
        success {
            mail to: 'yashraj8996@gmail.com',
                 subject: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build was successful. Check it out at ${env.BUILD_URL}"
        }
        failure {
            mail to: 'yashraj8996@gmail.com',
                 subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build failed. Check it out at ${env.BUILD_URL}"
        }
        always {
            cleanWs()
        }
    }
}
