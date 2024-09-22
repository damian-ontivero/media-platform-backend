import os


class RabbitMQConfig:
    def __init__(self, uri: str) -> None:
        self._uri = uri

    @property
    def uri(self) -> str:
        return self._uri

    @classmethod
    def from_env(cls) -> "RabbitMQConfig":
        uri = os.environ.get("RABBITMQ_URI", "").lower()

        return cls(uri)
