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
            outline=ABSTRACT)

