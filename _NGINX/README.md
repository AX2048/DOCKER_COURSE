## NGINX

docker build -t nginx-custom .

docker run -d --rm --name nginx-test -p 80:80 nginx-custom

docker container stop nginx-test