# -*- coding: utf-8 -*-
'''
Stage: "列車内"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   各列車の中の出来事はここで


## scenes
def talk_about_dark_island(w: World):
    return w.scene("魔獣の島の話",
            )

