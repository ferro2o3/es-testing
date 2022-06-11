# Getting started

This list of exercises follow the "Getting Started" guide on [Elasticsearch Quick Start](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html) documentation.

It consists of exercises that allows you to verify your learnings from it.

# Content

## Sending a request to ES

[Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html#send-requests-to-elasticsearch)

As part of this exercise, you will start the server with:

```
docker-compose up
```

Then, after a while, the two clusters should be up.

The first following Elastic recommended setup for multi-node stack with security (3 nodes + kibana), and the second with a minimal single node cluster.

Doing `docker ps` on a terminal should result in something similar to:

```
9eaa448f5008   docker.elastic.co/kibana/kibana:7.17.4                 "/bin/tini -- /usr/l…"   3 minutes ago   Up 3 minutes (healthy)   0.0.0.0:5601->5601/tcp             es-testing_kibana_1
cce3ce9c1da8   docker.elastic.co/elasticsearch/elasticsearch:7.17.4   "/bin/tini -- /usr/l…"   5 minutes ago   Up 5 minutes (healthy)   9200/tcp, 9300/tcp                 es-testing_es03_1
ef0bb962dcab   docker.elastic.co/elasticsearch/elasticsearch:7.17.4   "/bin/tini -- /usr/l…"   5 minutes ago   Up 5 minutes (healthy)   9200/tcp, 9300/tcp                 es-testing_es02_1
865d4af1c033   docker.elastic.co/elasticsearch/elasticsearch:7.17.4   "/bin/tini -- /usr/l…"   5 minutes ago   Up 5 minutes             9300/tcp, 0.0.0.0:9201->9200/tcp   es04
f905dbb89d73   docker.elastic.co/elasticsearch/elasticsearch:7.17.4   "/bin/tini -- /usr/l…"   5 minutes ago   Up 5 minutes (healthy)   0.0.0.0:9200->9200/tcp, 9300/tcp   es-testing_es01_1
```

This means that 2 clusters were created:

    cluster 1   - kibana
                - es01
                - es02
                - es03

    cluster 2   - es04

All elasticsearch nodes are multi-functional (master / data / etc). Cluster 2 is setup as single node cluster.

If you hit the first cluster on it's https endpoint (and accept the security certificate):

### Cluster 1

https://localhost:9200/


### Cluster 2

https://localhost:9201/

