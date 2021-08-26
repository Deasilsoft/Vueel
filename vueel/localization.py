import eel
import i18n

from vueel import Config

# Load locale files
i18n.load_path.append("resources/locale")

# Set default values
i18n.set("skip_locale_root_data", True)
i18n.set("locale", Config.get("language"))
i18n.set("fallback", "en")


# To be called on language change
def callback(language: str):
    i18n.set("locale", language)

    return True


# Set callback to config key "language"
Config.setCallback("language", callback)


@eel.expose
def T(key, **kwargs):
    """Replace key string with the translation to the selected language (if language is available; default language if it's unavailable is english)."""
    return i18n.t(key, **kwargs)
