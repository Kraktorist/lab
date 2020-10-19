### APP05

Simple python application to work with Postgres database.
The app works as a web server which shows the heartbeat of all containers running this application. Every container periodically updates its status into Postgres database running in a named container.
The interval of updates can be set as environment variable ```interval```. Default: 3 (seconds)

First container should be exposed as web server working on port 80. All other containers don't need this setting.
``` bash
docker build . -t app05

```
Run other containers:
``` bash
docker run -dt -v app03:/db app03
docker run -dt -v app03:/db app03
docker run -dt -v app03:/db app03
docker run -dt -v app03:/db app03
```

curl http://localhost. You should see a list of connected containers with their update timestamps
``` json
[
    [
        "b4432c407142",
        "2020-10-16 09:18:47",
        "2020-10-16 08:48:16",
        3
    ],
    [
        "5fc7905f152c",
        "2020-10-16 09:18:47",
        "2020-10-16 08:49:34",
        10
    ]
]
```

**_NOTE:_**  There is an issue when the update of the DB stops working. If you are faced with similar issue please remove all the containers and created volume and run them again

### Excercises
 - run multiple containers with different ```interval```
 - remove all the containers and check if the shared volume ```app03``` still exists
 - create new containers and use the same volume
 - check if you see old data on the web page
 - copy the volume files to local filesystem
 ...
