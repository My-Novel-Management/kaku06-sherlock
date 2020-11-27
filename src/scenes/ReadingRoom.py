# -*- coding: utf-8 -*-
'''
Stage: "書斎"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   後のウィルソン（本物）が使っている書斎
#   場所は現在のウィルソンの家とは異なり、隠遁生活中のコテージの中


## scenes
def note_for_thisnovel(w: World):
    return w.scene("作品のための注意書き",
            w.change_stage("ReadingRoom"),
            w.change_time("night"),
            w.plot_note("本作品は全て三人称で記述される"),
            w.plot_note("記述者＝私により後から整理され、書かれたもの"),
            w.plot_note("聞いた時が前後しても、読んでいくのにいいように並べ替えてある"),
            w.plot_note("本作は$sherlockという男を中心に巻き起こった事件について書いた、伝記的作品である"),
            )

