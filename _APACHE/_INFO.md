## APACHE

docker build -t apache-custom .

docker run -d --rm --name apache-test -p 80:80 apache-custom
