node ('jslave') {
    stage ('Checkout') {
        checkout scm
    }

    stage ('Build') {
        sh 'echo "No build necessary"'
    }

    stage ('Test') {
        sh 'for test in `ls */test*`; do python3 ${test}; done'
    }
}
