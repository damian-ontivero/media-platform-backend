import pytest


@pytest.fixture
def mock_serie_repository(mocker):
    return mocker.Mock()
