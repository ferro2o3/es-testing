import os
import pytest
from base64 import b64encode

if os.getenv("_PYTEST_RAISE", "0") != "0":

    @pytest.hookimpl(tryfirst=True)
    def pytest_exception_interact(call):
        raise call.excinfo.value

    @pytest.hookimpl(tryfirst=True)
    def pytest_internalerror(excinfo):
        raise excinfo.value


ES_USERNAME = "elastic"
ES_PASSWORD = os.environ.get("ELASTIC_PASSWORD")
ES_TOKEN = b64encode(f"{ES_USERNAME}:{ES_PASSWORD}".encode("utf8")).decode("ascii")
