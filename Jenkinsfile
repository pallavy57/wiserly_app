// def REPOSITORY_URI = "pallavy57/wiserly-inventory-planner"

pipeline{
    agent {
    label 'docker' 
  }
   environment{
      registry = "pallavy57/wiserly-inventory-planner"
      registryCredential = 'gcr:linen-waters-366217'
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
              agent {
        docker {
          label 'docker'
          image 'node:7-alpine'
          args '--name docker-node' // list any args
        }
      }
        steps{
          script {
              dockerImage = docker.build registry + ":$BUILD_NUMBER"
          }
        }
    } 
    // https://us-central1-docker.pkg.dev/linen-waters-366217/wiserly-inventory-planner
    stage('Docker Push') {
        steps{
          script {
            docker.withRegistry( 'https://us-central1-docker.pkg.dev/linen-waters-366217/wiserly-inventory-planner', registryCredential ) {
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
