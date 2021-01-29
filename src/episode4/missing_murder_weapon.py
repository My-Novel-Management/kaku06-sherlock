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
            w.plot_note("$sherlockは$casselにレプリカ作成を依頼して$blue_stoneを預けた"),
            #
            w.plot_note("$sherlockは次に情報屋を訪れる"),
            w.plot_note("$flenは「そろそろ来る頃だと思ってましたぜ。旦那」と抜かりない"),
            w.plot_note("$sherlockは前に言っていた裏世界が最近騒がしいというのを聞く"),
            w.plot_note("どうも$stoneを集めようという意志があり、それに関する情報が最近飛び交っていると"),
            w.plot_note("もともと流行病のように何度もブームがあったが、今回はどうもかなり大量の資金が流入して本格的に探している連中がいるという"),
            w.plot_note("また別件で、猟奇殺人事件についてもあった"),
            w.plot_note("「旦那は$ajinについてご存知ですかい」"),
            w.plot_note("それは人と闇の者の混血のことを主に言っていた。$maryもそうだ"),
            w.plot_note("「どうも最近の犯罪に、$ajin集団が一枚噛んでるって噂ですぜ」"),
            w.plot_note("先日の銀行強盗団も、その関係の勢力が関わっていたという噂があるらしい"),
            w.plot_note("それとおまけで違法$gunと$dragの話があった"),
            w.plot_note("新興勢力の資金源になっているらしいと。ただそれが今までの組織とは全く関係ないところから出てきたらしい"),
            w.plot_note("$sherlockは引き続き情報を集めてもらうよう言って、店を出た"),
            #
            w.plot_note("$maryは事情聴取後に心配になって市場を訪れる"),
            w.plot_note("ちょうど聴取から帰ってきた肉屋の$nowlisがいた"),
            w.plot_note("話を聞くと、たくさんガチョウを仕入れられたのも、付き合いのある卸問屋が余っているからもらってほしいと頼んできたからだった"),
            w.plot_note("警察にはそのことを話し、殺された$moura夫人とは面識がないことを確かめられると釈放された"),
            w.plot_note("ただ警察には容疑者候補の一人としてマークされていて、しばらく市場と自宅以外は外出するにも警察を通してくれと言われていた"),
            w.plot_note("$maryはそれを聞いて、自分が事件を解決すると言い出す"),
            w.plot_note("$nowlisは無茶するな、と言いつつも卸問屋のことを教えてくれた"),
            #
            w.plot_note("$maryがその卸問屋$hornetを訪れると、誰かと商談中だった"),
            w.plot_note("男は明らかに$ajinで、ガチョウクラブを名乗っていた"),
            outline=ABSTRACT)

