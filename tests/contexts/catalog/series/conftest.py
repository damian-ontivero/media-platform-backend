import pytest


@pytest.fixture
def mock_serie_repository(mocker):
    return mocker.Mock()


@pytest.fixture
def mock_media_finder(mocker):
    return mocker.Mock()
