# -*- coding: utf-8 -*-
'''
Chapter "エピローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import Market
from scenes import ReadingRoom
from scenes import SherlockHouse
from scenes import WilsonHouse


# Episode
# NOTE
#   .全ての顛末＞本物の$wilsonが帰ってくる
#   .探偵の誕生＞探偵社を設立
#   .$wilsonの手記＞新しい仕事が舞い込んでくる

# NOTE: outlines
ABSTRACT = """
偽$wilsonの死去により全ての事件は幕を下ろしたかに思えた。
家を失った$sherlockはひとまず$wilsonの家を借りることにする。
だがそこに$wilsonの家の大家がきて、家賃が半年滞納されていると催促してくる。
お金がなくどうしようもできない$sherlockたちだったが、そこに本物の$wilsonが帰ってきた。
事情を話すと$wilsonは自分が$sherlockの活躍を小説にして、それを新聞小説として掲載してもらおうと提案した。
こうしてこの作品は書かれたのだ、というネタばらしがある。
"""
OUTLINES = [
"""
偽$wilsonである$zeronの自殺により$boss復活の儀式にかかわる一連の事件に一応の決着がついた。
だが$sherlockと$mary、$limeは住む場所を失い、仕方なく$wilsonの家でしばらく暮らすことになる。しかし大家が家賃滞納を理由に家から出ていけと言ってきた。
そこに本物の$wilsonが帰ってきて、$sherlockたちは彼に一連の事件と自分たちがここにいる事情を語った。
$wilsonは$sherlockの活躍を小説として新聞に掲載することで家賃分を何とかしようと提案する。
これを承諾し、ここに$sherlock探偵社が誕生した。
""",
"""
※という訳で、記述者は本物の$wilsonだった。
作品の締めくくりに当たるエピローグを書き終えたところで$maryたちに呼ばれる。$maryが初めて焼いたというケーキなるお菓子を食べようというのだ。
$wilsonはそれを口にして昔暮らしていた世界を懐かしく思うが、そこに新たな問題を抱えた依頼人がやってきた。だがまたそれは次の物語。
""",
        ]

# NOTE: charas
#   ・本物の$wilson（一応ここが初出。だが$nowlisとして市場で出てきた男でもある。勘のいい読者だけ分かるように

# NOTE: stages

# NOTE: items

# NOTE: case
#   ・$wilsonすり替わり事件　→本物の$wilsonに長旅をさせ、その間になりすました


def total_the_end(w: World):
    return w.episode("全ての顛末",
            # NOTE
            w.plot_setup(""),
            w.plot_develop(""),
            w.plot_resolve(""),
            outline=OUTLINES[0])


def wilsons_papers(w: World):
    return w.episode("$wilsonの手記",
            # NOTE
            w.plot_setup(""),
            w.plot_develop(""),
            w.plot_resolve(""),
            outline=OUTLINES[-1])


# Chapter
def main(w: World):
    return w.chapter(TITLES[-1],
            total_the_end(w),
            wilsons_papers(w),
            w.symbol("（了）"),
            outline=ABSTRACT)


