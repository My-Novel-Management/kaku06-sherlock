# -*- coding: utf-8 -*-
'''
Episode 6-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$morianoについて"


# NOTE: outlines
ABSTRACT = """
$sherlockはすぐにアリバイを語り、自分の容疑を晴らす。
そもそも$stein教授とは王立図書館で出会った。彼の論文は$sherlockもよく目を通していて、教授から古代の知識について色々と教わっていたと話す。
そして$steinは$morianoの友人だと言い出す。
$morianoについて誰も知らなかった。
$sherlockは$morianoについて語る。この都市の多くの犯罪の糸が$morianoに繋がっていた。$sherlockは珍しく自分の命に代えても$morianoを倒すと言う。
そこに$maryが連れてきた老人こそが$morianoだった
"""

# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$patsonから$stein元教授が自宅で密室状態で殺されていたことを知らされる"),
            w.plot_turnpoint("$sherlockは自分と$stein教授の付き合いについて告白する"),
            w.plot_develop("$sherlockは$stein教授の研究で$boss復活の儀式という闇の技法が存在し、それを実際に行おうという集まりがあると示唆する。その中心的存在が$morianoだった"),
            w.plot_turnpoint("$sherlockは$morianoこそが今までの全ての事件の裏で糸を引いていた存在だと断言する"),
            w.plot_resolve("$sherlockは情報を集めて$morianoを何としても刑務所送りにしなければならないと、いつもにはない雰囲気で言う"),
            w.plot_turnpoint("$maryが連れてきた老紳士こそが$morianoだった"),
            outline=ABSTRACT)

