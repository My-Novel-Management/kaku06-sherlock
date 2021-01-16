# -*- coding: utf-8 -*-
'''
Episode 6-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "古代の研究者"


# NOTE: outlines
ABSTRACT = """
孤島事件後から$sherlockは頻繁に外に出かけるようになっていた。
$maryたちは少し退屈さを感じつつも、自分の今後の身の振り方について考える時間を持つ良い機会だった。
一方、元大学教授が謎の死を遂げた。その容疑者の一人として$sherlockが浮上する。
$maryは市場への買い物の帰り道で、ふさぎ込んでいる老紳士と遭遇し、彼を助ける。
やってきた$patsonは何かの資料を調べるのに必死になっている$sherlockに、$stein元教授殺人事件について事情をきかせろと迫る。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("孤島事件後、$sherlockは頻繁に外出し何かを調べていて$maryは少し寂しい思いをしていた"),
            w.plot_turnpoint("$maryは市場で$moriano犯罪研究所のチラシを拾う"),
            w.plot_develop("$maryは自分が$ajinであることに悩み、市場の知り合いなどに相談するがなかなかすっきりとはしない"),
            w.plot_turnpoint("$maryは道端でふさぎ込んでいた老人を助ける"),
            w.plot_resolve("$sherlockは$wilsonに犯罪研究所の$morianoという男を知っているか尋ね、その男について語っていた"),
            w.plot_turnpoint("$patsonが現れて$sherlockを容疑者として事情聴取すると言い出した"),
            outline=ABSTRACT)

