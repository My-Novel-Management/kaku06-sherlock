# -*- coding: utf-8 -*-
'''
Stage: "古物商"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   裏通りにあるブラックマーケットの商品を扱っている店。シャーロックの知人
#   武器もここで受け取ったり。情報も特殊なものはここで調べる


## scenes
def rumor_treasure_sword(w: World):
    return w.scene("宝剣の噂",
            w.plot_note("知人の古物商に鑑定してもらうと、確かに宝剣だと言われ、目的は達成したと皇太子の使者に伝える"),
            )

