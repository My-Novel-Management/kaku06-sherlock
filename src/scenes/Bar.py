# -*- coding: utf-8 -*-
'''
Stage: "バー"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   バー兼闇の取引所


## scenes
def underground_informater(w: World):
    return w.scene("裏の情報屋",
            w.plot_note("彼女が最後の$stoneの所有者だったという。しかし技法のために売り払い、今手元にはなかった"),
            w.plot_note("$sherlockは何者かが$stoneを四つ手に入れたのだと理解した"),
            )

