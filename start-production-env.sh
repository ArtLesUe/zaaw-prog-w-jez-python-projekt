docker stop arturapi-node-1
docker stop arturapi-node-2
docker stop arturapi-node-3
docker stop arturapi-node-4

docker rm arturapi-node-1
docker rm arturapi-node-2
docker rm arturapi-node-3
docker rm arturapi-node-4

docker run --publish 8889:8888 --name arturapi-node-1 --detach arturapi:v1
docker run --publish 8890:8888 --name arturapi-node-2 --detach arturapi:v1
docker run --publish 8891:8888 --name arturapi-node-3 --detach arturapi:v1
docker run --publish 8892:8888 --name arturapi-node-4 --detach arturapi:v1