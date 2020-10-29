# -*- coding: utf-8 -*-
'''
Chapter "最後の事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[6],
            "隣国マイリンゲンのライヘンバッハ",
            w.plot_setup("今までの事件の黒幕として$morianoが浮かび上がる"),
            w.plot_setup("$sherlockは一人でいるときに$morianoと対峙し、忠告を受ける"),
            w.plot_turnpoint("家が放火された"),
            w.plot_develop("それぞれ別々の仮宿を取った"),
            w.plot_develop("$maryや$limeが襲われる"),
            w.plot_develop("$wilsonまでも負傷し、安全が脅かされる"),
            w.plot_turnpoint("$sherlockは単身、$morianoとの対決に向かった"),
            w.plot_resolve("湖畔の屋敷で待っていた$morianoと対峙する"),
            w.plot_resolve("$morianoは全てを自供する"),
            w.plot_resolve("闇の世界について語り、$bossを復活させるためにあるものが必要だったと"),
            w.plot_resolve("全てが仕組まれていたことだと分かりながらここにやってきた$sherlock"),
            w.plot_resolve("しかし屋敷に続く橋が爆破され、警官隊は来られなかった"),
            w.plot_resolve("$sherlockが$morianoと闇の穴に落ちたと目撃証言が入った"),
            )


