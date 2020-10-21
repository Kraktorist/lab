### APP01

This simple python application creates a web-server which returns environment variables on any get request

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

``` json
{
    "GPG_KEY": "E3FF2839C048B25C084DEBE9B26995E310250568",
    "HOME": "/root",
    "HOSTNAME": "ba43b94015c6",
    "LANG": "C.UTF-8",
    "PATH": "/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "PYTHON_GET_PIP_SHA256": "6e0bb0a2c2533361d7f297ed547237caf1b7507f197835974c0dd7eba998c53c",
    "PYTHON_GET_PIP_URL": "https://github.com/pypa/get-pip/raw/fa7dc83944936bf09a0e4cb5d5ec852c0d256599/get-pip.py",
    "PYTHON_PIP_VERSION": "20.2.3",
    "PYTHON_VERSION": "3.8.6",
    "TERM": "xterm"
}
```

#### Exercises


- run another container on a different port
- run a container with additional environment variables
- build an python image based on linux image
- ...
