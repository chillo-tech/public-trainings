#!/bin/bash

for node in rabbitmq-1 rabbitmq-2 rabbitmq-3; do
    ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $node)
    echo "$node IP address: $ip"
done