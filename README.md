# Pneumonia Detection Using X-RAY With AWS, Docker, GitHub Actions, Flask

1. [Introduction](#introduction)
2. [Flask App](#flask-app)
3. [How To Run?](#how-to-run)
4. [Main Files of Structure](#main-files-of-structure)
5. [Deployment](#deployment)
6. [Continuous Integration and Continuous Deployment (CI/CD)](#continuous-integration-and-continuous-deployment-cicd)

## Introduction

This project aims to create a Flask web application for the detection of pneumonia using X-ray images. With a 22-layered neural network model, we have achieved an accuracy rate of 91%. The project is designed with a modular approach, with different files dedicated to data ingestion, preparing callbacks, training, and prediction. Deployment was carried out on AWS using Docker containerization, and we have established a CI/CD pipeline through GitHub Actions.


## Flask App
<img width="905" alt="Flask Image Xray" src="https://github.com/sandesh0202/Xray-for-Pneumonia/assets/74035326/4e65bd5a-d7bf-4502-bdb5-7d12ce3bb99d">

## How To Run?
#### STEPS:
Clone the repository
'''
https://github.com/sandesh0202/Xray-for-Pneumonia
'''

#### STEP 01- Create a conda environment after opening the repository
'''
conda create -n xray python=3.11.3 -y
'''
'''
conda activate xray
'''
#### STEP 02- install the requirements
'''
pip install -r requirements.txt
'''
'''
#Finally run the following command
python app.py
'''
Now, open up you local host and port
#### DVC cmd
'''
dvc init
dvc repro
dvc dag
'''

### AWS-CICD-Deployment-with-Github-Actions
#### 1. Login to AWS console.
#### 2. Create IAM user for deployment
'''
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

Create and Download the Access Key and Secret Access Key from IAM -> Settings
'''
#### 3. Create ECR repo to store/save docker image
- Save the URI - 691258540533.dkr.ecr.ap-south-1.amazonaws.com/xray
#### 4. Create EC2 machine (Ubuntu)
#### 5. Open EC2 and Install docker in EC2 Machine:
'''
#optional

sudo apt-get update -y

sudo apt-get upgrade
'''
#required
'''
curl -fsSL https://get.docker.com -o get-docker.sh
'''
'''
sudo sh get-docker.sh
'''
'''
sudo usermod -aG docker ubuntu
'''
'''
newgrp docker
'''
#### 6. Configure EC2 as self-hosted runner:
'''
setting>actions>runner>new self hosted runner> choose os> then run command one by one
'''
#### 7. Setup github secrets:
'''
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = demo>>  691258540533.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = xray
'''

## Main Files of Structure 

1. config.yaml - Contains location of files 
2. params.yaml - Adjust Project Parameters as per Requirements 
3. entity - Update the Configuration 
4. configuration manager in src config - reads configuration & creates directories.
5. components - Main Functions of Project
6. pipeline - Pipeline for End-to-End Processing
7. main.py - Main file for Final Execution
8. dvc.yaml - Execution using DVC
9. app.py - Flask Web App File
10. templates/index.html - Design of Web App

## Deployment
The application has been deployed on AWS using Docker containerization. This allows users to access the pneumonia detection service over the internet. The Docker container ensures that the application and its dependencies are isolated and can be easily deployed and scaled.

## Continuous Integration and Continuous Deployment (CI/CD)
We have established a CI/CD pipeline using GitHub Actions. This pipeline automates the process of building, testing, and deploying the application whenever changes are pushed to the repository. This ensures that the application remains up to date and reliable.

---

Thank you for your interest in our Pneumonia Detection Using X-Ray Images project. If you have any questions or feedback, please don't hesitate to reach out.

**Happy coding!**