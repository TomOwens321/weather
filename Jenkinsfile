library identifier: 'sharedlibs@master', retriever: modernSCM(
    [$class: 'GitSCMSource',
     remote: 'https://TomOwens321@github.com/TomOwens321/sharedlibs.git']
)

def retryCount = 3

pipeline {
    agent { node 'jslave' } 
    stages {
        stage ('Checkout') {
            checkoutWithRetries(retryCount) 
        }

        stage ('Build') {
            sh 'echo "Lets try out a shared function call."'
            sayHello('Tom')
            vars()
        }

        stage ('Test') {
            sh 'scripts/run_tests.sh'
        }
    }
}

def vars() {
    sh 'env'
}
