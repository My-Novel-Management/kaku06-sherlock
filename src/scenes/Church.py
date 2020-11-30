# -*- coding: utf-8 -*-
'''
Stage: "教会"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   教会については、こちらを利用する


## scenes
def mystery_cult(w: World):
    return w.scene("神秘教団",
            w.plot_note("$sherlockは彼女に接触しその技法を教えた$cultXのことをマークした"),
            w.plot_note("そこに情報がもたらされる"),
            )


def cult_facility(w: World):
    return w.scene("教団施設",
            w.plot_note("$sherlockとともに宗教団体の施設を探す"),
            )


def basement_hall(w: World):
    return w.scene("地下のホールで",
            w.plot_note("その地下で儀式が行われた跡を発見する"),
            w.plot_note("儀式が失敗したことはわかったが、$wilsonはいなかった"),
            )


def unexpected_end(w: World):
    return w.scene("意外な最後",
            w.plot_note("$sherlockは$maryたちに偽$wilsonが$bossの復活のために全てを準備していたのだと語る"),
            w.plot_note("そして儀式に不可欠だったのが$heroの心臓であり、それを探してずっと$heroの血縁の人間を殺しまわっていたと"),
            w.plot_note("どの心臓も合わなかったらしく、最後に白羽の矢がたったのが$sherlockで、ダミーの$morianoにより誘い出して殺そうとしたと"),
            w.plot_note("しかし全てが失敗に終わり、$stoneは粉々になって発見された"),
            w.plot_note("$wilsonは機会を伺って潜伏しているだろうが、また自分を殺しにくると伝える"),
            w.plot_note("だが警察は$wilsonの遺体を空き家で見つける"),
            )
