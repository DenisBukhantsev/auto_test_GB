import pytest

@pytest.fixture()
def bad_text():
    return "колбыса"

@pytest.fixture()
def good_text():
    return "колбаса"
