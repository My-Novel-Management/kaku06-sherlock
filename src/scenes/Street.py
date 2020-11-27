# -*- coding: utf-8 -*-
'''
Stage: "通り"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   路地は基本ここで処理。家の前なども路地側なので、こちらで
#   市内の路地の多くは石畳化されている


## scenes
def baker_street(w: World):
    return w.scene("$Baker通り",
            w.plot_note("$wilsonは$carで$sherlockの家の前までやってくる"),
            w.plot_note("$wilsonは近くにいた子供（$ignes）に家を尋ねて教えてもらう"),
            w.plot_note("そこで子供たちがもめ始めて、困惑"),
            w.plot_note("なんとか場が収まり、$sherlockの家を訪問する"),
            )


def he_is_sherlock(w: World):
    return w.scene("$sherlockという男",
            w.plot_note("$sherlockは何も言っていないのに$wilsonの素性を言い当てる"),
            w.plot_note("その上で王室からの依頼は受けないと言って断る"),
            w.plot_note("最後に「さっきの子供に財布をすられてるよ」と"),
            w.plot_note("$wilsonは振り返ったがもう子供たちの姿は消えていた"),
            )


def goto_curio_dealer(w: World):
    return w.scene("古物商を訪ねて",
            w.plot_note("$sherlockは裏通りを歩く"),
            )
