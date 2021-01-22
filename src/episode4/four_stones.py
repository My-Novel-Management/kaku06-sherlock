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
            w.plot_note("薄っすらと日が登り、$sherlockが$wilsonのところにやってくる"),
            w.plot_note("$sherlockは野暮用が片付いたと言う"),
            w.plot_note("$wilsonの方は何の変化もなく、おそらくここではないどこかに監禁されているのではないか、と"),
            w.plot_note("と、建物の前に誰か現れる。$adelだった"),
            w.plot_note("彼女はこっそりと建物に忍び込む。明らかに不法侵入だった"),
            w.plot_note("$wilsonは$sherlockに彼女が一体何者なのか尋ねる"),
            w.plot_note("よくは知らないが$wilsonの同業者だろうと"),
            w.plot_note("しばらくすると建物から出てくる$adel。その手に何か資料を持っていた"),
            w.plot_note("そこに出ていって声をかける$sherlock"),
            w.plot_note("$adelは無視して行ってしまおうとしたが、$sherlockが自分の知人がここの連中に捕まっている可能性を言うと"),
            w.plot_note("$adelは自分もそういう内容の指示を受けて、改めて調査に訪れたと語る"),
            w.plot_note("ただ監禁されているならここではなく、ハーバーの方だろうと"),
            w.plot_note("幹部が保持している船が密会の会場になっていると告げた"),
            #
            w.plot_note("$maryは謎の女性と話していた"),
            w.plot_note("彼女は$ailyと名乗り、自分は忘れ物を取りに来たら捕まってしまったと語る"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

