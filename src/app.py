import eel
import i18n
from win32api import GetSystemMetrics

WINDOW_SIZE = (1200, 800)
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

        return _("Success!")

    return _("app.minimum", minimum=CHARACTER_MINIMUM)


eel.init("web")
eel.start("index.html", size=WINDOW_SIZE, position=(GetSystemMetrics(0) / 2 - WINDOW_SIZE[0] / 2, GetSystemMetrics(1) / 2 - WINDOW_SIZE[1] / 2), options={
    "port": 8080
})
