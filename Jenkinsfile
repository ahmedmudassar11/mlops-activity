pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                script {
                    try {
                        // Clone the repository
                        checkout scm
                    } catch (Exception e) {
                        echo "Failed to clone repository: ${e}"
                    }
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    try {
                        // Install the required dependencies
                        bat 'pip install --upgrade pip'
                        bat 'pip install -r requirements.txt'
                    } catch (Exception e) {
                        echo "Failed to install dependencies: ${e}"
                    }
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    try {
                        // Execute the tests
                        bat 'pytest test.py'
                    } catch (Exception e) {
                        echo "Failed to run tests: ${e}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    try {
                        deploy(env.BRANCH_NAME)
                    } catch (Exception e) {
                        echo "Failed to deploy: ${e}"
                    }
                }
            }
        }
    }
}

def deploy(String branchName) {
    if (branchName == 'main') {
        echo "Deploying to production"
       // deploy
    } else {
        echo "Deploying to UAT"
    }
}
