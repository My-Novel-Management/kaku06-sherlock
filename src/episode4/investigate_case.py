# -*- coding: utf-8 -*-
'''
Episode 4-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World



# DEFINE
TITLE = "事件捜査"


# NOTE: outlines
ABSTRACT = """
$limeは$maryが戻ってこないことに気づき、市場に探しに出かける。$ignesからの情報でどうやらガチョウクラブに潜入捜査をしていたことが判明する。
一旦$sherlockに話そうとするが外出中で、$wilsonに手伝ってもらってガチョウクラブに向かうことに。
外出中の$sherlockは彼女が育った孤児院にきていた。そこで教師から彼女が$ajinであることを知らされる。ここに暮らす多くが$ajinだった。
今も毎月彼女から仕送りが届いているらしい。
他にもここの卒業生で仕送りをしてくれている子は多いが、最近になって多額の寄付があったのが、今手広く事業を手がけている男だった。その男からこの前ガチョウを貰ったと喜んでいた。
そのガチョウがガチョウクラブ経由と知る$sherlock。
ガチョウクラブの男たちに捕まえられた$maryは、$animalだとバレて、売り飛ばされそうになっていた。
そこにあの女性が現れ、彼女を助けると言う。その女性$jackだった（別名を名乗るが）。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$jackと$blue_stoneの関係があるという情報を得た$sherlockは、一旦家に戻るが$maryがいない"),
            w.plot_turnpoint("$maryが戻ってこないと$limeに言われた"),
            w.plot_develop("$maryの残した書き置きを手がかりに$sherlockと$limeはガチョウクラブに向かう。だが$maryは見ていないと言われた"),
            w.plot_turnpoint("被害者宅を調べていて$mouraの夫がガチョウクラブ会員であると判明した"),
            w.plot_resolve("$sherlockはガチョウクラブと$mouraの夫周辺を改めて調査する一方で$ignesたちに$mary捜索を依頼した"),
            w.plot_turnpoint("売り飛ばされそうになっている$maryの前に謎の女性（$jack）が現れた"),
            outline=ABSTRACT)

