def REPOSITORY_URI = "pallavy57/wiserly-inventory-planner"     
pipeline {
agent {
    label 'master'
}    
stages {
    // stage('Docker Install') {
    //     agent {
    //         docker { image 'node:20.10.0-alpine3.18' }
    //     }
    //     steps {
    //         sh 'node --version'
    //         sh 'docker ps'
    //     }
    // }
    stage('Get latest version of code') {
        agent any
         steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'pallavy75', url: 'git@github.com:pallavy57/wiserly_app.git']]])
            sh "ls -lart ./*"
        }
    }    
    stage('Docker Build') {
    	agent any
      steps {
      	withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh 'docker login --username="${USERNAME}" --password="${PASSWORD}"'
                sh "docker build -t ${REPOSITORY_URI}:${BUILD_NUMBER} ."
                sh 'docker image ls' 
        } 
      }
    }
    stage('Docker Push') {
    	agent any
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
        sh "docker push ${REPOSITORY_URI}:${BUILD_NUMBER} ."
        sh 'docker image ls' 
        } 
      }
    }
  }
}  
  
  
  
