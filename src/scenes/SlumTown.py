# -*- coding: utf-8 -*-
'''
Stage: "スラム街"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   切り裂きジャック事件で有名なホワイト・チャペル地区
#   チャリング・クロスの東5.5Km


## scenes
def goto_empty_house(w: World):
    return w.scene("空き家に向かう",
            )

