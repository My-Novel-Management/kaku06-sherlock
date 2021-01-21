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
            w.plot_note("ナイフを手にしていた$limeに驚く$wilsonだったが"),
            w.plot_note("すぐにナイフと$stoneがガチョウの胃袋から出てきたと言われる"),
            w.plot_note("それに驚いてやってきたのが$sherlock"),
            w.plot_note("ナイフを見て、それに付着したものが既に古い血であることを観察する"),
            w.plot_note("「本当に中に入っていたのか？　飲み込んでいたのだろうか」と考え始める"),
            w.plot_note("$sherlockは$wilsonに警察に連絡してもらい、とりあえず$limeたちからナイフと$stoneを丁寧に取り上げて確保する"),
            w.plot_note("「これどうしたらええ？」と疑問符の$maryに「重要な証拠だから食べる訳にはいかない」と言った"),
            w.plot_note("$maryと$limeは互いを見てうなだれる"),
            #
            w.plot_note("やってきたのは$patsonだった"),
            w.plot_note("またあんたらか、というため息"),
            w.plot_note("事件担当責任者は$restradeだが、別件で忙しいと言われた"),
            w.plot_note("事件について$patsonが説明する"),
            w.plot_note("実は凶器が現場から消失し、それを探していたところに連絡があったという"),
            w.plot_note("資産家の夫人が謎の死を遂げた"),
            w.plot_note("自宅が密室になり殺されていたが、殺害された凶器が見つからなかった"),
            w.plot_note("自殺説も上がったが胸を突き刺した角度がどうも自殺にしては妙だという話で、他殺の線で探していると"),
            w.plot_note("どうしてガチョウから出てきたのか、と問われたが分かるはずがないという当然の返答"),
            w.plot_note("$maryは$patsonに問い詰められる"),
            w.plot_note("$maryは自分が市場の肉屋から安く譲ってもらったことを話す"),
            w.plot_note("$patsonは早速市場に調査に向かった"),
            w.plot_note("$sherlockも$maryから詳しく話を聞く"),
            w.plot_note("肉屋の$nowlisが沢山安く手に入ったからと、安くしてくれたと語る"),
            w.plot_note("また警察に見せなかったが、$blue_stoneだと睨んだ$sherlockは宝石職人$casselのところに向かう"),
            #
            w.plot_note("$casselはすぐにそれは$blue_stoneだと言った"),
            w.plot_note("$blue_stoneの所有者は不明だった。どこにあるかも分からなかった。それがこうして出てきたということ"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

