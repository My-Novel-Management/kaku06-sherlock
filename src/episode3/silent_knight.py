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

# Scenes
# NOTE

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
            outline=ABSTRACT)

