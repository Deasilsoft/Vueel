import eel
from screeninfo import get_monitors


class Config:
    """Configuration class."""

    __callbacks = None
    __cache = None

    @staticmethod
    def reset():
        dimension = (1200, 800)
        position = [(m.width / 2 - dimension[0] / 2, m.height / 2 - dimension[1] / 2) for m in get_monitors() if m.is_primary][0]

        Config.__callbacks = {}
        Config.__cache = {
            "dimension": dimension,
            "position": position,
            "language": "en",
            "server": {
                "port": 8080
            }
        }

    @staticmethod
    def set(key: str, value: any):
        """
        Set a configuration value.

        :param (str) key: Configuration key-name.
        :param value: Configuration value.
        """

        if key not in Config.__callbacks or key in Config.__callbacks and Config.__callbacks[key](value):
            Config.__cache[key] = value

    @staticmethod
    def get(key: str) -> any:
        """
        Get a value from the configuration.

        :param (str) key: Configuration key-name.
        :return: Configuration value.
        """

        return Config.__cache[key]

    @staticmethod
    def setCallback(key: str, callback: callable):
        Config.__callbacks[key] = callback

    @staticmethod
    def unsetCallback(key: str) -> callable:
        return Config.__callbacks.pop(key)


@eel.expose
def C(key: str):
    """Get configuration value associated with key."""
    return Config.get(key)


Config.reset()
