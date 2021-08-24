import i18n

from vueel import config

# Load locale files
i18n.load_path.append("resources/locale")

# Set default values
i18n.set("skip_locale_root_data", True)
i18n.set("locale", config.get("language"))
i18n.set("fallback", "en")

# Define the easy to access T function
T = i18n.t


# To be called on language change
def callback(language: str):
    i18n.set("locale", language)

    return True


# Set callback to config key "language"
config.setCallback("language", callback)
