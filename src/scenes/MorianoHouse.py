# -*- coding: utf-8 -*-
'''
Stage: "モリアーノの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   モリアーノの住居兼研究室
#   普通に公開している住所で、特に警戒もしていない
#   地域は後で


## scenes
def broken_fire(w: World):
    return w.scene("火事で消え去った",
            w.plot_note("$morianoの邸宅は火事になり、全てが消え去った"),
            )

