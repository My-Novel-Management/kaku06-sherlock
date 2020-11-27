# -*- coding: utf-8 -*-
'''
Stage: "市場"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   立っている市場はどこでもここを使う。基本は古くから立っている賑わいのあるバラ市場


## scenes
def mystery_of_aily_corpse(w: World):
    return w.scene("$aily家の遺体の謎",
            w.plot_note("ただ謎の殺人事件と消えた$ailyについての謎が残った"),
            )

