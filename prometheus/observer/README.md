### What is this
Simple monitoring system to check different Internet resources based on the HTTP(S), ICMP, SMTP responses.
It's build using Docker, Prometheus and blackbox_exporter 

### How to use

```
cd c:\repos\
git clone https://github.com/Kraktorist/lab.git

docker network create prometheus
docker run --rm --network=prometheus -d -p 9115:9115 --name blackbox_exporter -v C:\repos\lab\prometheus\observer\blackbox:/config prom/blackbox-exporter:v0.18.0 --config.file=/config/blackbox.yml
docker run --rm --network=prometheus --name prometheus -d -p 9090:9090 -v C:\repos\lab\prometheus\observer\prometheus:/etc/prometheus  prom/prometheus:v2.25.0
```

### How to update the list of monitored URIs

Update ```prometheus/targets.d/http.yml``` or add another *.yml file with targets in the same folder.