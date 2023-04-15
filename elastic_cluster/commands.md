# The list of commands to spin an Elasticsearch cluster in docker

docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.9

- to create and start a 3-node Elasticsearch cluster and Kibana instance we need '.env' file and 'docker-compose.yml' file from this tutorial - https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

- commands:

1. Create and start the cluster:
   docker-compose up -d

2. Stop and remove the deployment:

- stop(save the data in the docker volumes for when we want to restart):
  docker-compose down

- restart the cluster with saved data:
  docker-compose up

- delete the network, containers and volumes when we stop the cluster, specify the -v flag:
  docker-compose down -v
