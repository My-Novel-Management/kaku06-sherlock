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
            "不穏な空気",
            w.plot_note("あれから一ヶ月。$maryたちのいる暮らしにも慣れた"),
            w.plot_note("$limeが意外と料理を覚えるのが早くて、二人でわいわいやっている"),
            w.plot_note("$sherlockは新聞を見ながらうなっている"),
            w.plot_note("最近さまざまな、不可解な犯罪が増えている"),
            w.plot_note("そこに一通の書簡が届く"),
            # TODO
            "$sherlockが穴に落ちた",
            w.plot_note("彼が事前に出した手紙が届く"),
            w.plot_note("そこにはこの手紙が届いたということは自分が亡くなった可能性があると書かれている"),
            w.plot_note("$sherlockは自分を殺したのは$morianoで、彼が亡くなったときには新聞のある部分に知らせが出るとある"),
            w.plot_note("$wilsonがその知らせを見つける"),
            w.plot_note("$sherlockからの手紙には$morianoが倒れても彼の意志を貫くと"),
            w.plot_note("それに気になるところがあり、自分が知っている人間にその情報を探らせているともあった"),
            "まだ生きているはず",
            w.plot_note("$sherlockが本当になくなったとは信じたくない$maryは、探すと言い出して街に出ていく"),
            )


