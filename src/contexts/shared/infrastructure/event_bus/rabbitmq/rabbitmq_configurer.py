from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber
from contexts.shared.infrastructure.event_bus.rabbitmq.rabbitmq_exchange_formatter import RabbitMQExchangeFormatter
from contexts.shared.infrastructure.event_bus.rabbitmq.rabbitmq_queue_formatter import RabbitMQQueueFormatter
from contexts.shared.infrastructure.rabbitmq.rabbitmq_connection import RabbitMQConnection


class RabbitMQConfigurer:
    def __init__(
        self,
        connection: RabbitMQConnection,
        exchange_formatter: RabbitMQExchangeFormatter,
        queue_formatter: RabbitMQQueueFormatter,
        subscribers: list[DomainEventSubscriber],
    ) -> None:
        self._connection = connection
        self._exchange_formatter = exchange_formatter
        self._queue_formatter = queue_formatter
        self._subscribers = subscribers

    async def configure(self) -> None:
        await self._declare_exchange(self._exchange_formatter.format())

        for subscriber in self._subscribers:
            await self._declare_queue(subscriber)

    async def _declare_exchange(self, exchange_name: str) -> None:
        await self._connection.declare_exchange(exchange_name, "direct")

    async def _declare_queue(self, subscriber: DomainEventSubscriber) -> None:
        routing_keys = [event.EVENT_NAME for event in subscriber.subscribed_to()]
        queue_name = self._queue_formatter.format(subscriber.__class__.__name__)

        await self._connection.declare_queue(queue_name, routing_keys)
