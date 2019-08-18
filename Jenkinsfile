node ('kjenk') {
    stage ('Checkout') {
        checkout scm
    }

    stage ('Build') {
        sh 'echo "No build necessary"'
    }

    stage ('Test') {
        sh 'scripts/run_tests.sh'
    }
}

// node ('bbonenil') {
//     stage ('Checkout') {
//         checkout scm
//     }

//     stage ('Build') {
//         sh 'echo "No build necessary"'
//     }

//     stage ('Test') {
//         sh 'scripts/run_tests.sh'
//     }
// }
