# -*- coding: utf-8 -*-
'''
Episode 8-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$wilsonの手記"


# NOTE: outlines
ABSTRACT = """
※という訳で、記述者は本物の$wilsonだった。
作品の締めくくりに当たるエピローグを書き終えたところで$maryたちに呼ばれる。$maryが初めて焼いたというケーキなるお菓子を食べようというのだ。
$wilsonはそれを口にして昔暮らしていた世界を懐かしく思うが、そこに新たな問題を抱えた依頼人がやってきた。だがまたそれは次の物語。
"""


def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("小説の記述者は本物の$wilsonだった"),
            w.plot_turnpoint("実は偽物の$wilsonが自宅を使っていることに気づいていた、と告白する"),
            w.plot_develop("肉屋$nowlisとして市場で働きつつ、動向を監視していた。その間に$sherlockという人物についてもある程度調べていたことも語る"),
            w.plot_turnpoint("$maryがケーキを焼いたと呼びに来る"),
            w.plot_resolve("実は$wilsonはずっと本物の$heroの血を持つ人物を探していた。こんな形で見つかるとは思わなかったと書き加え、ケーキを食べに合流する"),
            outline=ABSTRACT)

