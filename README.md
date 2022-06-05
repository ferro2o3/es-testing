# ES Testing

The objective of this project is to both have a series of tests running against an elasticsearch server, and run your own unit tests against it.

The initial objective is to run tests in a step by step way, with test results being shown in the docker standard output.

This is to allow the run of a test series, which is a tool used for testing your knowledge of [Elasticsearch Certified Engineer](https://www.elastic.co/training/elastic-certified-engineer-exam) topics.

In the current version, only tests inside `./tests/es-test` folder are run.

And if you have any test that you think would be great to add into the base certification test list, feel free to fork this project and create a PR with the new test stating to which topic it belongs to.

Any contributor has to accept both the MIT license and accept that their contributions will also be MIT licensed. The act of pushing a PR with a contribution is acceptance of the license and this terms.

For more details check the [LICENSE](https://github.com/ferro2o3/es-testing/blob/main/LICENSE) before contributing.

# Methodology

The whole concept was in a good part inspired on [rustlings](https://github.com/rust-lang/rustlings), the brilliant and simple step by step pratical exercices for rust-lang learning.

At it's bare simple test, the tasks executed are:

- check if the backend is running (aka ping elasticsearch root endpoint to check if it's ready)
- check if the health is green (aka ping elasticsearch `/_health` to check if all shards are accounted for - green state)
- start a simple UI

The UI will show the list of folders available for testing (only es-test by default), and when that is pressed, it will run the exercises, one by one.

The server keeps datastate on elasticsearch, meaning that the server data folder is kept between restarts in a local folder (`./data`).

Deleting that folder, will restart the tests from the begin.

# How does a test works?

The test works by infinite loop in python that triggers the following:

    make count = 0, then

    Check loop
        - check if the result matches the expected
            - if not, update current test to count (current test should show on the screen)
            - sleep 5 seconds
        - if yes, update count += 1
        - if there are no more tests, bail out

# References

- [Python Docker image](https://www.docker.com/blog/containerized-python-development-part-1/)
- [Elasticsearch image](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
- [rustlings](https://github.com/rust-lang/rustlings)
- [Elasticsearch Certification](https://www.elastic.co/training/elastic-certified-engineer-exam)
- [Layout](https://hackersandslackers.com/flask-jinja-templates/)
- [Licensing, Documentation and Style](https://github.com/SergioBenitez/Rocket/blob/master/README.md)

# License

es-testing is licensed under either of the following, at your option:

    Apache License, Version 2.0, ([LICENSE-APACHE](https://github.com/ferro2o3/es-testing/blob/main/LICENSE-APACHE) or https://www.apache.org/licenses/LICENSE-2.0)
    MIT License ([LICENSE-MIT](https://github.com/ferro2o3/es-testing/blob/main/LICENSE-MIT) or https://opensource.org/licenses/MIT)

# Starting

To start the elasticsearch clusters:

    docker-compose up

This will start a minimal 2 cluster setup with just one node, to make this compatible with all the exercises required for the Elasticsearch Certification Exam.

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
