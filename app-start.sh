#!/bin/bash

ls deployment-root
docker-compose -f docker-compose.prod.yml up -d --build