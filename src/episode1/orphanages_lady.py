# -*- coding: utf-8 -*-
'''
Episode 1-4: "孤児院の女"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Scenes
# NOTE

# NOTE: outlines
ABSTRACT = """
警察はそのことにより$ailyが何者かにより他殺されたのではないかという話になった。
$sherlockは再度孤児院を訪れる。そこで$ailyと当時仲良かった女性の存在を知る。
彼女は孤児院を抜けてから何をしているか分からない。
事件は容疑者が見つからないまま迷宮入りになりそうだった。
$sherlockは彼女にプレゼントしたという$royalswordの所在について考えていた。
$adel経由で王子と出会い、そこで再度$ailyについての情報を聞く。完全に別人だと判断した$sherlock。
再度孤児院を訪れ、教師に尋ねる。「あなたがオペラ歌手の$ailyですね」と。
"""


# Episode
def main(w: World):
    return w.episode("孤児院の女",
            # NOTE
            w.plot_setup("$sherlockは$ailyについて聞く為に王子と出会う"),
            w.plot_turnpoint("王子は一度だけ$ailyの自宅を訪ねたが、その時は無視されたと語る"),
            w.plot_develop("一旦$sherlockは$ailyについての情報を整理し、知人の鑑識からも情報を得る"),
            w.plot_turnpoint("$ailyが二人いたことが判明する"),
            w.plot_resolve("$sherlockは再度孤児院を訪ねて女教師に「あなたが$ailyですね」と言った"),
            w.plot_turnpoint("更に$ailyが巷で噂になっている怪盗$jackだと言った"),
            outline=ABSTRACT)

