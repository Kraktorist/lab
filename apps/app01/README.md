### APP01

This is simple python application creates a web-server which returns environment variables on any get request

#### Build

``` bash
docker build . -t app01
```

#### Run

``` bash
 docker run -dt -p 80:80 app01
```
#### Checks

- Check you see running container

``` bash
docker ps
```

- Check you can get response from the container

``` bash
curl http://localhost
```

you shoud see a JSON which contains a set of environment variables


#### Excersizes


- run another container on a different port
- run a container with additional environment variables
- build a container based on another non-python image
