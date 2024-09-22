import pytest


@pytest.fixture
def mock_media_repository(mocker):
    return mocker.Mock()
