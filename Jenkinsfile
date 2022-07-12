pipeline {
  agent {
    docker {
      image 'fiifikrampah/fdi:latest'
      args '-v /etc/passwd:/etc/passwd -v /etc/group:/etc/group'
      args '-u root:root -v /var/lib/jenkins/workspace/myworkspace:/tmp/' + ' -v /var/lib/jenkins/.ssh:/root/.ssh'
    }
  }
  stages {
    stage('Init') {
      steps {
        sh '''
        terraform -chdir=terraform init
        '''
      }
    }
    stage('Plan') {
      steps {
        withCredentials([
            usernamePassword(credentialsId: 'aws_credentials_id', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')
          ]) {
            sh '''
            terraform -chdir=terraform plan -var aws_access_key=${AWS_ACCESS_KEY_ID} -var aws_secret_key=${AWS_SECRET_ACCESS_KEY}
            '''
          }
      }
    }
    stage('Apply') {
      steps {
          withCredentials([
            usernamePassword(credentialsId: 'aws_credentials_id', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')
          ]) {
            sh '''
            terraform -chdir=terraform apply -var aws_access_key=${AWS_ACCESS_KEY_ID} -var aws_secret_key=${AWS_SECRET_ACCESS_KEY} -auto-approve
            '''
        }
      }
    }
    stage('Deploy to EKS') {
      steps {
          withCredentials([
            usernamePassword(credentialsId: 'aws_credentials_id', passwordVariable: 'AWS_SECRET_ACCESS_KEY', usernameVariable: 'AWS_ACCESS_KEY_ID')
          ]) {
            sh '''
            aws eks --region $(terraform  -chdir=terraform output -raw region) update-kubeconfig --name $(terraform  -chdir=terraform output -raw cluster_name)
            helm install fdi kubernetes
            '''
        }
      }
    }
  }
}