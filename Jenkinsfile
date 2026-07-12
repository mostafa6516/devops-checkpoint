pipeline {
    agent any

    triggers {
        // Requires a GitHub webhook pointing at: http://<jenkins-host>:8080/github-webhook/
        githubPush()
    }

    environment {
        IMAGE_NAME     = 'devops-checkpoint-app'
        IMAGE_TAG      = "${env.BUILD_NUMBER}"
        CONTAINER_NAME = 'devops-checkpoint-app'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    args '-v $WORKSPACE:/app -w /app'
                    reuseNode true
                }
            }
            steps {
                // No requirements.txt / external deps needed for this script.
                // Compile it as a lightweight smoke test that it's valid Python.
                sh 'python3 -m py_compile file.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d -i --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success {
            echo "Build ${env.BUILD_NUMBER} deployed successfully."
        }
        failure {
            echo "Build ${env.BUILD_NUMBER} failed."
        }
    }
}
