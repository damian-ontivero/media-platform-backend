class RabbitMQExchangeFormatter:
    """
    RabbitMQExchangeFormatter is responsible for formatting the exchange name.

    The exchange name is formatted as follows:
    - The context name is converted to lowercase.
    - The formatted context name is appended with '.domain_events'.

    Example:
    - Context name: retentions
    - Formatted exchange name: retentions.domain_events
    """

    def __init__(self, context: str) -> None:
        if not context:
            raise ValueError("context must not be empty")

        if not isinstance(context, str):
            raise TypeError("context must be a string")

        self._context = context.lower()

    def format(self) -> str:
        return f"{self._context}.domain_events"
