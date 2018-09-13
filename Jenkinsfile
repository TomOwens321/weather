node ('jslave') {
    stage ('Checkout') {
        checkoutWithRetries(2) 
    }

    stage ('Build') {
        sh 'echo "No build necessary"'
    }

    stage ('Test') {
        sh 'scripts/run_tests.sh'
    }
}

def checkoutWithRetries(retryCount) {
    while (retryCount>0) {
        try {
            checkout scm
        }
        catch {
            retryCount--
            echo "Checkout scm failed... Retrying"
        }
}
