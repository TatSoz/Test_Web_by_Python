"""DDT"""

import pytest


@pytest.fixture()
def coordinates():
    return 37.7891838, -122.4033522


@pytest.fixture()
def text():
    return 'One Montgomery Tower'