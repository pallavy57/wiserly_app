def REPOSITORY_URI = "pallavy57/wiserly-inventory-planner"

podTemplate(yaml: '''
    apiVersion: v1
    kind: Pod
    metadata:
      name: master
      namespace: wiserly-inventory-planner
    spec:
      containers:
      - name: docker
        image: docker
        command:
        - sleep
        args:
        - 99d
''') {
  node("wiserly-inventory-planner") {
        stage('Get latest version of code') {
        agent any
         steps {
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'pallavy57', url: 'https://github.com/pallavy57/wiserly_app.git']]])
            sh "ls -lart ./*"
        }
    }    
    stage('Docker Build') {
    	agent {
        docker {
            image 'docker'
            reuseNode true
              }
          }
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



