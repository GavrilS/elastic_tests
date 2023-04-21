# For local development and testing we will use docker-compose.yml file to setup elasticsearch and kibana with xpack-security disabled (the docker-compose file is in the same directory as this file)

1. Run the containers:
   docker-compose up -d

2. To test Elasticsearch and Kibana you can do the following:

- For elasticsearch run: $ curl localhost:9200
  If Elasticsearch has started normally this command will produce a similiar output:
  @Example:
  {
  "name" : "dcfe253860ea",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "2OLBNf1xT4uNWofKUayzbA",
  "version" : {
  "number" : "8.2.2",
  "build_flavor" : "default",
  "build_type" : "docker",
  "build_hash" : "9876968ef3c745186b94fdabd4483e01499224ef",
  "build_date" : "2022-05-25T15:47:06.259735307Z",
  "build_snapshot" : false,
  "lucene_version" : "9.1.0",
  "minimum_wire_compatibility_version" : "7.17.0",
  "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
  }
  @End
- To test if kibana is running open a browser and go to: http://localhost:5601
