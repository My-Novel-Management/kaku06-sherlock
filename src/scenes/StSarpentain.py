# -*- coding: utf-8 -*-
'''
Stage: "サーペント通り"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   アイリーの暮らす住居のある通り。住宅街。


## scenes
def rumor_of_aily(w: World):
    return w.scene("$ailyの噂",
            w.plot_note("女の家は高級住宅街にあった"),
            w.plot_note("女の家を訪れる前に周囲に聞いて回る"),
            "近所の家",
            w.plot_note("周囲の評判はいい人で人当たりもよく、色々分けてもらっている話しか出なかった"),
            w.plot_note("$sherlockは$wilsonに「何か妙だ」といってから、$ailyの家に向かう"),
            )

