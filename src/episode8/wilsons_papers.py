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
            w.plot_note("という訳で、ここまで書いてきたのは本物の$wilsonだった"),
            w.plot_note("色々と補足しておくと、実際に$wilsonは最後の場面以外にも登場している"),
            w.plot_note("一つは肉屋の$nowlisとして、だ"),
            w.plot_note("知人に頼まれ、肉屋をしばらくやっていたのだ"),
            w.plot_note("そもそも自分の家に出入りしている謎の男がいることには気づいていた"),
            w.plot_note("どうなるか動向を見守っていた"),
            w.plot_note("また$maryと知り合い、またそこから$sherlockなども知るに至った"),
            w.plot_note("実は$mikelの依頼で$heroの血を引く人間を探していたが、偽物の方が早くに見つけてしまった"),
            w.plot_note("なぜ本物の$heroが必要になったのかは、また別の物語で語る機会があるだろう。その時を楽しみにしてもらいたい"),
            w.plot_note("これにて$boss復活をめぐる一連の事件は本当に幕を下ろす"),
            w.plot_note("しかしまた別の物語がすぐに彼らを呼んでいる"),
            w.plot_note("それについても近いうちに書くことになるだろう"),
            w.plot_note("原稿を書き終えると、ちょうど$maryが呼びに来る"),
            w.plot_note("リビングには彼女がやいたカップケーキが準備されていた"),
            w.plot_note("懐かしい"),
            w.plot_note("以前いた世界でよく口にしていたことを、ふと思い出した"),
            w.plot_note("この世界でまた口にできて、嬉しい"),
            w.plot_note("それについてもまた語ることがあるだろう"),
            w.plot_note("$sherlockが言っていた"),
            w.plot_note("謎はすべて解いてしまったらただの事実しか残らない"),
            w.plot_note("少しくらいは残しておいた方が、謎も料理も楽しめるというものだと"),
            outline=ABSTRACT)

