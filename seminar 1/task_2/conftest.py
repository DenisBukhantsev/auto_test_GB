import pytest
from HW1_test import get_login
@pytest.fixture()
def token():
    return get_login()

@pytest.fixture()
def get_description():
    return 'New_description_for_test'

