# -*- coding: utf-8 -*-
'''
Episode 1-3: "$ailyという女"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Scenes
# NOTE

# NOTE: outlines
ABSTRACT = """
$sherlockは$ailyが活動していたオペラ座に足を運ぶ。
そこで座長から改めて$ailyの人物像を聞く。
$ailyに出会ったのは街角のパブで歌っていた時だった。その歌声は素晴らしく、すぐにスカウトしたが、歌うこと以外は何もできず、人付き合いも全然だった。
それがある日を境に陽気になり、役者としても素晴らしい才能を見せつけた。そこからはずっと看板女優だと語る。
ただ私生活は謎に包まれていて、家に行ったのも今回が初めてだと。
また慈善事業に熱心で、ある程度稼げるようになる前から孤児院に寄付をしていたと。
その孤児院を教えてもらう。
孤児院で教師に会い、そこで$ailyがこの孤児院出身だと教わる。
$ailyの印象が変わる。小さい頃から他人を信じずに歌だけを信じて生きてきた。その彼女が舞台で変わったんだ、と言っていたがどこか違和感だった。
すると、殺されていた女性が$ailyだったと$restradeから連絡が入った
"""


# Episode
def main(w: World):
    return w.episode("$ailyという女",
            # NOTE
            w.plot_setup("$ailyが寄付していたという孤児院を訪ね、彼女の情報を集める"),
            w.plot_turnpoint("$ailyはその孤児院出身だった"),
            w.plot_develop("$ailyが孤児院出身で貧しいところから成功したと知る。しかし教師の語る$aily像はやはり王子のものと違和感があった"),
            w.plot_turnpoint("$ailyには唯一といっていい友人がいたことを知る"),
            w.plot_resolve("最初に$ailyが働いていたパブを訪ね、そこでよくその友人の女が来ていたことを知った"),
            w.plot_turnpoint("殺害されていたのが$ailyだと、警察の調べで分かった"),
            w.plot_note("孤児院にやってきた$sherlockと$wilson"),
            w.plot_note("$London市内でもスラム街にあり、雰囲気が違っている"),
            w.plot_note("見たところ普通の孤児だけでなく、混血児などの面倒も見ているらしい"),
            w.plot_note("訪れた時には孤児院の子供ではない、スラムに暮らす外の子供への炊き出しを配っていた"),
            w.plot_note("院長の$merouが応対していた"),
            w.plot_note("他にも女性教師の$yilaの姿もある（実は$jack）"),
            w.plot_note("$sherlockは$merouから$ailyについて聞く"),
            w.plot_note("$ailyは多額の寄付をしてくれるいい人でもあるけれど、それ以前にここの元院生だったという"),
            w.plot_note("$ailyは両親が酷い親で、発見されたときには栄養失調の衰弱死寸前だった"),
            w.plot_note("保護した団体からここに預けられて、最初は誰とも口をきかなかった"),
            w.plot_note("音楽の時間に端っこで一人口ずさんでいるのを聞いて、一緒に歌ってみないと誘った"),
            w.plot_note("歌によって打ち解けて、みんなとも多少コミュニケーションが取れるようになった"),
            w.plot_note("パブで働けることになり、そこで雇ってもらい、ここを出ていった"),
            w.plot_note("その後はオペラにスカウトされ、今のように人気歌手になった"),
            w.plot_note("働き始めてから少額で寄付をしてくれていたが、オペラ歌手になり沢山寄付をくれるようになった"),
            w.plot_note("孤児院に顔を出すことはなかった。最初はちょくちょく顔を出してくれていた"),
            w.plot_note("最近は全く見ていない。精神的に弱い部分があるがうまくやっているのか心配だった等"),
            w.plot_note("$sherlockは他の人からも話をと思い、$yilaに声をかける"),
            w.plot_note("$yilaは時々手伝いにきているらしい"),
            w.plot_note("$yilaから$ailyには一人だけ女性の友達がいたと教わる"),
            w.plot_note("その親友は歌うことしかできなかった$ailyに食事を運んだり、一緒に遊んだりしてあげた"),
            w.plot_note("ここを出てからも親交があり、パブに勤めていた頃は毎日のように応援にかけつけた"),
            w.plot_note("オペラで歌うようになり、少し親交が薄くなった"),
            w.plot_note("その友達の女性は孤児院にも現れないし、どこで何をしているのかも分からないと"),
            w.plot_note("名前は$reddleyと言った"),
            #
            w.plot_note("$sherlockは次に$ailyが働いていたパブに向かう"),
            w.plot_note("パブは小さいところで店長は歌だけが上手かったが他にも沢山いるような目立たない存在だったと"),
            w.plot_note("$ailyの友人の女性について尋ねたが、そんな女見た記憶がないと"),
            #
            w.plot_note("$sherlockは王子からの書簡にあった$ailyが性悪女だという文言がどうも気になると言う"),
            w.plot_note("$wilsonに頼んで王宮前に立ち寄ってもらう"),
            w.plot_note("そこで門番をしている守衛の$fredに手紙を握らせた"),
            w.plot_note("一旦自宅へと送ってもらう"),
            w.plot_note("また翌日調査しようということで、別れた"),
            #
            w.plot_note("翌朝$sherlock宅を訪れると「大変なことになった」と$sherlock"),
            w.plot_note("警察からの連絡で殺されていたのが当の$aily本人だと判明した、と"),
            outline=ABSTRACT)

