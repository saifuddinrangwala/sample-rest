#!/bin/bash

sudo docker build -t sample-rest:$(git rev-parse --short HEAD) -t sample-rest:latest .



