import pytest
import yaml
from Seminar1 import check_Text

def test_check(good_text, bad_text):

    assert good_text in check_Text(bad_text)

