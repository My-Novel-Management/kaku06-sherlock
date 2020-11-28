# -*- coding: utf-8 -*-
'''
Stage: "ジェイキンスの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   ライムを拾った質屋のオーナーの家
#   どこに設定する？　近所かな


## scenes
def scene_name(w: World):
    return w.scene("__scene__",
            )

