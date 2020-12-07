# -*- coding: utf-8 -*-
'''
Stage: "警察署"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   交番規模のものから、警察署本部までこちらで


# alias
STATION = "PoliceStation"
OFFICE = "PoliceOffice"
INTERROGATION = "PoliceInterrogationRoom"


# Scenes
## in Empty House
def interrogation(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    pat = w.get("patson")
    rest = w.get("restrade")
    return w.scene("事情聴取",
            w.change_camera("mary"),
            w.change_stage(INTERROGATION),
            w.plot_note("警察の事情聴取を受けた$maryたち"),
            mary.be("事情聴取を受けている$S"),
            pat.be(),
            pat.talk("もう一度聞くけど、いいかい？"),
            mary.talk("何度聞かれても同じことやもん", "一度聞いたら覚えられへんのん、$k_pat"),
            pat.talk("事務手続きだから我慢してよ", "$meだって何もやりたくてやってるんじゃなくて、人が一人亡くなったれっきとした事件だからね"),
            mary.do("$Sは再度、自分たちの状況を話す"),
            # TODO
            )

