# -*- coding: utf-8 -*-
'''
Episode 4-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "事件解決"


# NOTE: outlines
ABSTRACT = """
$jackは$maryを外へと逃してくれようとする。しかし男たちに気づかれ、逆に閉じ込められてしまう。それでも$jackは$sherlockがくると言う。
$maryは$jackも$ajinだと知り、自分の悩みを相談する。$sherlockはどんな人種であろうがそこに妙な感情は抱かないと言う。時折本当に感情があるんだろうかと疑うくらいで、その点で彼は信頼していいと。$maryはほっとする。
一方$sherlockは$limeからの情報を得て、警察に手配する。
その間に再度被害者宅とガチョウの卸業者を調査する。そこで事件の犯人がガチョウクラブの人間ではなく、それに見せかけた彼女の愛人の仕業だと見破る。
ナイフの指紋が検出できないように細工していたのは、その技術が存在することを知っていたかららしい。男の出自が謎だったが、どうも別の国からやってきた人物らしかった。
ただの痴情のもつれが原因と知り、偽装しただけで、凶器の隠し場所に悩んだ末のガチョウに食べさせるというやり口だった。
そして$ignesから警察により$maryが保護されたという連絡が入った。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryは謎の女性（$jack）によって助け出される"),
            w.plot_turnpoint("しかし逃げ出したのがバレて追われる身となった"),
            w.plot_develop("$sherlockの指示でガチョウクラブに警察の捜査が入る。しかしそこに$maryの姿はなかった"),
            w.plot_turnpoint("男たちの誰もナイフから指紋検出されなかった"),
            w.plot_resolve("全て空振りだった$shelrockの前に$maryと謎の女（$jack）が現れる"),
            w.plot_turnpoint("$sherlockにより事件の犯人が逮捕された（$moura夫人の愛人だった）"),
            w.plot_note("$sherlockは$wilsonに「$jackが国内に入ったという情報が入った」と言った"),
            w.plot_note("$sherlockは今回の$blue_stoneには$jackが絡んでいると睨んでいた"),
            w.plot_note("$jackが、というか、その裏にいる人物あるいは組織がどんな目的で$stoneを集めようとしているのかを考えていると"),
            w.plot_note("そこで$maryも$limeも帰ってこないことに気づく"),
            w.plot_note("どちらが片付け物をするかという議論になり、それより二人を探そうということに"),
            #
            w.plot_note("$limeは$mikelによって安全な場所まで連れてこられていた"),
            w.plot_note("$limeは友達がガチョウクラブにいるから確かめに行きたい旨を話す"),
            w.plot_note("ガチョウクラブについては内偵調査が入っているが、あまりいい話は聞かないから近づくなと"),
            w.plot_note("$limeは危険でも友人の方が大切だと言う"),
            w.plot_note("仕方なく$mikelは$adelに確認させることにして、$limeを送っていく"),
            #
            w.plot_note("一方$maryはどうやって逃げ出そうかと考えていた"),
            w.plot_note("場所も分からない"),
            w.plot_note("眠らされて、どこかに運ばれたのは確かだと考える"),
            w.plot_note("よく耳をすまして周囲の状況を確認した"),
            w.plot_note("$sherlockの言葉を思い出す。諦める前にまず今手に入る全ての情報をいれて、考えること"),
            w.plot_note("少ない情報では間違った結果しか選択できない"),
            w.plot_note("まずは選択肢を増やすことだ、と"),
            w.plot_note("かすかに波の音が聴こえる"),
            w.plot_note("海か川の近く"),
            w.plot_note("船で国外に出されると推測した"),
            w.plot_note("外で見張りが交代しているのが分かる"),
            w.plot_note("$maryはどこかのタイミングでドアが開くだろうと考え、それまでに準備を進めることにした"),
            #
            w.plot_note("$sherlockと$wilsonは$maryと$limeの行方を推理する"),
            w.plot_note("ガチョウの件で追っていたことを思い出し、$ignesのアジトに向かう"),
            w.plot_note("少年探偵団のメンバーが暮らしている長屋"),
            w.plot_note("$maryと$limeの行方を調べてくれと頼む"),
            w.plot_note("すぐにパブで$raiderがしゃべっていた情報を掴む"),
            w.plot_note("そこからガチョウクラブの存在がクローズアップされる"),
            w.plot_note("$wilsonにガチョウクラブに向かってもらい、$sherlockは別行動を取る"),
            #
            w.plot_note("夜のガチョウクラブ前は静まり返っていた"),
            w.plot_note("$wilsonは監視すべく、そこで待っていることに"),
            #
            w.plot_note("$limeは家に戻った"),
            w.plot_note("しかし誰もいない"),
            w.plot_note("大人しくしているように言われたが心配になり、再び外に出る$lime"),
            #
            w.plot_note("$sherlockは$moura夫人宅に来ていた"),
            w.plot_note("外交官の旦那は家にいて、怪訝な顔で応対に出た"),
            w.plot_note("$sherlockは夫人がガチョウクラブに入っていたことを尋ねる"),
            w.plot_note("ガチョウクラブでガチョウが安く手に入ると聞いている、とだけ"),
            w.plot_note("その頃から性格に変化はなかったか、と"),
            w.plot_note("あと、ガチョウクラブは誰から紹介されたのか、と"),
            #
            w.plot_note("$maryは明け方、物音を聞く"),
            w.plot_note("と、誰か知らない女性が捕まえられて入れられた"),
            w.plot_note("その女性は$maryは知らないが、$jackだった"),
            outline=ABSTRACT)

