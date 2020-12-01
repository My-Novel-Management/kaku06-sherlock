# -*- coding: utf-8 -*-
'''
Stage: "アイリーの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   アイリーが住んでいる（はず）の家。高級住宅地にある戸建ての別荘で
#   皇太子を騙すために利用したもの
#   ：２F
#   ：１F
#   ：Ｂ１Ｆ


## scenes
def her_absence(w: World):
    return w.scene("$ailyは不在",
            w.plot_note("しかし誰も出てこない"),
            w.plot_note("鍵が空いているのを妙に思い、中に入る"),
            )


def found_corpse(w: World):
    return w.scene("発見された遺体",
            "$ailyの家の中",
            w.plot_note("家の中はがらんとしていて、まるで新居のよう"),
            "同・寝室",
            w.plot_note("一つだけ木箱が置かれていただけで、そこには人が倒れていた"),
            w.plot_note("女の家で謎の女性の遺体が発見された"),
            )


def hello_restrade(w: World):
    return w.scene("$restradeと$sherlock",
            "$ailyの家・寝室",
            w.plot_note("$sherlockは警察に連絡を取る"),
            w.plot_note("現れたのは$restradeで、$sherlockとは旧知の仲のようだった"),
            w.plot_note("$sherlockは$restradeと少し話す"),
            )


def investigation_aily_room(w: World):
    return w.scene("家宅捜索",
            "同・キッチン",
            w.plot_note("$sherlockは現場を見て、殺害されていたのは$ailyではないと言う"),
            w.plot_note("そもそも家の中にものがなさすぎて、生活していた証拠がない"),
            w.plot_note("遺体の身元は行方不明になっている人間の誰かだろうと"),
            w.plot_note("自分がここにきたのはある人物に彼女にあずけているものを取り戻してほしいと頼まれたからだ、とだけ"),
            w.plot_note("$sherlockは$wilsonと一緒に外に出て、ある場所に行くように指示する"),
            w.plot_note("行き先はある孤児院だった"),
            )
