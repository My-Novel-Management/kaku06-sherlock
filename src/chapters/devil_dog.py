# -*- coding: utf-8 -*-
'''
Chapter "魔獣"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[5],
            "舞台は荒野ダートムア",
            w.plot_setup("その荒野では魔獣の伝説があった"),
            w.plot_setup("実際に魔獣の仕業と考えられる猟奇殺人が発生する"),
            w.plot_setup("$sherlockのところにその捜査依頼が舞い込む"),
            w.plot_turnpoint("だが別の用事があり$sherlockが行けないと言い出す"),
            w.plot_develop("$maryたちで事件調査に赴く"),
            w.plot_develop("その家は不遇な死が続いていた"),
            w.plot_develop("情報を集めていく中で本物の魔獣に襲われそうになる"),
            w.plot_turnpoint("$maryが魔獣に殺されそうになる"),
            w.plot_resolve("$sherlockがかけつけ、魔獣を追い払う"),
            w.plot_resolve("$maryたちが集めた情報をもとに$sherlockは事件の真相に至る"),
            w.plot_resolve("降霊術で魔獣を呼び出したが、それはただ愛犬を蘇らせたいという女の気持ちだった"),
            w.plot_resolve("魔獣に餌を与える必要があり、仕方なく伝説になぞらえて殺人させたのだ"),
            w.plot_resolve("魔獣は退治され、女は逮捕された"),
            w.plot_resolve("その女に降霊術（偽物）を教えたのはある宗教団体の人間だった"),
            )


