# -*- coding: utf-8 -*-
'''
Stage: "孤児院"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   アイリーが育った孤児院。運営の大本は協会
#   [裏庭]
#   [寝室][寝室]
#   [応接間]
#   [ホール]


## scenes
def a_orphanage(w: World):
    return w.scene("ある孤児院",
            w.plot_note("孤児院に到着し、そこに入る"),
            w.plot_note("なぜここにきたのか尋ねると、$ailyという女性が寄付をしていた場所だったと"),
            w.plot_note("寄付をするとそこの孤児たちが作った栞がもらえるが、それが落ちていたのだ"),
            w.plot_note("尋ねたが、$ailyという女性に心当たりはないらしい"),
            )


def teachers_talk(w: World):
    return w.scene("教師の話",
            "同・部屋",
            w.plot_note("応対してくれた教師（実は$aily）は、ここは養子としてもらわれていく子もいるが、大半は自立して働いて暮らしていると"),
            w.plot_note("その場所に支援してくれているその女性も素晴らしい人だろうと、彼女は言った"),
            w.plot_note("$sherlockはそこで子供たちが自分のことをいつもくる女性の知人と思って話しかける"),
            )


def secret_treasure(w: World):
    return w.scene("子供たちの宝物",
            w.plot_note("子供が彼女からあるものを預かっていることを知った"),
            w.plot_note("それは宝剣だった"),
            "孤児院・前",
            w.plot_note("$sherlockは宝剣をレプリカとすり替え、持ち帰る"),
            )

