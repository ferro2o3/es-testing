"""
This works as a smoke test for elasticsearch tests and at the same
time, as a template to make more tests
"""
import requests


def description():
    return """<p><b>Elasticsearch server is available.</b></p>
<br />
<p>This test checks the presence of elasticsearch on port 9200.</p>
"""


def test_if_server_is_alive():
    try:
        r = requests.get(
            "http://localhost:9200", headers={"Content-Type": "application/json"}
        )
        status = r.status_code
    except:
        status = 404

    assert status == 200
