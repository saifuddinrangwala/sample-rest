#!/bin/bash

ENDPOINT=http://localhost:8080

curl --header "Content-Type: application/json"   --request POST   --data '{"color":"green","taste":"sweet"}' $ENDPOINT/v1/bananas
curl $ENDPOINT/v1/bananas

curl $ENDPOINT/v1/apples
curl $ENDPOINT/v1/apples/1
curl $ENDPOINT/v1/apples/2
curl $ENDPOINT/v1/apples/3


