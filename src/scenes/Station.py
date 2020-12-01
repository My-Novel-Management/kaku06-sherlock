# -*- coding: utf-8 -*-
'''
Stage: "駅"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   各駅はここで扱う
#   ＜チャリング・クロス駅＞


## scenes
def goto_dark_island(w: World):
    return w.scene("魔獣の島に向けて",
            )

