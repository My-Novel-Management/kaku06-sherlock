# -*- coding: utf-8 -*-
'''
Stage: "教会"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   教会については、こちらを利用する


## scenes
def mystery_cult(w: World):
    return w.scene("神秘教団",
            w.plot_note("$sherlockは彼女に接触しその技法を教えた$cultXのことをマークした"),
            w.plot_note("そこに情報がもたらされる"),
            )

