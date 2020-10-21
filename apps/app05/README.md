### APP05

Simple python application to work with Postgres database.
The app works as a web server which shows the heartbeat of all containers running this application. Every container periodically updates its status into Postgres database which is running in a named container.
The interval of updates can be set as environment variable ```interval```. Default: 3 (seconds)
```dbserver```, ```dbname```, ```dbuser```, ```dbpassword``` are environment variables to connect to the database

#### Build database

Build database image from ```app02```. Create a network and build a container. See ```app02``` for details

#### Run applications

First container should be exposed as web server working on port 80. All other containers don't need this setting.
``` bash
docker build . -t app05
docker run -dt --network db -e dbserver="postgres" -e dbuser="postgres" -e dbpassword="mysecret" -e dbname="app" -e interval=15 -p 80:80 --name app05 app05
```
Run other containers:
``` bash
docker run -dt --network db -e dbserver="postgres" -e dbuser="postgres" -e dbpassword="mysecret" -e dbname="app" -e interval=1 app05
docker run -dt --network db -e dbserver="postgres" -e dbuser="postgres" -e dbpassword="mysecret" -e dbname="app" -e interval=3 app05
docker run -dt --network db -e dbserver="postgres" -e dbuser="postgres" -e dbpassword="mysecret" -e dbname="app" -e interval=5 app05
docker run -dt --network db -e dbserver="postgres" -e dbuser="postgres" -e dbpassword="mysecret" -e dbname="app" -e interval=10 app05
```

curl http://localhost. You should see a list of connected containers with their last update timestamps
``` json
[
    [
        109,
        "dcc41df95b3c",
        15,
        "2020-10-19 14:08:34.744258",
        "2020-10-19 13:31:11.043909"
    ],
    [
        9,
        "f3e6bbcec1ec",
        10,
        "2020-10-19 14:08:31.959897",
        "2020-10-19 13:30:08.941714"
    ]
]
```

#### Exercises
- Run database and containers with another password
- build load balancer on top of the application using nginx
