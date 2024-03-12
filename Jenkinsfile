pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                // Clone the repository
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    checkout scm
                }
            }
        }

        stage('Install dependencies') {
            steps {
                // Install the required dependencies
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat 'pip install --upgrade pip'
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run tests') {
            steps {
                // Execute the tests
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat 'pytest test.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                        deploy(env.BRANCH_NAME)
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
