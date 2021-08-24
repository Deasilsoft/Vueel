import eel

from vueel import config, DB, T
from . import constants

# Close the DB connection
DB.close()

# Set language to Norwegian
config.set("language", "no")


# TODO: make behaviour like this inherit from vueel
@eel.expose
def language():
    return config.get("language")


# Expose function to the UI
@eel.expose
def hello_world_python():
    return T("app.hello")


# Expose function to the UI
@eel.expose
def print_string(string):
    if len(string) > constants.CHARACTER_MINIMUM:
        print(string)

        return T("app.success")

    return T("app.minimum", minimum=constants.CHARACTER_MINIMUM)
