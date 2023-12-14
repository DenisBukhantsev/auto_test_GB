import pytest
from HW1_test import get_post, test_post_create, test_check_post_create
id_chek = 92417
def test_1(token):
    output = get_post(token)["data"]
    result = [item["id"] for item in output]
    assert id_chek in result

def test_2(get_description):
    res = test_check_post_create()
    assert get_description in res, 'check_post_create FAIL'