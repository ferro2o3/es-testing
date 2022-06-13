# Elasticsearch Testing

This project is very loosely based on [rustlings](https://github.com/rust-lang/rustlings).

The objective is to help with validating your knowledge on all things elasticsearch.

It's designed around the [Elasticsearch Certified Engineer](https://www.elastic.co/training/elastic-certified-engineer-exam) topics, but has a couple more things added on it.


# Methodology

You run the setup (docker compose containers), then run the python project (very simple flask python app), and hit the http endpoint of it.

Then you are proposed a list of topics.

Each topic is composed by a series of exercises which will validate themselves and stop either on the next execise that needs completion or at the end of it.

Then you can either reset the topic to restart it, or continue to another topic.

State is preserved in the data folder (along with the elasticsearch data files), so if you remove that folder, everything will be reset.

# Setup

Start the elasticsearch clusters with:

```
docker-compose up
```

Then, after a while, the two clusters should be up.

The first follows Elastic [recommended setup](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-compose-file) for multi-node stack with security (3 nodes + kibana), and the second with a minimal [single node cluster](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-dev-mode).

> Neither are "production ready"! For that please consult the [guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-prod-prerequisites) and other recommended practices for your platform of choice.

After running the command, doing `docker ps` on a terminal should result in something similar to:

```
CONTAINER ID   IMAGE                                                  COMMAND                  CREATED          STATUS                   PORTS                              NAMES
dd09b6b01f5b   docker.elastic.co/elasticsearch/elasticsearch:7.17.4   "/bin/tini -- /usr/l…"   9 minutes ago    Up 9 minutes             9300/tcp, 0.0.0.0:9201->9200/tcp   cluster2-es04
6ed2fc610311   docker.elastic.co/kibana/kibana:7.17.4                 "/bin/tini -- /usr/l…"   12 minutes ago   Up 8 minutes (healthy)   0.0.0.0:5601->5601/tcp             es-testing_kibana_1
0966f996e275   docker.elastic.co/elasticsearch/elasticsearch:7.17.4   "/bin/tini -- /usr/l…"   13 minutes ago   Up 9 minutes (healthy)   9200/tcp, 9300/tcp                 cluster1-es03
5102ca270771   docker.elastic.co/elasticsearch/elasticsearch:7.17.4   "/bin/tini -- /usr/l…"   13 minutes ago   Up 9 minutes (healthy)   9200/tcp, 9300/tcp                 cluster1-es02
dcdda678ea2a   docker.elastic.co/elasticsearch/elasticsearch:7.17.4   "/bin/tini -- /usr/l…"   13 minutes ago   Up 9 minutes (healthy)   0.0.0.0:9200->9200/tcp, 9300/tcp   cluster1-es01
```

This means that 2 clusters were created:

    cluster1    - kibana
                - es01
                - es02
                - es03

    cluster2    - es04

All elasticsearch nodes are multi-functional (master / data / etc). Cluster 2 is setup as single node cluster.

You can hit the clusters at the https endpoints of:

## Cluster 1

- https://localhost:9200/

    curl --cacert ./certs/ca/ca.crt -u elastic:elastic https://localhost:9200

## Cluster 2

- https://localhost:9201/

    curl --cacert ./certs/ca/ca.crt -u elastic:elastic https://localhost:9201


# Run the tests

Just type to setup:

    python -m venv .venv
    . .venv/bin/activte
    pip install -U pip
    pip install -r requirements.txt

And then to run it:

    flask run src/server.py

If you are developing new tests, you may need to run instead:

    pip install -r requirements.dev.txt

The main difference is the addition of black and flask8 for code styling / formating.

# References

- [Python Docker image](https://www.docker.com/blog/containerized-python-development-part-1/)
- [Elasticsearch image](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
- [rustlings](https://github.com/rust-lang/rustlings)
- [Elasticsearch Certification](https://www.elastic.co/training/elastic-certified-engineer-exam)
- [Layout](https://hackersandslackers.com/flask-jinja-templates/)
- [Licensing, Documentation and Style](https://github.com/SergioBenitez/Rocket/blob/master/README.md)

# Contributions

Contributions are welcomed with PRs targeting the main branch. All authors of PRs have to accept that their contributions are lisenced by both APACHE 2.0 and MIT licenses and will be distributed with such licenses. Submission of a PR is acceptence of such terms.

# Licenses

For users, es-testing is licensed under either of the following, at your option:

    Apache License, Version 2.0, ([LICENSE-APACHE](https://github.com/ferro2o3/es-testing/blob/main/LICENSE-APACHE) or https://www.apache.org/licenses/LICENSE-2.0)
    MIT License ([LICENSE-MIT](https://github.com/ferro2o3/es-testing/blob/main/LICENSE-MIT) or https://opensource.org/licenses/MIT)

Users are free to redistribute on either (or both) of those licenses as they choose.
