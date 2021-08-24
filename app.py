import eel

import src
from vueel import config

if src:

    # LOAD THE PRE-BUILT UI
    eel.init("storage/ui")

    # RUN THE UI WITH EEL
    eel.start("index.html", size=config.get("dimension"), position=config.get("position"), options=config.get("server"))
