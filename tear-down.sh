#!/bin/bash

docker-compose -f production.yml stop
docker-compose -f production.yml down --remove-orphans
docker rmi -f webapp-nginx
docker rmi webapp-flask
docker volume rm $(docker volume ls -f dangling=true -q)
