def REPOSITORY_URI = "pallavy57/wiserly-inventory-planner"

podTemplate(yaml: '''
    apiVersion: v1
    kind: Pod
    metadata:
      name: wiserly-inventory-planner-pod
      namespace: wiserly-inventory-planner
    spec:
      containers:
      - name: docker
        image: docker
        command:
        - sleep
        args:
        - 99d
''', namespace:"wiserly-inventory-planner", serviceAccount : "wiserly-inventory-planner-web") {
  node("master") {
        stage('Get latest version of code') {
            checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'pallavy57', url: 'https://github.com/pallavy57/wiserly_app.git']]])
            sh "ls -lart ./*"
    }    
    stage('Docker Build') {
      	withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                sh 'docker login --username="${USERNAME}" --password="${PASSWORD}"'
                sh "docker build -t ${REPOSITORY_URI}:${BUILD_NUMBER} ."
                sh 'docker image ls' 
        }
    }
    stage('Docker Push') {
        withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
        sh "docker push ${REPOSITORY_URI}:${BUILD_NUMBER} ."
        sh 'docker image ls' 
        } 
    }


  }
}



