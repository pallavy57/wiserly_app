// def REPOSITORY_URI = "pallavy57/wiserly-inventory-planner"
pipeline {
   agent any
  environment {
registry = "pallavy57/wiserly-inventory-planner"
registryCredential = 'docker-hub'
dockerImage = ''
}
  stages {
    stage('Get latest version of code') {
        agent any
         steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'pallavy57', url: 'https://github.com/pallavy57/wiserly_app.git']]])
            sh "ls -lart ./*"
        }
    }    
    stage('Docker Build') {
      script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
      }
      // steps {
      // 	withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
      //           sh 'docker login --username="${USERNAME}" --password="${PASSWORD}"'
      //           sh "docker build -t ${REPOSITORY_URI}:${BUILD_NUMBER} ."
      //           sh 'docker image ls' 
      //   } 
      // }
    }
    stage('Docker Push') {
    	script {
          docker.withRegistry( '', registryCredential ) {
          dockerImage.push()
      }
      // steps {
      //   withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
      //   sh "docker push ${REPOSITORY_URI}:${BUILD_NUMBER} ."
      //   sh 'docker image ls' 
      //   } 
      // }
    }
    stage('Cleaning up') {
        steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
        }
    }
}
  }
}






  
  
