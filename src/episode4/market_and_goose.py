# -*- coding: utf-8 -*-
'''
Episode 4-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "市場とガチョウ"


# NOTE: outlines
ABSTRACT = """
$limeが同居するようになり、彼女も家事を手伝うようになっていた。だが彼女は$maryと違い、料理も上手で掃除や洗濯も手際よくこなし、$maryは買い物だけが自分の役割になってしまった。そのことについて居場所を失ったような気になり、市場で仲良くなった肉屋の$nowlisに相談する。
一方$sherlockは$wilsonから頼まれていた第二王女失踪の調査が、$limeを見つけたことで一旦解決した。けれど連続失踪事件、および、最近明らかになった連続猟奇殺人事件について独自に調査を進めていた。
$wilsonは$sherlockと$limeから頼まれて、もうしばらく第二王女が見つかったことは内緒にしておくことにした、と言ったが、その裏で王室執務官の$mikelと出会っていた。何とか無事なこと、安全は確保していることを伝えると、$mikelの方で色々と考えると言われた。
$maryは$nowlisから沢山貰ったからとガチョウを一羽まるまるプレゼントしてもらえた。
喜んでそれを持ち帰り、$limeに捌いてもらうとそのガチョウの中からナイフと$blue_stoneが出てきた
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$limeが一緒に暮らすようになり、$maryは自分の役割を取られたような気分になっていた"),
            w.plot_turnpoint("$maryは逃げるように市場に買い出しに行く"),
            w.plot_develop("$sherlockは$wilsonの依頼を終えても失踪事件について調査を続けていた。あまり構ってくれないと憤慨する$maryは市場で仲良くなった肉屋の$nowlisに相談する"),
            w.plot_turnpoint("$nowlisからガチョウをもらう"),
            w.plot_resolve("$maryは自分も役に立つとガチョウを自慢する"),
            w.plot_turnpoint("だが$limeに捌いてもらったガチョウからはナイフと$blue_stoneが出てきた"),
            w.plot_note("$maryに続いて$limeも$sherlockの家で一緒に暮らすようになった"),
            w.plot_note("部屋は$sherlockの寝室を二人に使ってもらい、$sherlockはリビングか研究室で寝ることになった"),
            w.plot_note("$maryも$limeも$sherlockがしてなかった分まで部屋の掃除や片付け、洗濯物をしてくれた"),
            w.plot_note("$limeはどういう訳か$maryよりも遥かにそういったことに長けていて、一人家政婦を雇ったくらいの戦力になっていた"),
            w.plot_note("この日の朝食には焼き立てのトーストに野菜を盛り付けたサラダ、ミルクではなく果物を使ったスムージーになっていた"),
            w.plot_note("$sherlockは「最近食事がちゃんとしている」と口にしてしまう"),
            w.plot_note("$limeは口数が少ないが、多少慣れて説明くらいはしてくれるようになっていた"),
            w.plot_note("花嫁修業と称して、様々な習い事をさせられていたらしい"),
            w.plot_note("料理や裁縫だけでなく、楽器も、生花や舞踊の類も長けていた"),
            w.plot_note("更に薙刀という東洋の武術も習得していた"),
            w.plot_note("かなりスペックが高く、$maryは自分なんていらないんじゃないかと思ってしまう"),
            w.plot_note("先に食べ終わり、キッチンに引っ込んで洗い物をする"),
            w.plot_note("朝食の片付けが終わると、逃げるように買い物にでかけた$mary"),
            #
            w.plot_note("$wilsonが訪れる"),
            w.plot_note("第二王女失踪事件の解決が終わっても、まだ何かと毎日やってきては雑談していた"),
            w.plot_note("最近、主にスラム街の方で若い女性の猟奇殺人が続いていた"),
            w.plot_note("もともと事件の多い地区だったが、さすがに何らかの関係があるだろうと"),
            w.plot_note("また失踪事件については別途、$sherlockの興味で調査を行っていた"),
            w.plot_note("$sherlockにその後、王室側の依頼へのレスポンスがどうなっているか尋ねられ、$wilsonはまだ何もないと誤魔化した"),
            w.plot_note("$limeは掃除しつつもその話を聞いていて、不安そう"),
            w.plot_note("$wilsonが兜くらい外したらと言うが、この方が慣れていると鎧騎士の姿のままだった"),
            #
            w.plot_note("市場にやってくる$mary"),
            w.plot_note("最近仲良くなった肉屋の$nowlisが声をかけてくる"),
            w.plot_note("ため息をついていた$maryは$nowlisに「元気になりたいからお肉を安く譲ってくれ」と無茶な注文"),
            w.plot_note("話を聞く$nowlis"),
            w.plot_note("$maryは普段家で新聞や資料、本を読んでいるだけの$sherlockに対して、自分が微力ながら助けになると思っていた"),
            w.plot_note("家事も洗濯も苦手だけれどがんばってやっている"),
            w.plot_note("だが新しい住人の$limeはそれを完璧にこなしてしまい、自分の居場所がなくなったみたいだと"),
            w.plot_note("$nowlisは買い物だって大事な仕事だし、本当に役立たずなら$sherlockも追い出すんじゃないかと"),
            w.plot_note("そこでまるまる一匹のガチョウを取り出す$nowlis"),
            w.plot_note("大量に安く手に入ったから、おすそ分けだと"),
            w.plot_note("かなりおまけして安くしてくれた"),
            w.plot_note("あとついでに卵もいくつかおまけしてくれる"),
            w.plot_note("それで満足して笑顔になる$mary"),
            w.plot_note("ありがとうを言って帰っていく"),
            #
            w.plot_note("帰りの途中で警戒中の警察の一団とすれ違う"),
            w.plot_note("それを指揮していたのは$patsonで、$maryを見つけるなり顔を顰める"),
            w.plot_note("近づいてきて$sherlockはどうしている？と"),
            w.plot_note("答える義務はないと言って、つっぱねて、さっさと帰っていく"),
            #
            w.plot_note("家に戻った$maryはガチョウを見せて「自分じゃなかったらおまけしてもらえなかった」と自慢げ"),
            w.plot_note("さっそく$limeに捌いてもらう"),
            w.plot_note("$sherlockは$maryに何も言わない"),
            w.plot_note("$maryはキッチンで$limeとどんな料理にしようか楽しげに相談している"),
            w.plot_note("$wilsonはガチョウ一羽まるまるを見て、丸焼きを楽しみにしていた"),
            w.plot_note("今日はここで夕飯をごちそうになろうか、と"),
            w.plot_note("と、声が上がる"),
            w.plot_note("$maryが$sherlockたちに早く来てと言うので、かけつける$wilsonと、特に見に行く必要を感じない$sherlock"),
            w.plot_note("キッチンに顔を出した$wilsonはそこで$limeが手にしている血まみれのナイフを目にする"),
            outline=ABSTRACT)

