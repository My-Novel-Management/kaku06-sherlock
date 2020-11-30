# -*- coding: utf-8 -*-
'''
Stage: "廃屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   廃墟や廃屋はここを使う


## scenes
def awaking_mary(w: World):
    return w.scene("目覚めた$mary",
            w.plot_note("$maryは爆弾が仕掛けられた部屋に閉じ込められていた"),
            w.plot_note("爆弾はダミーだった"),
            w.plot_note("部屋から出られなくなった$maryと$lime、探偵団たち"),
            )


def escape_from_danger(w: World):
    return w.scene("危険からの脱出",
            w.plot_note("$sherlockの言葉を思い出して、$maryは脱出法を見つける"),
            w.plot_note("ダミーとして用意していた爆弾を使い、扉を爆破して何とか抜け出す$maryたち"),
            )


