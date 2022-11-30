docker stop arturapi-node-1
docker stop arturapi-node-2
docker stop arturapi-node-3
docker stop arturapi-node-4
docker stop arturapi-balancer

docker rm arturapi-node-1
docker rm arturapi-node-2
docker rm arturapi-node-3
docker rm arturapi-node-4
docker rm arturapi-balancer

docker image rm arturapi:v1 --force
docker image rm arturapi:v2 --force
docker build --tag arturapi:v1 --file Dockerfile .
docker build --tag arturapi:v2 --file Dockerfile2 .