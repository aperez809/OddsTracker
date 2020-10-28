#!/bin/bash

cd /home/ubuntu/cd-Oddstracker

docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build