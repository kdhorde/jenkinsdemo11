pipeline {
 agent any 
  stages{
    stage('checkout code'){
        steps{
           checkout scm
        }
    }
    stage('Extract data'){
        steps{
           bat "python extract.py" 
        }
    }

 }

}