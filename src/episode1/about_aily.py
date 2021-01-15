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
            outline=ABSTRACT)

