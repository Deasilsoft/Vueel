import eel
from screeninfo import get_monitors

from vueel import getDB, L

getDB().close()

# TODO: MOVE SCREEN_SIZE AND WINDOW_SIZE HANDLING TO VUEEL CONFIGURATION
SCREEN_SIZE = [(m.width, m.height) for m in get_monitors() if m.is_primary][0]
WINDOW_SIZE = (1200, 800)

CHARACTER_MINIMUM = 3


@eel.expose
def hello_world_python():
    return L("app.hello")


@eel.expose
def print_string(string):
    if len(string) > CHARACTER_MINIMUM:
        print(string)

        return L("app.success")

    return L("app.minimum", minimum=CHARACTER_MINIMUM)
