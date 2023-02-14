# ehr-bridge
EHR Bridge Application

# Dokcer Configuration

## Check docker is running on your machine 
 - docker ps or sudo docker ps (currently no container or image found)

## Run Build
 - docker-compose -f dc-local.yml build or sudo docker-compose -f dc-local build.yml

## Check all the docker images
 - docker images or sudo docker images

## Up the docker
 - docker-compose -f dc-local.yml up or sudo docker-compose -f dc-local.yml up  (Run the project)

## Check all the docker container
 - docker ps -a or sudo docker ps -a (Now you got some containers which is used in project)


## Check project is running or not
    - Go to browser
        - http://127.0.0.1:8000/swagger/

## To create a superuser account, use this command
 - docker exec -it ehr_bridge_django_local bash
    - python manage.py createsuperuser (Ask for username, email and password)