# -*- coding: utf-8 -*-
'''
Episode 7-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "空き家の冒険"


# NOTE: outlines
ABSTRACT = """
ホームレスからスラム街の空き家に$sherlockが出没すると言われ、そこを監視する$maryたち。
夜になると外見や風貌が$sherlockに似た男がその空き家に入り、明かりが灯った。男はいつも$sherlockがしていたように本を読んでいた。
そこに来客がある。二人はしばらく何か言い争った後で、突然明かりが消えた。
しばらく待っても動きがなく、$maryたちは調べるために空き家に突入する。
そこで殺された男の遺体を発見し、警察に通報した。
警察の事情聴取を受けた$maryたち。$maryはそこで$patsonから警察は$sherlockを容疑者として疑っている情報を得る。
$maryは単身で、$sherlockの容疑を晴らすために空き家の調査を行う。
すると、そこで抜け道を発見した。
$maryが抜け道を進むと廃工場に出た。そこで今までに失踪した人間たちの遺体を発見する。だがそこで何者かによって意識を失った。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockが現れるという空き家を監視していた$maryたちは、そこで争いがあるのを目撃して、中を調査する"),
            w.plot_turnpoint("空き家で男の遺体を発見する"),
            w.plot_develop("警察に連絡し、$maryたちは事情聴取を受ける。そこで$sherlock生存情報を得たことなどを話す$mary"),
            w.plot_turnpoint("$maryは$patsonから$sherlockを容疑者に考えていることを教わる"),
            w.plot_resolve("$maryは単独で空き家を調査に向かう"),
            w.plot_turnpoint("$maryは抜け道を見つけた"),
            outline=ABSTRACT)

