Commands to run beat agents with docker:

# Metricbeat:

1. Pull the image - docker pull docker.elastic.co/beats/metricbeat:8.2.2
2. Run the metricbeat setup(it will create index pattern, load visualizations, dashboards and machine learning jobs):
   docker run \
   docker.elastic.co/beats/metricbeat:8.2.2 \
   setup -E setup.kibana.host=kibana:5601 \
   -E output.elasticsearch.hosts=["elasticsearch:9200"] \
   --network=elastic

   docker run --network=elastic docker.elastic.co/beats/metricbeat:8.2.2 setup -E setup.kibana.host=kibana:5601 -E output.elasticsearch.hosts=["elasticsearch:9200"]

   docker run --network=elastic docker.elastic.co/beats/metricbeat:8.2.2 --help

   docker run --network-elastic docker.elastic.co/beats/metricbeat:8.2.2 run -e

<!--
============= Need to be updated ====================
- With configuration file options:

1. Download a sample config file:
   curl -L -O https://raw.githubusercontent.com/elastic/beats/7.17/deploy/docker/metricbeat.docker.yml
2. Config with volume mount:
   docker run -d \
    --name=metricbeat \
    --user=root \
    --volume="$(pwd)/metricbeat.docker.yml:/usr/share/metricbeat/metricbeat.yml:ro" \
    --volume="/var/run/docker.sock:/var/run/docker.sock:ro" \
    --volume="/sys/fs/cgroup:/hostfs/sys/fs/cgroup:ro" \
    --volume="/proc:/hostfs/proc:ro" \
    --volume="/:/hostfs:ro" \
    docker.elastic.co/beats/metricbeat:7.17.9 metricbeat -e \
    -E output.elasticsearch.hosts=["localhost:9200"]

   docker run -d --name=metricbeat --network=elast-alert_default --user=root --volume="C:\Users\Gari\Desktop\Projects\Elastic alert test\elastic_cluster\metricbeat.docker.yml:/tmp/share/metricbeat/metricbeat.yml:ro" --volume="/var/run/docker.sock:/var/run/docker.sock:ro" --volume="/sys/fs/cgroup:/hostfs/sys/fs/cgroup:ro" --volume="/proc:/hostfs/proc:ro" --volume="/:/hostfs:ro" docker.elastic.co/beats/metricbeat:7.17.9 metricbeat -e -E output.elasticsearch.hosts=["es01:9200"]

docker run docker.elastic.co/beats/metricbeat:7.17.9 setup -E setup.kibana.host=kibana:5601 -E output.elasticsearch.hosts=["172.18.0.3:9300"]
-->
