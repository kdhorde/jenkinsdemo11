pipeline {
    agent any

    stages {
        stage('Checkout code') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat '''
                C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install --upgrade pip
                C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install pandas python-dateutil
                '''
            }
        }

        stage('Extract data') {
            steps {
                bat 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe extract.py'
            }
        }
    }
}
