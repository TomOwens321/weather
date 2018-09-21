@Library('sharedlibs') _

node ('jslave') {
    stage ('Checkout') {
        checkoutWithRetries(3) 
    }

    stage ('Build') {
        sh 'echo "No build necessary"'
        vars()
    }

    stage ('Test') {
        sh 'scripts/run_tests.sh'
    }
}

def checkoutWithRetries(retryCount) {
    if (binding.hasVariable('busy')) {
        echo 'busy found '
        busy = true
    } else {
        def busy = true
        echo 'created busy'
    }
    while (retryCount>0) {
        try {
            if (retryCount == 3) {
                throw new Exception('Weeeee')
            }
            checkout scm
            retryCount = 0
        }
        catch (Exception e) {
            msg = e.getMessage()
            if ((retryCount % 3) == 0) {
                echo "Checkout scm failed due to ${msg}.  Retrying"
            }
            retryCount--
        }
    }
    busy = false
}

def vars() {
    sh 'env'
}
