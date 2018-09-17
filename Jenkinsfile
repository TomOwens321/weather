node ('jslave') {
    stage ('Checkout') {
        def busy = true
        checkoutWithRetries(3) 
    }

    stage ('Build') {
        sh 'echo "No build necessary"'
    }

    stage ('Test') {
        sh 'scripts/run_tests.sh'
    }
}

def checkoutWithRetries(retryCount, busy = true) {
    while (busy) {
        echo 'I am busy'
        sleep(2)
        busy = false
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
            retryCount--
            msg = e.getMessage()
            echo "Checkout scm failed due to ${msg}.  Retrying"
        }
    }
}
