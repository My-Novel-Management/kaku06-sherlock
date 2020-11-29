# -*- coding: utf-8 -*-
'''
Stage: "図書館"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   王立図書館
#   場所は後ほど選定


## scenes
def ancient_method(w: World):
    return w.scene("太古の秘法",
            w.plot_note("図書館にやってきて、古文書を調べる"),
            w.plot_note("太古の技法で失われた魂を呼び戻す、闇の技法だった"),
            w.plot_note("本当に蘇らせたのだとわかる"),
            )

