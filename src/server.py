from flask import Flask
import os
import subprocess

server = Flask(__name__)


@server.route("/")
def hello():

    my_list = os.listdir("./tests")

    run_it = [
        "pytest",
        "-x",
        "--tb=no",
        "--color=no",
        "-s",
        "tests/es-test/0001_server_is_alive_test.py",
        "-m",
        "precheck",
    ]

    result = subprocess.run(run_it, stdout=subprocess.PIPE)

    # pytest -x --tb=no --color=yes -s tests/es-test/0001_server_is_alive_test.py -m precheck
    # pytest -x --tb=no --color=yes -s tests/es-test/0001_server_is_alive_test.py -m postcheck

    return "Hello World4!"


if __name__ == "__main__":
    server.run(host="0.0.0.0", debug=True)
