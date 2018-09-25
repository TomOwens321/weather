library identifier: 'sharedlibs@master', retriever: modernSCM(
    [$class: 'GitSCMSource',
     remote: 'https://TomOwens321:Yomama@github.com/TomOwens321/sharedlibs.git']
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
