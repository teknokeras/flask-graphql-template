#!/bin/bash

docker-compose stop
docker-compose down
docker rmi webapp-nginx
docker rmi webapp-flask
docker volume rm $(docker volume ls -f dangling=true -q)
