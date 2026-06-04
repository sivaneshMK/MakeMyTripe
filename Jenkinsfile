pipeline{
    agent any

    triggers{
        // githubPush()
        pollSCM('H/1 * * * *')
    }

    stages{
        stage('checkout'){

            steps{
                git branch: 'master',
                url: 'https://github.com/sivaneshMK/MakeMyTripe.git'
            }
        }
        stage('Setup Env'){
            steps{
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''

            }
        }
        stage('Run Tests'){

            steps{
                bat'''
                call venv\\Scripts\\activate
                pytest --html=report.html --self-contained-html

                '''
            }
        }
    }

    post {
        always{
            archiveArtifacts artifacts:'report.html', fingerprint:true
        }
    }

}