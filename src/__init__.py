import eel

from vueel import Config, DB, T
from . import constants

# Close the DB connection
DB.close()

# Set language to Norwegian
Config.set("language", "no")


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
