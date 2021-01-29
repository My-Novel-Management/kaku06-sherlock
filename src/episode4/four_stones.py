# -*- coding: utf-8 -*-
'''
Episode 4-5
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World



# DEFINE
TITLE = "四つの$stone"


# NOTE: outlines
ABSTRACT = """
殺人事件が解決され、また$maryも無事に戻ってきた。
ただ$blue_stoneが何故一緒にあったのか、その謎だけが$sherlockには引っかかっていた。
後日$maryを助けてくれたという女性と出会う。彼女が$jackだとすぐに分かり、$sherlockは何故戻ってきたのか尋ねる。
どうやら預けていた$blue_stoneが誰かに盗まれたと分かり、取り戻しにきたらしい。どこからどう回ったのか、殺害された$moura夫人の手に渡り、男が盗んだが、凶器と一緒にガチョウに隠してしまったということだった。
$jackは何者かが$stoneを集めようとしていると警告する。四つの$stoneを集めて何をしようとしているのかはよく分からないが、それは今の世の中にとってよくないことだと$jackは考えている。
その目的解明と何かやろうとしていることの阻止を託され、$jackから$blue_stoneを預けられた
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("事件が解決し、ガチョウクラブにも捜査の手が入った。$maryも$jackにより救出された"),
            w.plot_turnpoint("$jackは$sherlockに話があると呼び出した"),
            w.plot_develop("$jackは$stoneと裏社会の動きについて$sherlockに教える"),
            w.plot_turnpoint("自分が盗んだ$red_stoneは何者かに盗まれたと告白した"),
            w.plot_resolve("$jackは$sherlockに$blue_stoneを託し、裏世界で動いている何者かの企みを阻止してほしいと依頼した"),
            w.plot_note("薄っすらと日が登り、$sherlockが$wilsonのところにやってくる"),
            w.plot_note("$sherlockは野暮用が片付いたと言う"),
            w.plot_note("$wilsonの方は何の変化もなく、おそらくここではないどこかに監禁されているのではないか、と"),
            w.plot_note("と、建物の前に誰か現れる。$adelだった"),
            w.plot_note("彼女はこっそりと建物に忍び込む。明らかに不法侵入だった"),
            w.plot_note("$wilsonは$sherlockに彼女が一体何者なのか尋ねる"),
            w.plot_note("よくは知らないが$wilsonの同業者だろうと"),
            w.plot_note("しばらくすると建物から出てくる$adel。その手に何か資料を持っていた"),
            w.plot_note("そこに出ていって声をかける$sherlock"),
            w.plot_note("$adelは無視して行ってしまおうとしたが、$sherlockが自分の知人がここの連中に捕まっている可能性を言うと"),
            w.plot_note("$adelは自分もそういう内容の指示を受けて、改めて調査に訪れたと語る"),
            w.plot_note("ただ監禁されているならここではなく、ハーバーの方だろうと"),
            w.plot_note("幹部が保持している船が密会の会場になっていると告げた"),
            #
            w.plot_note("$maryは謎の女性と話していた"),
            w.plot_note("彼女は$ailyと名乗り、自分は忘れ物を取りに来たら捕まってしまったと語る"),
            w.plot_note("$maryは自分の事情を話して、ガチョウクラブが密売組織だと訴える"),
            w.plot_note("$ailyは$maryが$sherlockの知人と知り、自分も知人だと告げて、助けてあげると言う"),
            #
            w.plot_note("一方$limeは誰も見つからず、一人でさまよい歩いていた"),
            w.plot_note("と、謎の悲鳴を聞く"),
            w.plot_note("$limeが見に行くと、そこには惨殺された女性の姿があった"),
            w.plot_note("$maryと勘違いして悲鳴をあげる$lime"),
            w.plot_note("そこに駆けつけたのは$mikelだった"),
            w.plot_note("$mikelはそれを見て、話題の猟奇殺人事件だと分かり、すぐ警察に連絡する"),
            w.plot_note("それと同時に$limeに対して頭を抱える"),
            #
            w.plot_note("$sherlockたちはハーバーまでやってきていた"),
            w.plot_note("沢山の船がとまっている"),
            w.plot_note("$sherlockはそのうちの一艘に見張りが立っているのを見つける"),
            w.plot_note("誰かを待っているようだ"),
            w.plot_note("$wilsonにどの程度武術の心得があるか聞いて、大丈夫というのが分かり、先に行って人数の推測を立てる"),
            w.plot_note("見張りは船と周辺で五名は確認できた"),
            w.plot_note("$wilsonが陽動役になり"),
            w.plot_note("$sherlockは一人一人減らしつつ、監禁場所を探す"),
            w.plot_note("そこに女性に連れられた$maryの姿が現れる"),
            w.plot_note("その女性を見て$sherlockは驚く。$jackだった"),
            #
            w.plot_note("$jackにより助け出された$mary"),
            w.plot_note("倉庫には大量の$dragと$gunがあった"),
            w.plot_note("事件は外交官特権を利用して密売・密輸を行っていた$mouraの夫と、ガチョウクラブの犯罪を露見させようという、夫人の愛人の策略だった"),
            w.plot_note("夫人は配管工の$raiderに鞍替えして、それを恨んでの犯行だったが、ナイフを隠したガチョウが$raiderに渡らず、肉屋に渡ってしまった誤算"),
            w.plot_note("更にそれが$sherlockの手に渡り、何故か中に$blue_stoneまで入っていた"),
            #
            w.plot_note("その日、$sherlockは$jackに呼び出されて食堂にやってくる"),
            w.plot_note("食堂でオーダーをとった店員が$jackだった"),
            w.plot_note("彼女はそれを運んできて対面に座る"),
            w.plot_note("$jackは$maryを助けたことで、見逃してくれた恩は返したと言う"),
            w.plot_note("ずっと借りを返す機会を伺っていたと"),
            w.plot_note("話は$blue_stoneについてだった"),
            w.plot_note("新聞に乗せたのが$sherlockだということはすぐ分かった"),
            w.plot_note("確かにもともとは$moura夫人が持っていて、それを$jackが盗んだのだが、隠し場所に困り、ガチョウの中に隠した"),
            w.plot_note("すぐ回収するつもりだったが、そこに元愛人の$zolkがやってきて殺人事件を起こしたので、とりに行けなかった"),
            w.plot_note("国内に戻ってきたのも$blue_stoneの所在が分かったからだった"),
            w.plot_note("$sherlockは誰の思惑で$stoneを集めているのか問いかける"),
            w.plot_note("$red_stoneについては別の依頼で、そこから自分なりに$stoneについて調べたという"),
            w.plot_note("現在闇マーケットで$stoneを求める声が高まっていて、かなりの金額がついている"),
            w.plot_note("偽物もたくさん出回っているという"),
            w.plot_note("$jackは誰が集めようとしているのか分からないが、自分が集めてそちらに高く売りつけようという算段があった"),
            w.plot_note("$jackは$sherlockにしばらく$blue_stoneを預けておいてあげる、という"),
            w.plot_note("いつか必要になったら取りに行くと"),
            w.plot_note("またしばらく国外に消える、と言い残して、店から出ていった"),
            #
            w.plot_note("$maryは$sherlockたちに謝罪する。自分一人で突っ走ってごめんなさいと"),
            w.plot_note("$limeは何かすぐれない。いつも以上に言葉少なだった"),
            w.plot_note("事件解決したのに$sherlockも考え事が増えて、外出することも増えた"),
            w.plot_note("やってきた$wilsonは$maryに「みんなは？」と"),
            w.plot_note("$maryは自分で何か役立とうと、ちゃんと料理の勉強を始めていた"),
            w.plot_note("$refiがやってきて、焼き菓子を教えてもらっていた"),
            w.plot_note("少しずつ変化してきているのを感じる$wilson"),
            outline=ABSTRACT)

