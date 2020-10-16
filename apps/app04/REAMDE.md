### APP04

It's just default NGINX proxy for app03 python web application.
First of all we need to create a bridge network "local" to provide connection between app03 and app04
Then run app03 in app04.
``` bash
docker network create local
cd app03 
docker build . -t app03
docker run -dt --name app03 --network local app03
cd ../app04
docker run --network local --name app03-nginx -p 8080:8081 -v proxy.conf:/etc/nginx/conf.d/nginx.conf:ro -d nginx
```
  
