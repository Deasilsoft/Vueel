import eel
from screeninfo import get_monitors


class Config:
    """Configuration class."""

    __is_init = False
    __cache = None
    __callbacks = {}

    @staticmethod
    def __init():
        if not Config.__is_init:
            dimension = (1200, 800)
            position = [(m.width / 2 - dimension[0] / 2, m.height / 2 - dimension[1] / 2) for m in get_monitors() if m.is_primary][0]

            Config.__cache = {
                "dimension": dimension,
                "position": position,
                "language": "en",
                "server": {
                    "port": 8080
                }
            }

            Config.__is_init = True

    @staticmethod
    def set(key: str, value: any):
        """
        Set a configuration value.

        :param (str) key: Configuration key.
        :param value: Configuration value.
        """

        Config.__init()

        if key not in Config.__callbacks or key in Config.__callbacks and Config.__callbacks[key](value):
            Config.__cache[key] = value

    @staticmethod
    def get(key: str) -> any:
        """
        Get a value from the configuration.

        :param (str) key: Configuration key.
        :return: Configuration value.
        """

        Config.__init()

        return Config.__cache[key]

    @staticmethod
    def setCallback(key: str, callback: callable):
        """
        Set the callback to the configuration key. Called before value has been changed.

        :param (str) key: Configuration key.
        :param (callable) callback: Callback function.
        """

        Config.__init()

        Config.__callbacks[key] = callback

    @staticmethod
    def unsetCallback(key: str) -> callable:
        """
        Unset the callback to the configuration key.

        :param (str) key: Configuration key.
        :return: Callback unset is returned.
        """

        Config.__init()

        return Config.__callbacks.pop(key)


@eel.expose
def C(key: str):
    """Get configuration value associated with key."""

    return Config.get(key)
