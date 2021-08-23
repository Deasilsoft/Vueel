import eel

from src import SCREEN_SIZE, WINDOW_SIZE

eel.init("storage/ui")

eel.start("index.html", size=WINDOW_SIZE, position=(int(SCREEN_SIZE[0] / 2 - WINDOW_SIZE[0] / 2), int(SCREEN_SIZE[1] / 2 - WINDOW_SIZE[1] / 2)), options={
    "port": 8080
})
