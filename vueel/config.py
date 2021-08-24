from typing import Dict

from screeninfo import get_monitors


class Config:

    def __init__(self, callbacks: Dict[str, callable] = None):
        dimension = (1200, 800)
        position = [(m.width / 2 - dimension[0] / 2, m.height / 2 - dimension[1] / 2) for m in get_monitors() if m.is_primary][0]

        self.callbacks = {} if callbacks is None else callbacks
        self.config = {
            "dimension": dimension,
            "position": position,
            "language": "en",
            "server": {
                "port": 8080
            }
        }

    def set(self, key: str, value: any):
        """
        Set a configuration value.

        :param (str) key: Configuration key-name.
        :param value: Configuration value.
        """

        if key not in self.callbacks or key in self.callbacks and self.callbacks[key](value):
            self.config[key] = value

    def get(self, key: str) -> any:
        """
        Get a value from the configuration.

        :param (str) key: Configuration key-name.
        :return: Configuration value.
        """

        return self.config[key]

    def setCallback(self, key: str, callback: callable):
        self.callbacks[key] = callback

    def unsetCallback(self, key: str) -> callable:
        return self.callbacks.pop(key)
