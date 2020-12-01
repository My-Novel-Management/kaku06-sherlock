# -*- coding: utf-8 -*-
'''
Stage: "港"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   港全般はここで扱う


## scenes
def goto_dark_island(w: World):
    return w.scene("魔獣の島に出港",
            w.plot_note("$sherlockたちは駅から船に乗り換え、その孤島を目指す"),
            )

