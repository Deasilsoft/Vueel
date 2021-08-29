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
Config.set_callback("language", callback)


@eel.expose
def T(key, **kwargs):
    """Get language string from key, insert arguments into string where applicable."""
    return i18n.t(key, **kwargs)
