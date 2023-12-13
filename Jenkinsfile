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
    IMAGE_NAME = "wip-repo"
  }

  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        metadata:
          labels:
            name: inventoryplanner
        spec:
          containers:
          - name: dockerapp
            image: gcr.io/cloud-builders/docker
            command:
            - cat
            tty: true
          - name: kubectlapp
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
            sh 'docker build -t ${IMAGE_NAME} .'
            withAWS(credentials: 'aws-jenkins', region: 'eu-north-1') {
                    sh 'aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin  public.ecr.aws/y5g9s1s7'
                    sh 'docker tag ${IMAGE_NAME}:latest public.ecr.aws/y5g9s1s7/wip-repo/${IMAGE_NAME}:latest'
                    sh 'docker push  public.ecr.aws/y5g9s1s7/${IMAGE_NAME}:latest'
            }
            sh 'docker rmi ${IMAGE_NAME}:latest'
            echo 'Build docker image Finish'
          }
        }
      }
    }
  }
}