import types

import eel

import src
from vueel import C

if isinstance(src, types.ModuleType):

    # LOAD THE PRE-BUILT UI
    eel.init("storage/ui")

    # RUN THE UI WITH EEL
    eel.start("index.html", size=C("dimension"), position=C("position"), port=C("port"))
