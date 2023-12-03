def REPOSITORY_URI = "pallavy57/wiserly-inventory-planner"
// pipeline {
//    agent {dockerfile true}

//   stages {
//     stage('Get latest version of code') {
//         agent any
//          steps {
//             checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'pallavy57', url: 'https://github.com/pallavy57/wiserly_app.git']]])
//             sh "ls -lart ./*"
//         }
//     }    
//     stage('Docker Build') {
//       steps {
//       	withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
//                 sh 'docker login --username="${USERNAME}" --password="${PASSWORD}"'
//                 sh "docker build -t ${REPOSITORY_URI}:${BUILD_NUMBER} ."
//                 sh 'docker image ls' 
//         } 
//       }
//     }
//     stage('Docker Push') {
//     	agent any
//       steps {
//         withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
//         sh "docker push ${REPOSITORY_URI}:${BUILD_NUMBER} ."
//         sh 'docker image ls' 
//         } 
//       }
//     }
//   }
// }


pipeline {
    agent {
        docker { image 'node:20.10.0-alpine3.18' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}



  
  
