FROM nginx:latest

RUN apt-get update
RUN apt-get upgrade -y

COPY . /etc/nginx/conf.d/
