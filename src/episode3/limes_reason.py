# -*- coding: utf-8 -*-
'''
Episode 3-5
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$limeの事情"


# NOTE: outlines
ABSTRACT = """
第二王女と告白した$limeは、事情があり、王室ではずっと肩身の狭い思いをしていて、逃げ出したいと思っていた。
ちょうどそこに泥棒が入ってきたので誘拐してもらった。けれど売り飛ばされる相談が聞こえて途中で怖くなり、物置にあった鎧を着て逃げ出したのだが、どうやら鎧に呪いがかかっていたようでしゃべれなくなり、途方にくれていたところを質屋夫婦に拾ってもらった。
出ていかなくていいと言ってはくれたが迷惑になるので、出てきたと。
$sherlockは$limeを連れ出し、知人の神官のところで呪いを解いてもらう。
$limeは事情を語った上で、$sherlockに王室に戻らなくて済むようにしばらくここで生活させてほしいと頼む。渋った$sherlockだったが王室の人間にバレたらその時は素直に戻るという条件付きで、棲まわせることにした。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("第二王女だと語った$limeは自分がどうしてこうなっているのかという事情を$sherlockたちに話した"),
            w.plot_turnpoint("$limeは泥棒に自分から誘拐してくださいと頼んだ、と語る"),
            w.plot_develop("$limeは誘拐された先で売り飛ばされる計画を聞いて、逃げ出す時に物置にあったこの呪いの鎧を着てしまい、困っていたところを質屋オーナー夫婦に拾われたと語る"),
            w.plot_turnpoint("$sherlockは$limeの呪いを知人の神官に解いてもらう"),
            w.plot_resolve("$limeは王室に戻りたくないのでしばらくここで置いてもらえないかと頼み込んだ"),
            w.plot_note("$shelrockの前に現れた$limeは、なんと女性だった"),
            w.plot_note("$limeはまず「ありがとうございます」と丁寧な口調で言う"),
            w.plot_note("$maryは「驚いたでしょ」と何故かうれしげ"),
            w.plot_note("$limeは先にオーナー夫婦宅にいき、これ以上は世話になれないことを説明し、家を出る約束をしてきたという"),
            w.plot_note("そこで$sherlockにしばらく置いてもらいたい、と"),
            w.plot_note("赤鎧クラブのお金はオーナー夫婦に受け取ってもらえなかったので、それを元手にしてどこか住み込みで働ける場所を見つけると言う"),
            w.plot_note("だが$sherlockは$limeに、その前にどういう事情でこうなったのか話してほしいと言う"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

