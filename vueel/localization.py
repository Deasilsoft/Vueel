import pathlib
import re

import eel
import i18n

from vueel import Config

LOCALE_DIR = "resources/locale"

# Load locale files
i18n.load_path.append(LOCALE_DIR)

# Set default values
i18n.set("skip_locale_root_data", True)
i18n.set("locale", Config.get("language"))
i18n.set("fallback", "en")


# To be called on language change
def callback(language: str):
    i18n.set("locale", language)

    return True


def available(dir=None, locales=None):
    if dir is None:
        directory = pathlib.Path(LOCALE_DIR)
    else:
        directory = dir

    if locales is None:
        locales = []

    for child in directory.iterdir():
        locale = re.sub(r"^[^.]+\.", "", child.stem)

        if child.is_file() and locale not in locales:
            locales.append(locale)
        elif child.is_dir():
            locales = available(child, locales)

    return locales


# Set callback to config key "language"
Config.set_callback("language", callback)


@eel.expose
def T(key, **kwargs):
    """Get language string from key, insert arguments into string where applicable."""
    return i18n.t(key, **kwargs)
