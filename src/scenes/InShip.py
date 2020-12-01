# -*- coding: utf-8 -*-
'''
Stage: "船内・船上"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   船はここで。船内も


## scenes
def goto_dark_island(w: World):
    return w.scene("魔獣の島へ（船上）",
            w.plot_note("$maryたちは旅行だと喜んでいたが、$sherlockは不穏な招待状を怪しんでいた"),
            )

