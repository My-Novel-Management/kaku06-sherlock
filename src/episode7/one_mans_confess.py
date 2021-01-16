# -*- coding: utf-8 -*-
'''
Episode 7-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "ある男の告白"


# NOTE: outlines
ABSTRACT = """
$maryがいなくなり$limeは$ignesたちに協力をしてもらい、彼女を捜索する。だが警察側は$maryが$sherlockの逃亡幇助をしているのだとして、参考人として探していた。
一方目覚めた$maryの前には$sherlock（に似た男$jake）が現れていた。
$jakeは今までの失踪事件、猟奇殺人の全てが自分の手によるものだと告白する。自分も$maryと同じように闇の者の血を引く$ajinであり、普通に暮らしていると闇の血が騒ぎ、それを抑えるために誘拐、殺人を行う必要があると語る。
$jakeは真相を知った$maryを殺そうとする。
$ignesたちの情報網で、どうやら$maryに似た娘を廃工場街で見かけたという情報が入る。そこに向かう$limeたち。
$maryは$animal化して$jakeに抵抗していたが、どうしても$sherlockを傷つけることができず、追い詰められる。
そこに$maryを助けにあのホームレスの男が入ってくる。そのホームレスの正体こそが、$sherlockだった。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryは空き家からの抜け道を進み、それが廃工場に繋がっていることを知る"),
            w.plot_turnpoint("廃工場で沢山の遺体を発見する"),
            w.plot_develop("遺体が行方不明者だと分かったが、手口がどれも猟奇殺人のそれに似ていた"),
            w.plot_turnpoint("そこに$sherlockに似た男が現れる"),
            w.plot_resolve("$sherlock（に似た男$jake）は自分が失踪事件、猟奇殺人事件の犯人であると告白し、幼少期から鬱屈した歪んだ感情を抱えていたことを語る"),
            w.plot_turnpoint("$maryはその男が偽物であることを見抜いた"),
            outline=ABSTRACT)

