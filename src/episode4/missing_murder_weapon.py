# -*- coding: utf-8 -*-
'''
Episode 4-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "凶器のない殺人"


# NOTE: outlines
ABSTRACT = """
何かの事件に関連していると$sherlockが警察に届ける。担当の$restradeがやってきて、凶器が見つからない事件のものの疑いがあると教えてくれる。
事件は資産家の$moura夫人の家から所蔵していたコレクションが数点盗まれた。強盗殺人だったが、凶器が見つからず、ずっと探していたらしい。
ナイフは鑑識に回し、その間に$sherlockに事件解決をしてほしいと依頼する$restrade。
現場に向かった$sherlockだったが、一方$maryは市場の知人、肉屋の$nowlisが容疑者候補に上がっていると聞いて、何とか力になれないかと独自に調査に乗り出す。
$maryは市場でガチョウの入手先を聞き、卸業者を当たり、その先にガチョウクラブというものが存在していると知る。
一方、以前に$sherlockが開発した指紋検出装置により、一緒に入っていた$blue_stoneから$jackの指紋が検出され、一気に$jackが容疑者に躍り出た。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockはナイフと$blue_stoneについて警察に届けると共に情報を調べる"),
            w.plot_turnpoint("$restradeがやってきてナイフがある事件に関係している可能性があると言った"),
            w.plot_develop("資産家の夫人が謎の死を遂げ、その凶器が見つからなかったが、ガチョウから出てきたナイフに付着していた血液が一致した。$sherlockは知人に$blue_stoneについての鑑定を依頼する"),
            w.plot_turnpoint("$maryが単独で事件捜査していると$limeから聞く"),
            w.plot_resolve("$maryは市場の知人のツテを使ってガチョウの行方を追いかけた"),
            w.plot_turnpoint("$maryは卸先の男からガチョウクラブについて教わる"),
            outline=ABSTRACT)

