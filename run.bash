#!/bin/bash

CONTAINER_ID=$(sudo docker ps --format="{{.ID}}")
echo $CONTAINER_ID

sudo docker stop $CONTAINER_ID
sudo docker rm $CONTAINER_ID

sleep 5 

sudo docker run -d -p 3601:3601 sample-rest:latest



