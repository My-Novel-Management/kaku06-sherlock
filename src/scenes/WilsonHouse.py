# -*- coding: utf-8 -*-
'''
Stage: "ウィルソンの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World

# NOTE
#   ウィルソン（本物）が借りている家
#   場所は通勤地（王宮）にほど近いところで、ベーカー通りまで車で30分程度
#   [キッチン][バス・トイレ]
#   [寝室]
#   [リビング]


## scenes
def prepare_something(w: World):
    return w.scene("何かの準備",
            w.change_camera("wilson"),
            w.change_stage("WilsonHouse"),
            w.change_time("midmorning"),
            w.plot_note("私（$wilson）は出かける準備をしていた"),
            w.plot_note("テーブルの上には新聞記事がちらばっている"),
            w.plot_note("謎の失踪事件が多発していた"),
            w.plot_note("食べかけの朝食を片付け、部屋から出る"),
            w.plot_note("いつも厄介事を頼まれる、そういう運命の下に生まれたんだと語る"),
            )


def rumor_sherlock(w: World):
    return w.scene("$sherlockの噂",
            w.plot_note("$wilsonは外にとめてあった$carに向かう"),
            w.plot_note("そこで大家と出会う"),
            w.plot_note("大家からは家賃を支払ってもらわないと困ると言われるが、今受けた仕事の金が入ったらと"),
            w.plot_note("同じような男がいて困っている。結婚しない男の一人暮らしはどうも信用ならないと"),
            w.plot_note("それが$sherlockという、自称便利屋だが、何をやっているのかさっぱりだと"),
            w.plot_note("$wilsonは$carに乗り込み、出かける"),
            )
