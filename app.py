import eel
import i18n
from screeninfo import get_monitors

SCREEN_WIDTH, SCREEN_HEIGHT = [(m.width, m.height) for m in get_monitors() if m.is_primary][0]
WINDOW_WIDTH, WINDOW_HEIGHT = (1200, 800)

CHARACTER_MINIMUM = 3

i18n.load_path.append("localization")
_ = i18n.t


@eel.expose
def hello_world_python():
    return _("app.hello")


@eel.expose
def print_string(string):
    if len(string) > CHARACTER_MINIMUM:
        print(string)

        return _("app.success")

    return _("app.minimum", minimum=CHARACTER_MINIMUM)


eel.init("web")
eel.start("index.html", size=(WINDOW_WIDTH, WINDOW_HEIGHT), position=(int(SCREEN_WIDTH / 2 - WINDOW_WIDTH / 2), int(SCREEN_HEIGHT / 2 - WINDOW_HEIGHT / 2)), options={
    "port": 8080
})
