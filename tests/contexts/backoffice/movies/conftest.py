import pytest


@pytest.fixture
def mock_movie_repository(mocker):
    return mocker.Mock()
