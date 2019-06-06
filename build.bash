#!/bin/bash

sudo docker build --network=host -t saifuddin53/sample-rest:$(git rev-parse --short HEAD) -t saifuddin53/sample-rest:latest .

sudo docker login

sudo docker push saifuddin53/sample-rest




