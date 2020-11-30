# -*- coding: utf-8 -*-
'''
Stage: "山小屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   ウィルソン（偽）がしんでいた山小屋


## scenes
def his_dead(w: World):
    return w.scene("彼は死んでいた",
            w.plot_note("同じ手法だったが、それは遠隔操作$gunによる自殺だった"),
            )

