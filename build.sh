#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: Version argument is missing."
    exit 1
fi

echo "Building docker image for version $1"
docker build --platform linux/amd64 -t ghcr.io/yuichiromukaiyama/chatgpt-plugin-example:$1 .
docker push ghcr.io/yuichiromukaiyama/chatgpt-plugin-example:$1

echo "build successfully!"
echo "docker pull ghcr.io/yuichiromukaiyama/chatgpt-plugin-example:$1"