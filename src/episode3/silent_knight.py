# -*- coding: utf-8 -*-
'''
Episode 3-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "沈黙の騎士"


# NOTE: outlines
ABSTRACT = """
$maryが一緒に暮らすようになり、彼女が家事に関する全てを買って出てくれた。だが$maryは経験がなく、おまけに壊滅的に下手だった。
今日も料理を失敗し、落ち込んで市場に買い出しに行く$maryを見送りつつ、$sherlockは$wilsonからの依頼で記事を調査する。
謎の失踪事件についての記事はいくつかあったが、関連性が見えてこない。それとは別の最近猟奇的な殺され方をしている事件があった。そちらはまだ話題になっていなかったが気になるという$sherlock。
一方買い物に出かけた$maryは$ignesたちと面識ができ、少し喋れるようになっていた。彼らに色々と紹介してもらい、市場の人間たちとも馴染みつつあった。彼女が$animalということで最初は奇異に見られたが、それも今でもマスコット的な存在となっていた。
帰り道、$maryは真っ赤な鎧を着た騎士を見つける。彼は困惑した様子で、$maryは思わず声を掛けた。
$maryが謎の鎧騎士を連れてくる。しかしその鎧騎士は話すことができなかった。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            #   NOTE
            w.plot_setup("$maryが一緒に暮らすようになり家事全般を担当してくれるようになったが彼女は壊滅的に下手だった"),
            w.plot_turnpoint("失敗して落ち込む$maryは市場に買い出しに向かう"),
            w.plot_develop("$wilsonは$sherlockにもう少し$maryに対して優しく扱ってやればと進言するが$sherlockは興味がない。ただ$wilsonの依頼である第二王女失踪に関する記事を集めてくれていた"),
            w.plot_turnpoint("$maryは市場で困っている赤い鎧騎士を見つける"),
            w.plot_resolve("$maryが困っていた鎧騎士を拾って連れて帰ってくる"),
            w.plot_turnpoint("$maryが連れてきた鎧騎士は喋ることができなかった"),
            w.plot_note("$maryが一緒に暮らすようになった"),
            w.plot_note("彼女は起きてくると、リビングで新聞を広げている$sherlockを見て「おはよう」と挨拶する"),
            w.plot_note("返事のない$sherlockにきれながらもキッチンに向かう"),
            w.plot_note("顔を洗い、エプロンをする"),
            w.plot_note("朝食の準備をする"),
            w.plot_note("焦げた目玉焼きにベーコン、パンにミルク"),
            w.plot_note("$sherlockは何も言わずにそれを食べる"),
            w.plot_note("そこに$wilsonが訪れる。「おはよう。ずいぶんと香ばしい臭いだね」"),
            w.plot_note("相変わらず料理は下手なままで$wilsonにからかわれると、$maryは「うちかて必死にやってんねん」とむくれる"),
            w.plot_note("「食事なんてお腹が膨れればいいんだよ」とそっけない$sherlock"),
            w.plot_note("$wilsonにも出してくれて、そのプレートを食べるがまずい顔"),
            w.plot_note("$maryは怒りながらも自分でもまずいらしい"),
            w.plot_note("$maryはそれでも食べて、後片付けにキッチンに引っ込む"),
            w.plot_note("$wilsonは$sherlockに失踪事件について何か進捗があったか尋ねる"),
            w.plot_note("改めて$wilsonの依頼内容を整理する$sherlock"),
            w.plot_note("第二王女が失踪したのは一ヶ月前。既に亡くなっていてもおかしくない"),
            w.plot_note("謎の失踪事件については、普通の失踪事件と見分けがつかないから判断しようがないが、記事にはいくつも見つかる"),
            w.plot_note("記事に掲載されるものの発生はばらばらで、頻度もよく分からない"),
            w.plot_note("それとは別に女性の猟奇殺人が二件、近く発生している。このうちの一人が半月前に失踪していた"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

