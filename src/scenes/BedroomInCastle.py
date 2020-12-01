# -*- coding: utf-8 -*-
'''
Stage: "古城内の個室"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   古城内の個室についてはこっちで担当
#   [個室]


## scenes
def marys_enjoy(w: World):
    return w.scene("楽しむ$maryたち",
            w.plot_note("食事がお開きになり、$sherlockたちは与えられた部屋に戻る"),
            w.plot_note("寝ようとしていたときに、悲鳴が聞こえた"),
            )


def vanishing_moch(w: World):
    return w.scene("消えた$moch",
            w.plot_note("翌朝、$mochの姿が城から消えていた"),
            )
