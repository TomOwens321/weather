library identifier: 'sharedlibs@master', retriever: modernSCM(
    [$class: 'GitSCMSource',
     remote: 'https://TomOwens321@github.com/TomOwens321/sharedlibs.git']
)

def retryCount = 3

pipeline {
    agent { node 'jslave' } 
    stages {
        stage ('Checkout') {
            steps {
                checkoutWithRetries(retryCount) 
            }
        }

        stage ('Build') {
            steps {
                sh 'echo "Lets try out a shared function call."'
                sayHello('Tom')
                vars()
             }
        }

        stage ('Test') {
            steps { 
                sh 'scripts/run_tests.sh'
            }
        }
    }
}

def vars() {
    sh 'env'
}
