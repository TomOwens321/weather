library identifier: 'sharedlibs@master', retriever: modernSCM(
    [$class: 'GitSCMSource',
     remote: 'git@github.com:TomOwens321/sharedlibs',
     credentialsId: 'me_at_github']
)

def retryCount = 3

node ('jslave') {
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

def vars() {
    sh 'env'
}
