FROM ubuntu:latest

RUN apt-get update && apt-get upgrade && apt-get install -y nginx python3-certbot-nginx 

CMD ["nginx", "-g", "daemon off;"]