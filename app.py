import eel

import src
from vueel import C

if src:

    # LOAD THE PRE-BUILT UI
    eel.init("storage/ui")

    # RUN THE UI WITH EEL
    eel.start("index.html", size=C("dimension"), position=C("position"), options=C("server"))
