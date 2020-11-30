# -*- coding: utf-8 -*-
'''
Stage: "隠れ家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   シャーロックと少年探偵団の隠れ家。市場の近くにある


## scenes
def visit_hideout(w: World):
    return w.scene("隠れ家の訪問",
            w.plot_note("$maryたちは$ignesたち少年探偵団に連れられて彼らの隠れ家を訪れる"),
            w.plot_note("そこは$sherlockがもしものために彼らに準備させていた場所だった"),
            w.plot_note("多くの資料が集まり、武器なども収納されている"),
            )


def sherlocks_talk(w: World):
    return w.scene("$sherlockの話（空き家事件について）",
            w.plot_note("そこに$sherlockはいた。大怪我を負っていたが大丈夫だと言う"),
            w.plot_note("そこで$sherlockは自分がこの半年ほどの間にどうしていたのかを語る"),
            w.plot_note("そして$wilsonが偽物で、すべての黒幕だと教えた"),
            w.plot_note("そこに警察から連絡が入る"),
            w.plot_note("$sherlockの指示で監視していた施設が突如爆発したらしい"),
            )
