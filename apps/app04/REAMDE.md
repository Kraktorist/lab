### APP04

It's just a default NGINX proxy for app03 python web application.
First of all we need to create a bridge network "local" to provide connection between ```app03``` and ```app04```
Then run ```app03``` in ```app04```.
``` bash
docker network create local
cd ../app03 
docker build . -t app03
docker run -dt --name worker --network local app03
cd ../app04
docker run --network local --name app03-nginx -p 8080:8081 -v $(pwd)/proxy.conf:/etc/nginx/conf.d/nginx.conf:ro -d nginx
```
The service will be available on http://0.0.0.0:8080/app03

#### Exercises
- build reverse proxy on another port
- add static content to the proxy
