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
     }

    stage ('Start') {
      steps {
        slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
         }
    } 
    
    stage('Checkout SCM') {
        steps{
             checkout scm
            }
       }
    stage('numpy_pandas') {
        steps{
              sh '''
                    python numpy_pandas_ex.py
                 '''
            }
       }
    stage('generator_fun') {
        steps{
              sh '''
                    python pythonfiles/generators_fun_ex.py
                 '''
            }
       }      
}
  post {
        always {
            echo 'Started...!'
            deleteDir() /* clean up our workspace */
        }
        success {
            echo 'Succeeeded...!'
            slackSend (color: '#00FF00', message: "SUCCESSFUL...: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        unstable {
            echo 'Unstable...!'
        }
        failure {
            echo 'Failed...!'
            slackSend (color: '#FF0000', message: "FAILED...: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        changed {
            echo 'Things were different before...!'
        }
    }
}