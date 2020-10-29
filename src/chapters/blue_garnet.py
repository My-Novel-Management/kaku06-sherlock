# -*- coding: utf-8 -*-
'''
Chapter "青いガーネット"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[4],
            w.plot_setup("最近巷で怪盗$jackの話を聞かなくなっていた"),
            w.plot_setup("$maryが仲良くなった市場の男からニワトリをもらってくる"),
            w.plot_turnpoint("そのニワトリを捌くと中から宝石が出てくる"),
            w.plot_develop("その宝石はどうやら$ailyに盗まれた宝剣についていたものと同じだと分かる"),
            w.plot_develop("$sherlockは$ailyの消息を改めて探る"),
            w.plot_develop("謎の女性の猟奇殺人が発生するが、それが怪盗$jackの死体と言われる"),
            w.plot_turnpoint("$sherlockのもとに$ailyからの手紙が届く"),
            w.plot_resolve("その暗号を解読し、$sherlockは$ailyに会いに向かう"),
            w.plot_resolve("宝石がある儀式に必要とされ、自分が狙われたから預かってもらったと$jackは告白した"),
            w.plot_resolve("$jackは改めて$sherlockに全ての糸を引く黒幕の存在を調べて、その情報が欲しいと依頼した"),
            )


