# -*- coding: utf-8 -*-
'''
Stage: "山小屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   ウィルソン（偽）がしんでいた山小屋


# Scenes
## in EmptyHouse
def his_dead(w: World):
    mary, shal, lime = w.get("mary"), w.get("sherlock"), w.get("lime")
    wil = w.get("wilson")
    rest = w.get("restrade")
    return w.scene("彼は死んでいた",
            w.change_camera("sherlock"),
            w.change_stage("MountCottage"),
            w.plot_note("同じ手法だったが、それは遠隔操作$gunによる自殺だった"),
            shal.be(),
            shal.do("現場にいった説明をする$S"),
            shal.do("連絡を受けて$restradeたちと一緒にその山小屋に向かう"),
            shal.do("国境を超えた先にある山"),
            shal.do("先行部隊が取り囲み、逃げないように見張っていた"),
            shal.do("何も動きがなく、$Sがもしやと思い、突入するように要請し、扉を破って入った"),
            shal.do(""),
            )

