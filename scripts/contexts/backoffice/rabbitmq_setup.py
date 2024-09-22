import asyncio

from apps.backoffice.api.v0.dependecy_injection import container
from contexts.shared.infrastructure.event_bus.rabbitmq.rabbitmq_configurer import RabbitMQConfigurer


def run() -> None:
    configurer: RabbitMQConfigurer = container.find("RabbitMQConfigurer")

    asyncio.run(configurer.configure())
