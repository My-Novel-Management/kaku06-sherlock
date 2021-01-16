# -*- coding: utf-8 -*-
'''
Episode 4-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "市場とガチョウ"


# NOTE: outlines
ABSTRACT = """
$limeが同居するようになり、彼女も家事を手伝うようになっていた。だが彼女は$maryと違い、料理も上手で掃除や洗濯も手際よくこなし、$maryは買い物だけが自分の役割になってしまった。そのことについて居場所を失ったような気になり、市場で仲良くなった肉屋の$nowlisに相談する。
一方$sherlockは$wilsonから頼まれていた第二王女失踪の調査が、$limeを見つけたことで一旦解決した。けれど連続失踪事件、および、最近明らかになった連続猟奇殺人事件について独自に調査を進めていた。
$wilsonは$sherlockと$limeから頼まれて、もうしばらく第二王女が見つかったことは内緒にしておくことにした、と言ったが、その裏で王室執務官の$mikelと出会っていた。何とか無事なこと、安全は確保していることを伝えると、$mikelの方で色々と考えると言われた。
$maryは$nowlisから沢山貰ったからとガチョウを一羽まるまるプレゼントしてもらえた。
喜んでそれを持ち帰り、$limeに捌いてもらうとそのガチョウの中からナイフと$blue_stoneが出てきた
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$limeが一緒に暮らすようになり、$maryは自分の役割を取られたような気分になっていた"),
            w.plot_turnpoint("$maryは逃げるように市場に買い出しに行く"),
            w.plot_develop("$sherlockは$wilsonの依頼を終えても失踪事件について調査を続けていた。あまり構ってくれないと憤慨する$maryは市場で仲良くなった肉屋の$nowlisに相談する"),
            w.plot_turnpoint("$nowlisからガチョウをもらう"),
            w.plot_resolve("$maryは自分も役に立つとガチョウを自慢する"),
            w.plot_turnpoint("だが$limeに捌いてもらったガチョウからはナイフと$blue_stoneが出てきた"),
            outline=ABSTRACT)

