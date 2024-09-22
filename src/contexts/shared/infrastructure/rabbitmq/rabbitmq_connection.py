from typing import Any
from typing import Awaitable
from typing import Callable

from aio_pika import ExchangeType
from aio_pika import IncomingMessage
from aio_pika import Message
from aio_pika import connect_robust

from contexts.shared.infrastructure.rabbitmq.rabbitmq_config import RabbitMQConfig


class RabbitMQConnection:
    def __init__(self, config: RabbitMQConfig) -> None:
        self._config = config

    async def declare_exchange(self, exchange_name: str, exchange_type: str) -> None:
        connection = await connect_robust(self._config._uri)

        # Context manager is necessary because the connection
        # should be closed after the exchange is declared
        async with connection:
            channel = await connection.channel()

            await channel.declare_exchange(exchange_name, ExchangeType(exchange_type), durable=True)

    async def declare_queue(self, queue_name: str, routing_keys: list[str]) -> None:
        connection = await connect_robust(self._config._uri)

        # Context manager is necessary because the connection
        # should be closed after the queue is declared
        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue(queue_name, durable=True)

            for routing_key in routing_keys:
                exchange_name = routing_key.split(".")[0] + ".domain_events"

                await queue.bind(exchange_name, routing_key)

    async def publish(self, exchange_name: str, message: str, routing_key: str) -> None:
        connection = await connect_robust(self._config._uri)

        # Context manager is necessary because the connection
        # should be closed after the message is published
        async with connection:
            channel = await connection.channel()
            exchange = await channel.get_exchange(exchange_name)

            await exchange.publish(Message(body=message.encode(), content_type="application/json"), routing_key)

    async def consume(self, queue_name: str, on_message: Callable[[IncomingMessage], Awaitable[Any]]) -> None:
        connection = await connect_robust(self._config._uri)

        # Context manager is not necessary because the connextion
        # should be running until the consumer is stopped
        channel = await connection.channel()
        queue = await channel.get_queue(queue_name)

        await queue.consume(on_message, no_ack=True)
