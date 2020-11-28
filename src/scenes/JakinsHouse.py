# -*- coding: utf-8 -*-
'''
Stage: "ジェイキンスの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   ライムを拾った質屋のオーナーの家
#   場所はSaxeCoburgSquareにある
#   ：２F
#   [寝室][寝室]
#   ：１F
#   [キッチン][バス][トイレ]
#   [応接間]
#   [リビング][応接間（顧客用）]
#   [事務室]


## scenes
def orners_home(w: World):
    return w.scene("オーナー夫婦の家",
            w.plot_note("質屋のオーナー夫婦はいい人そうで、$binsとも顔を合わせて帰っていった"),
            )


def orners_talk(w: World):
    return w.scene("オーナーの話",
            w.plot_note("アリバイ証明から$limeとオーナー夫婦の無実は証明された"),
            w.plot_note("開放された$limeだったがオーナー夫婦からは不審がられ、家を追い出されてしまう"),
            )
