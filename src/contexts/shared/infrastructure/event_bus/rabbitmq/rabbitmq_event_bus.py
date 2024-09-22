import json

from contexts.shared.domain.domain_event import DomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber
from contexts.shared.domain.event_bus.event_bus import EventBus
from contexts.shared.infrastructure.event_bus.domain_event_deserializer import DomainEventDeserializer
from contexts.shared.infrastructure.event_bus.rabbitmq.rabbitmq_consumer import RabbitMQConsumer
from contexts.shared.infrastructure.event_bus.rabbitmq.rabbitmq_exchange_formatter import RabbitMQExchangeFormatter
from contexts.shared.infrastructure.event_bus.rabbitmq.rabbitmq_queue_formatter import RabbitMQQueueFormatter
from contexts.shared.infrastructure.logger.logger import Logger
from contexts.shared.infrastructure.rabbitmq.rabbitmq_connection import RabbitMQConnection


class RabbitMQEventBus(EventBus):
    def __init__(
        self,
        subscribers: list[DomainEventSubscriber],
        connection: RabbitMQConnection,
        exchange_formatter: RabbitMQExchangeFormatter,
        queue_formatter: RabbitMQQueueFormatter,
        logger: Logger,
    ) -> None:
        super().__init__(subscribers)

        self._connection = connection
        self._exchange_formatter = exchange_formatter
        self._queue_formatter = queue_formatter
        self._logger = logger

    async def add_subscribers(self) -> None:
        deserializer = DomainEventDeserializer.configure(self._subscribers)

        for subscriber in self._subscribers:
            queue_name = self._queue_formatter.format(subscriber.__class__.__name__)
            consumer = RabbitMQConsumer(self._connection, subscriber, deserializer, self._logger)

            self._logger.info(f"Subscribing {subscriber.__class__.__name__} to {queue_name}")
            await self._connection.consume(queue_name, consumer.on_message)

    async def publish(self, events: list[DomainEvent]) -> None:
        for event in events:
            routing_key = event.type
            message = json.dumps(event.to_primitives())

            self._logger.info(f"Publishing {event.__class__.__name__} to {routing_key}")
            await self._connection.publish(self._exchange_formatter.format(), message, routing_key)
