@Library('sharedlibs') _

node ('jslave') {
    stage ('Checkout') {
        checkoutWithRetries(3) 
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
