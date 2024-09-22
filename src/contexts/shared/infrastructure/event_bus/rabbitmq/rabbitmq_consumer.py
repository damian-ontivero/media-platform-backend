from aio_pika import IncomingMessage

from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber
from contexts.shared.infrastructure.event_bus.domain_event_deserializer import DomainEventDeserializer
from contexts.shared.infrastructure.logger.logger import Logger
from contexts.shared.infrastructure.rabbitmq.rabbitmq_connection import RabbitMQConnection


class RabbitMQConsumer:
    def __init__(
        self,
        connection: RabbitMQConnection,
        subscriber: DomainEventSubscriber,
        deserializer: DomainEventDeserializer,
        logger: Logger,
    ) -> None:
        self._connection = connection
        self._subscriber = subscriber
        self._deserializer = deserializer
        self._logger = logger

    async def on_message(self, message: IncomingMessage) -> None:
        event = self._deserializer.deserialize(message.body.decode())

        self._logger.info(f"Received {event.__class__.__name__}")
        await self._subscriber.on(event)
