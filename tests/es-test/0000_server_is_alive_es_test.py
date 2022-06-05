import pytest


def test_if_server_is_alive():
    assert True == True


@pytest.mark.precheck
def test_number_one():
    """Docstring"""
    assert 1 == 1


@pytest.mark.postcheck
def test_number_two():
    """Docstring"""
    assert [1] == [1]
