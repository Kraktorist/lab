### APP02

Simple postgres database application. Following commands create a bridge network where the container will be placed and run adminer (web application to manage various databases)  
```bash
docker network create --driver=bridge db
docker build . -t postgres
docker run -dt --name postgres --network db -e POSTGRES_PASSWORD=mysecret postgres
docker run -dt --name adminer --network db -p 8080:8080 adminer
```
