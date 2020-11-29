# -*- coding: utf-8 -*-
'''
Stage: "シュタインの家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   モリアーティを調べていた過去の友人の大学教授の男の家


## scenes
def case_of_house(w: World):
    return w.scene("事件の起こった家で",
            w.plot_note("$restradeと合流し、事件についての情報をもらう"),
            w.plot_note("現場にはＭの文字が書き残されていた"),
            )


def restrade_meets(w: World):
    return w.scene("$restradeと会う",
            w.plot_note("$sherlockは$morianoだと語る"),
            w.plot_note("$restradeですら耳にしたことがなかったその男のことを、$sherlockは友人のように仔細に話してみせる"),
            )


def about_moriano(w: World):
    return w.scene("$morianoについて",
            w.plot_note("$morianoは教育者の家庭に生まれた"),
            w.plot_note("幼い頃に神童とよばれ、あらゆる学問について素晴らしい成績を収めたが、彼が大学で興味を持ったのは人間そのものだった"),
            w.plot_note("大学時代に書いた論文は一本で、それは「人間と犯罪について」というものだ"),
            w.plot_note("統計手法を用いて実際にあった事件から犯人や被害者の心理、行動が細かく観察されている"),
            w.plot_note("今でも警察が犯罪心理学の基礎として流用しているものの多くがここから派生したもので、犯罪学の父と呼ばれる存在だと"),
            w.plot_note("しかしある時、急に大学をやめ、世間から遠ざかってしまった"),
            w.plot_note("個人の研究所を立ち上げて個人的な研究をしているという噂はあるが、研究成果を発表したりはしていない"),
            w.plot_note("その$morianoと連絡を取り合っていた形跡がある男が殺されたのだ、それも密室で、怪死した"),
            w.plot_note("$sherlockは全ての事件は$morianoにつながると言い切った"),
            )
