#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */

pipeline {
  agent any 
    options{
       timestamps()
       buildDiscarder(logRotator(numToKeepStr: '30'))
       /*timeout(time: 30, unit: 'SECONDS')*/
    }
    environment {
        VIRTUAL_ENV = "${env.WORKSPACE}/venv"
}
    stages {
        stage ('Start') {
      steps {
        slackSend (color: '#FFFF00', message: "STARTED...!  : Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
         }
    } /*
        stage ('Install Requirements') {
            steps {
                sh """
                    echo ${SHELL}
                    [ -d venv ] && rm -rf venv
                    #virtualenv --python=python2.7 venv
                    virtualenv venv
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
                echo "RESULT: ${currentBuild.result}"
                echo "${env.WORKSPACE}"
            }
     }  */
    stage('Checkout SCM') {
        steps{
             checkout scm
            }
       }
    stage('numpy pandas') {
        steps{
              sh '''
                    python numpy_pandas_ex.py
                    sudo chmod 777 /var/lib/jenkins/workspace/jenkins-python-test_master@tmp/gen_output.pkl
                 '''
            }
       }
    stage('generator fun') {
        steps{
              sh '''
                    python pythonfiles/generators_fun_ex.py
                 '''
            }
       }
    stage('build_id url') {
        steps{
              echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
              echo "Running ${env.BUILD_ID} on ${env.BUILD_URL}"
            }
       }    /*
    stage('Download') {
            steps {
                sh '''
                python numpy_pandas_ex.py > /var/lib/jenkins/workspace/jenkins-python-test_master@tmp/gen_output.txt
                  '''
            }
        }  */
} 
  post {
        always {
            echo 'Build Started...!'
           /* archiveArtifacts artifacts: '/var/lib/jenkins/workspace/jenkins-python-test_master@tmp/gen_output.txt', onlyIfSuccessful: true */
            deleteDir() /* clean up our workspace */
        }
        success {
            echo 'Succeeeded...!'
           /* slackSend (color: '#00FF00', message: "SUCCESSFUL...! : Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})") */
        }
        unstable {
            echo 'Unstable...!'
        }
        failure {
            echo 'Failed...!'
           /* slackSend (color: '#FF0000', message: "FAILED...! : Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})") */
        }
        changed {
            echo 'Things were different before...!'
        }
    }
}
