import pytest


@pytest.fixture
def mock_command_bus(mocker):
    return mocker.AsyncMock()


@pytest.fixture
def mock_query_bus(mocker):
    return mocker.AsyncMock()


@pytest.fixture
def mock_event_bus(mocker):
    return mocker.AsyncMock()
