#!/bin/bash

sudo docker rm $(sudo docker ps -a --filter "status=exited" --filter "status=created" --filter "status=dead" --format="{{.ID}}")
sudo docker rmi $(sudo docker images | grep "<none>" | awk '{ print $3 }')
