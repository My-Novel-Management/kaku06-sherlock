# -*- coding: utf-8 -*-
'''
Episode 3-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "鎧騎士の正体"


# NOTE: outlines
ABSTRACT = """
$sherlockにより$limeの疑いが晴れた。
しかし$limeは質屋オーナー夫婦に悪いと、家を出る。
孤独になった$limeを、$maryが再び拾って家へと連れてきた。
$maryは自分も働くから何とか置いてもらえないかと頼む。$sherlockは思案するが。
そこで$limeはある告白を始めた。自分が何故こういう状況になっているのか。
$limeは自分が失踪中の第二王女だと告白した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("強盗団が全員死んだことと$sherlockの調査により$limeの疑いが晴れた"),
            w.plot_turnpoint("$limeが釈放されたと連絡を受ける"),
            w.plot_develop("無実となった$limeだったが迷惑をかけたとオーナー夫婦の許を去った。だが路上でどうしようと困っていて、再び$maryに拾われる"),
            w.plot_turnpoint("$maryが$limeを連れてくる"),
            w.plot_resolve("$limeは$sherlockたちに自分がどうしてこうなっているのか、事情を話す"),
            w.plot_turnpoint("$limeは$sherlockたちに自分は失踪中の第二王女だと語った"),
            outline=ABSTRACT)

