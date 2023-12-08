// // def REPOSITORY_URI = "pallavy57/wiserly-inventory-planner"

// pipeline{
//     agent {
//     label 'docker' 
//   }
//    environment{
//       registry = "pallavy57/wiserly-inventory-planner"
//       registryCredential = 'gcr:linen-waters-366217'
//       dockerImage = ''
//    }
//    stages{
//     stage('Get latest version of code') {
//          steps {
//             checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'pallavy57', url: 'https://github.com/pallavy57/wiserly_app.git']]])
//             sh "ls -lart ./*"
//         }
//     } 
//     stage('Docker Build') {
//               agent {
//         docker {
//           label 'docker'
//           image 'node:7-alpine'
//           args '--name docker-node' // list any args
//         }
//       }
//         steps{
//           script {
//               dockerImage = docker.build registry + ":$BUILD_NUMBER"
//           }
//         }
//     } 
//     // https://us-central1-docker.pkg.dev/linen-waters-366217/wiserly-inventory-planner
//     stage('Docker Push') {
//         steps{
//           script {
//             docker.withRegistry( 'https://us-central1-docker.pkg.dev/linen-waters-366217/wiserly-inventory-planner', registryCredential ) {
//             dockerImage.push()
//             }
//           }
//         }
//     } 


//     stage('Cleaning up') {
//         steps{
//         sh "docker rmi $registry:$BUILD_NUMBER"
//         }
//     } 
//    }
// }
pipeline {
  environment {
    PROJECT = "linen-waters-366217"
    APP_NAME = "wiserly-inventory-planner"
    REPO_NAME = "wiserly-inventory-planner"
    REPO_LOCATION = "us-central1 (Iowa)"
    IMAGE_NAME = "${REPO_LOCATION}-docker.pkg.dev/${PROJECT}/${REPO_NAME}/${APP_NAME}"
  }

  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        metadata:
          labels:
            app: inventory_planner_resources
            namespace: wiserly-inventory-planner
        spec:
          containers:
          - name: docker
            image: gcr.io/cloud-builders/docker
            command:
            - cat
            tty: true
          - name: kubectl
            image: gcr.io/cloud-builders/kubectl
            command:
            - cat
            tty: true
      '''
    }
  }
  
  stages {
    stage('Pull Git'){
      when { expression { true } }
      steps{
        checkout scm
      }
    }

    stage('Build docker image') {
    when { expression { true } }
      steps{
        container('docker'){
          dir('Backend Wiserly') {
            echo 'Build docker image Start'
            sh 'pwd'
            sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            withCredentials([file(credentialsId: "${PROJECT}_artifacts", variable: 'GCR_CRED')]){
              sh 'cat "${GCR_CRED}" | docker login -u _json_key_base64 --password-stdin https://"${REPO_LOCATION}"-docker.pkg.dev'
              sh 'docker push ${IMAGE_NAME}:${IMAGE_TAG}'
              sh 'docker logout https://"${REPO_LOCATION}"-docker.pkg.dev'
            }
            sh 'docker rmi ${IMAGE_NAME}:${IMAGE_TAG}'
            echo 'Build docker image Finish'
          }
        }
      }
    }
  }
}