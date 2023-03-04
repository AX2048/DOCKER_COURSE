### Nginx on Ubuntu

Build image and run:
```
docker build -t nginx-ubuntu .

$ docker images
REPOSITORY                   TAG       IMAGE ID       CREATED          SIZE
nginx-ubuntu                 latest    d2314de82762   15 seconds ago   176MB

docker run -d -p 8083:80 nginx-ubuntu

$ docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
d814443078c3   nginx-ubuntu   "nginx -g 'daemon of…"   35 seconds ago   Up 35 seconds   0.0.0.0:8083->80/tcp, :::8083->80/tcp   stoic_gates

$ docker stop d814443078c3
d814443078c3
```