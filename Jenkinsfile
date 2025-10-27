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
           bat "C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe extract.py" 
        }
    }

 }

}