# -*- coding: utf-8 -*-
'''
Stage: "博物館"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   王室の貴重品なども収蔵されている王立博物館
#   シティ（旧市内）の端にあり、現在改装中
#   [展示室A][展示室B][展示室C][展示室D]
#   [展示室（大ホール）]
#   [玄関ホール]


## scenes
def alibi_proof(w: World):
    return w.scene("アリバイの証明",
            w.plot_note("銀行へとやってきた$sherlockはそこにいた$restradeにそのアリバイの証拠を教える"),
            w.plot_note("前日に鍵が壊れて、誰も質屋に入れなくなっていたのだった"),
            )

