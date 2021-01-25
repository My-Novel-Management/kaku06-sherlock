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
            w.plot_note("孤島事件後、$maryが鬱々としていた"),
            w.plot_note("$sherlockはどこかに出かけていく"),
            w.plot_note("入れ替わりに$wilsonがやってきて$limeに「どうしたの？」と尋ねる"),
            w.plot_note("$maryは買い物に出かける"),
            w.plot_note("$wilsonも$sherlockに用事があったが、彼が不在なのでと出ていく"),
            w.plot_note("$limeは一人になり、考える"),
            w.plot_note("$mikelから王の体調不良の話を聞いていた"),
            w.plot_note("いつか王室に戻る決意をするべきです、と言われ、どうしようか迷っていた"),
            #
            w.plot_note("$maryは市場にやってきていた"),
            w.plot_note("花屋に立ち寄り$refiが元気に働いているのを見る"),
            w.plot_note("$refiは以前よりも色々な仕事を任されるようになっていた"),
            w.plot_note("声をかけようとした$refiにおじぎだけして、立ち去る$mary"),
            w.plot_note("肉屋の$nowlisが声をかけてくる"),
            w.plot_note("$ignesは少し遠くの配達に出ていると言った"),
            w.plot_note("$maryは最近自分の将来のことを考えてもやもやしていると"),
            w.plot_note("あと$ajinであるという立ち位置も、以前思っていたよりもずっと自分の立場を複雑にしているんだと気づいたと"),
            w.plot_note("市場の人間の多くは多種多様な人種を見ていて、そこまで思わない"),
            w.plot_note("$nowlisは気にするな、と励ました"),
            w.plot_note("$maryは買い物を済ませる"),
            w.plot_note("その帰り道、道端でしゃがみこんでいる老人を見つけた"),
            #
            w.plot_note("$sherlockは資料を手に家に戻ってきた"),
            w.plot_note("$limeから$wilsonが何か用事があると言っていたと聞く"),
            w.plot_note("$sherlockは$wilsonが戻ってくるまでにまとめておきたいと、資料をテーブルに広げ始める"),
            w.plot_note("そこには$morianoという名前があった"),
            w.plot_note("犯罪研究所というものを作っている"),
            w.plot_note("$sherlockはどうやら$moriano犯罪研究所が、一連の失踪事件にからんでいると見ているらしい"),
            w.plot_note("$morianoは元大学教授で、かつて神童と呼ばれた人物だった"),
            w.plot_note("$sherlockも彼の論文はいくつか読んで勉強しているという"),
            w.plot_note("多方面に才能を発揮し、若くして教授の地位を得て、王立大学で教鞭を持つ"),
            w.plot_note("しかし何故か突如大学をやめて、一人で犯罪研究所を開設した"),
            w.plot_note("やめる前に興味は心理学から犯罪学に移り、犯罪者の心の動きを数式化したり、現在の犯罪学の基礎となるいくつかの理論を論文にしている"),
            w.plot_note("今でも警察は彼に世話になっているという"),
            w.plot_note("その犯罪研究所がなぜ犯罪に関わっているのか、と$limeは尋ねる"),
            w.plot_note("$sherlockが個人的に作っている失踪者リストが、すべてその犯罪研究所に関係していたのだ"),
            w.plot_note("なんらかの調査、あるいは実験に参加したものがその後失踪している"),
            w.plot_note("最初は無作為、あるいは嗜好犯罪の類と考えたが、そうではなく、ある目的をもってこの失踪事件が発生していると"),
            w.plot_note("それに$moriano教授が何の考えもなしに、この関連性を放置するはずがないという確信もあった"),
            w.plot_note("$sherlockは自分の身の危険も覚え、$wilsonに協力を仰ごうと考えているとも語った"),
            w.plot_note("そこに$maryが老人をつれてやってくる"),
            w.plot_note("$sherlockはその老人こそが$morianoだという"),
            w.plot_note("何のことだか分からない$mary"),
            w.plot_note("$morianoは「はじめましてかな、$sherlock君」と挨拶をした"),
            outline=ABSTRACT)

