### APP06

This is an example of docker-compose deployment. This creates Postgres database ```app02```, a couple of workers ```app05``` and Nginx balancer similar to ```app04``` 
``` bash
docker-compose up -d
```
The application is accessible on http://127.0.0.1:8081 and shows running containers and their status.

#### Exercises
Work with docker-compose.
- run the deployment
- scale the deployment
- destroy the deployment
- change some parameters in docker-compose.yml and see what happens

#### Additionally
- make an image from ```app05```, upload it on hub.docker.com, and modify docker-compose.yml to use the image from Docker hub.
