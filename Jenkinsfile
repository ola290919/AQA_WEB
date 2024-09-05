pipeline {
    agent any
    parameters {
        string(name: 'EXECUTOR_URL', defaultValue: 'selenoid', description: 'Address of Selenoid executor')
        string(name: 'APP_URL', defaultValue: 'http://opencart:8080', description: 'Address of OpenCart application')
        string(name: 'BROWSER', defaultValue: 'chrome', description: 'Browser name')
        string(name: 'BROWSER_VERSION', defaultValue: '127.0', description: 'Browser version')
        string(name: 'NUMPROCESS', defaultValue: '1', description: 'Number of processes')
    }
    environment {
        GIT_REPO = 'https://github.com/ola290919/AQA_WEB.git'
        ALLURE_RESULTS = 'allure-results'
        EXECUTOR_URL = "${params.EXECUTOR_URL}"
        APP_URL = "${params.APP_URL}"
        BROWSER = "${params.BROWSER}"
        BROWSER_VERSION = "${params.BROWSER_VERSION}"
        NUMPROCESS = "${params.NUMPROCESS}"
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'jenkins', url: "${env.GIT_REPO}"
            }
        }
        stage('Install dependencies for tests') {
            steps {
              catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --no-cache-dir virtualenv
                pip3 install -r requirements.txt
                mkdir -p logs
                pytest --executor ${EXECUTOR_URL} --url ${APP_URL} --browser ${BROWSER} --bv ${BROWSER_VERSION} -n ${NUMPROCESS} --alluredir ${ALLURE_RESULTS}
                '''
              }  
            }
        }
        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: "${env.ALLURE_RESULTS}"]]
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}