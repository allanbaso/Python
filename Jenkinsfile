pipeline {
    agent { 
        node {
            label 'docker-agent-py'
            }
      }
    triggers {
        pollSCM '*/1 * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                echo "doing building stuff.."
                sh '''
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing testing stuff.."
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivering stuff.."
                '''
            }
        }
    }
}
