Run nginx
```
docker run --rm -d -v ${PWD}:/usr/share/nginx/html -p 8082:80 nginx
```

```
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                   NAMES
498b0c517612   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8082->80/tcp, :::8082->80/tcp   crazy_hertz
```