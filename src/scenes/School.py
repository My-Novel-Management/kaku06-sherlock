# -*- coding: utf-8 -*-
'''
Stage: "王立学園"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   この国一番の学校
#   教育機関の最高峰で、大学は別途ある


## scenes
def WIP(w: World):
    return w.scene("__scene__",
            )

