#!/bin/bash

ls deployment-root
docker-compose -f deployment-root/docker-compose.prod.yml up -d --build