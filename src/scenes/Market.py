# -*- coding: utf-8 -*-
'''
Stage: "市場"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   立っている市場はどこでもここを使う。基本は古くから立っている賑わいのあるバラ市場


## scenes
def mystery_of_aily_corpse(w: World):
    return w.scene("$aily家の遺体の謎",
            w.plot_note("ただ謎の殺人事件と消えた$ailyについての謎が残った"),
            )


def shopping_enjoy(w: World):
    return w.scene("楽しいお買い物",
            w.plot_note("$maryは料理はあいかわらず下手だが、それでもよく市場に顔を出して買い物をしていた"),
            w.plot_note("$maryは今日も市場に出かける"),
            w.plot_note("この町の市場の賑わいが$maryは好きだった"),
            w.plot_note("市場には少年探偵団の$ignesも働いている"),
            w.plot_note("最近仲良くなった果物屋の$nowlisから友人からガチョウをもらったと言ってそれを分けてもらえた"),
            w.plot_note("$maryはガチョウを持って帰る"),
            )


def wanted_jack(w: World):
    return w.scene("$jackが指名手配",
            w.plot_note("$jackが改めてその殺人事件の容疑者として手配される"),
            )
