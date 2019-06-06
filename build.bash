#!/bin/bash

sudo docker build --network=host -t sample-rest:$(git rev-parse --short HEAD) -t sample-rest:latest .



