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
            shal.do("山小屋の中には$wilsonだけがいて、ベッドの上で亡くなっていた"),
            shal.do("毒殺と見られる"),
            shal.do("小屋は特に使われた形跡はなく、荷物も何一つなかった"),
            shal.do("$sherlockは彼が持ち逃げしたと思われる、儀式に一番大事だったものがどこかにあるはずだと探したが、なかった"),
            shal.do("ただテーブルの上には彼が犯行に使ったと思われる改造$gunが一つ、中に弾がない状態で放置されていた"),
            shal.do("銃殺なのか毒殺なのか、当初は意見が別れたが、あとで自分で毒を飲んだが、その後に誰かによって$gunで撃たれたらしいと判明する"),
            shal.do("$Sは誰かの手による殺人を訴えたが、警察は自殺の線が濃厚だと、意見を受け入れなかった"),
            )

