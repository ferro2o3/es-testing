"""
This works as a smoke test for elasticsearch tests and at the same
time, as a template to make more tests
"""
import requests
from conftest import ES_TOKEN


def description():
    return """<p><b>Elasticsearch server is available.</b></p>
<br />
<p>This test checks the presence of elasticsearch on port 9200.</p>
"""


def test_if_server_is_alive():
    try:
        r = requests.get(
            "https://localhost:9200/_search",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Basic {ES_TOKEN}",
            },
            verify="./certs/ca/ca.crt",
        )
        status = r.status_code
    except:
        status = 404

    assert status == 200
