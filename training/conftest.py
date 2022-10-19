# common fixture for all tests
import pytest
from training.fixture.application import Application

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture