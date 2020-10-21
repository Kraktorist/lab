### APP02

Simple postgres database application. Following commands create a bridge network where the container will be placed and run custom postgres and adminer (web application to manage various databases)  
```bash
docker network create --driver=bridge db
docker build . -t postgres
docker run -dt --name postgres --network db -e POSTGRES_PASSWORD=mysecret postgres
docker run -dt --name adminer --network db -p 8080:8080 adminer
```
Now adminer should be available on port 8080

#### Exercices
- Login to the database using adminer
- check if you see new database ```app```
- rebuild the container with different database name and credentials

