#!/bin/bash

docker-compose -f development.yml stop
docker-compose -f development.yml down --remove-orphans
docker rmi -f webapp-nginx
docker rmi webapp-flask
docker volume rm $(docker volume ls -f dangling=true -q)
