import re


class RabbitMQQueueFormatter:
    """
    RabbitMQQueueFormatter is responsible for formatting the queue name.

    The queue name is formatted as follows:
    - The subscriber class name is split by the uppercase letters.
    - The split words are joined by an underscore.
    - The joined words are converted to lowercase.
    - The context name is prepended to the formatted queue name.

    Example:
    - Subscriber class name: UpdateUserProjectionOnUserUpdated
    - Module name: retentions
    - Formatted queue name: retentions.update_user_projection_on_user_updated
    """

    def __init__(self, context: str) -> None:
        if not context:
            raise ValueError("context must not be empty")

        if not isinstance(context, str):
            raise TypeError("context must be a string")

        self._context = context.lower()

    def format(self, value: str) -> str:
        name = re.sub(r"(?<!^)(?=[A-Z])", "_", value).lower()

        return f"{self._context}.{name}"
