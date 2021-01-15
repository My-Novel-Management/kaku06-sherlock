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
            outline=ABSTRACT)

