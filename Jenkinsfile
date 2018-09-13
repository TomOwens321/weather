node ('jslave') {
    stage ('Checkout') {
        checkoutWithRetries(3) 
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
            if (retryCount == 3) {
                throw new Exception('Weeeee')
            }
            checkout scm
            retryCount = 0
        }
        catch (all) {
            retryCount--
            echo "Checkout scm failed... Retrying"
        }
    }
}
