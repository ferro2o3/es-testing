"""
This works as a smoke test for elasticsearch tests and at the same
time, as a template to make more tests
"""
import requests
from conftest import ES_TOKEN


def description():
    return """<p><b>Add one single document</b></p>
<br />
<p>Using the Single document APIs add one document into the <strong>test-index</strong> of document type <strong>_doc</string>, with the following content:</p>
<blockquote>
{
  "@timestamp": "1969-07-20T20:17:00.000Z",
  "event": {
    "original": "Apollo 11 - Moon landing"
  }
}
</blockquote>
"""


def test_if_server_is_alive():
    print(f"Token: {ES_TOKEN}")
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

    assert status == 201
