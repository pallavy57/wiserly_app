// def REPOSITORY_URI = "pallavy57/wiserly-inventory-planner"

pipeline{
   agent any
   environment{
      registry = "pallavy57/wiserly-inventory-planner"
      registryCredential = 'docker-hub'
      dockerImage = ''
   }
   stages{
    stage('Get latest version of code') {
         steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'pallavy57', url: 'https://github.com/pallavy57/wiserly_app.git']]])
            sh "ls -lart ./*"
        }
    } 
    stage('Docker Build') {
        steps{
          script {
              dockerImage = docker.build registry + ":$BUILD_NUMBER"
          }
        }
    } 
    stage('Docker Push') {
        steps{
          script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
            }
          }
        }
    } 


    stage('Cleaning up') {
        steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
        }
    } 
   }
}
