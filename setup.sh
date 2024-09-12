#!/bin/bash

docker-compose build
docker-compose up -d
docker-compose logs > log.txt
