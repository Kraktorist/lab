### APP03

Simple python application to work with shared volumes.
The app works as a web server which shows the heartbeat of all containers running this application. Every container periodically updates its status into SQLite database located on a shared volume.
The interval of updates can be set as environment variable ```interval```. Default: 3 (seconds)
The path to the database is ```dbpath```. Default: /db/app03.db
First container should be exposed as web server working on port 80. All other containers don't need this setting.
``` bash
docker build . -t app03
docker run -dt -p 80:80 -v app03:/db app03
```
Run other containers:
``` bash
docker run -dt e interval=10 -v app03:/db app03
docker run -dt e interval=1 -v app03:/db app03
docker run -dt e interval=15 -v app03:/db app03
docker run -dt e interval=30 -v app03:/db app03
```

**_NOTE:_**  SQLite is not a shared database actually therefore there is an issue when the update of the DB stops working. If you are faced with similar issue please remove all the containers and created volume and run them again

