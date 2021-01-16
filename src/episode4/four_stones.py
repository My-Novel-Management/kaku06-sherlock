# -*- coding: utf-8 -*-
'''
Episode 4-5
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World



# DEFINE
TITLE = "四つの$stone"


# NOTE: outlines
ABSTRACT = """
殺人事件が解決され、また$maryも無事に戻ってきた。
ただ$blue_stoneが何故一緒にあったのか、その謎だけが$sherlockには引っかかっていた。
後日$maryを助けてくれたという女性と出会う。彼女が$jackだとすぐに分かり、$sherlockは何故戻ってきたのか尋ねる。
どうやら預けていた$blue_stoneが誰かに盗まれたと分かり、取り戻しにきたらしい。どこからどう回ったのか、殺害された$moura夫人の手に渡り、男が盗んだが、凶器と一緒にガチョウに隠してしまったということだった。
$jackは何者かが$stoneを集めようとしていると警告する。四つの$stoneを集めて何をしようとしているのかはよく分からないが、それは今の世の中にとってよくないことだと$jackは考えている。
その目的解明と何かやろうとしていることの阻止を託され、$jackから$blue_stoneを預けられた
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("事件が解決し、ガチョウクラブにも捜査の手が入った。$maryも$jackにより救出された"),
            w.plot_turnpoint("$jackは$sherlockに話があると呼び出した"),
            w.plot_develop("$jackは$stoneと裏社会の動きについて$sherlockに教える"),
            w.plot_turnpoint("自分が盗んだ$red_stoneは何者かに盗まれたと告白した"),
            w.plot_resolve("$jackは$sherlockに$blue_stoneを託し、裏世界で動いている何者かの企みを阻止してほしいと依頼した"),
            outline=ABSTRACT)

