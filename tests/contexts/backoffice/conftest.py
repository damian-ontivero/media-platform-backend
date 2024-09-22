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


@pytest.fixture(autouse=True)
def clean_storage_test_directory():
    import os
    import shutil

    shutil.rmtree("var/storage-test", ignore_errors=True)
    os.makedirs("var/storage-test", exist_ok=True)
    yield
    shutil.rmtree("var/storage-test", ignore_errors=True)
