# -*- coding: utf-8 -*-
'''
Episode: 0-1 "読者のための諸注意"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# Scenes
# NOTE

# NOTE: outlines
ABSTRACT = """
※記述者視点となる。本作は全ての事件に一応の解決が見られてから伝聞により情報を補完し、小説として再構成されたことが注記される。
"""


# Episode
def main(w: World):
    return w.episode("読者のための諸注意",
            # NOTE
            w.plot_setup("ある記述者がこの物語を執筆している"),
            w.plot_turnpoint("$sherlockに出会ったことが全てのきっかけだと書いている"),
            w.plot_develop("どういう規則に従って書かれているか等の注意事項について説明する記述者"),
            w.plot_turnpoint("部屋に誰か（$mary）が入室してきて、記述者に早く来いと呼び出しをする"),
            w.plot_resolve("記述者は振り返り、こういったこともかつてはなかったと感慨深く思いながら、物語の続きを書き始める"),
            w.plot_note("この物語は$sherlockという男と、彼が解決したいくつかの事件に関して書かれている"),
            w.plot_note("つまり既に事後に書かれたものである"),
            w.plot_note("私を含めて全て原則三人称で記述される"),
            w.plot_note("私が$sherlockという男に出会わなかったらこの物語は書かれなかっただろう"),
            w.plot_note("私が誰かということはおいおい分かると思う"),
            w.plot_note("足りない情報を伝聞により補完し、小説風に加工して読みやすくしていることを断っておく"),
            w.plot_note("現実の事件のいくつかはバラバラに起こり、単一の視点ではその関係性が見えないこともしばしばである"),
            w.plot_note("そこに、ドアがノックされる"),
            w.plot_note("「ケーキ焼けたで？」と、小柄な娘が恥ずかしそうに覗き込む"),
            w.plot_note("私はすぐ行くと答えて、筆を置く"),
            w.plot_note("物語は私が$sherlockに出会う前から始まる。物語を始めよう"),
            outline=ABSTRACT)

