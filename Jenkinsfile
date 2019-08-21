podTemplate(yaml: """
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: python
spec:
  containers:
  - name: python
    image: python
    command:
    - cat
    tty: true
"""
)
node ('POD_LABEL') {
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
