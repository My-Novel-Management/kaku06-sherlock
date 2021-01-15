# -*- coding: utf-8 -*-
'''
Episode 1-0: "便利屋$sherlock"
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
$wilsonはある依頼をする為に便利屋$sherlockの許を訪れる。
しかし$sherlockは$wilsonが説明する前から、彼がどういう人物で何を依頼しようとしているのかまで言い当て、挙げ句に「王室からの依頼は受けない」と断ってしまう。
$wilsonは諦めて立ち去ろうとするが、自分の$carに子供たちが群がっているのを見て追い払おうとしてからまれる。そこを通りかかりの少年$ignesに助けられた。
だが$sherlockが出てきて$ignesにすった財布を返すように言われて、少年は返して立ち去った。
$wilsonはこうして$sherlockとまともに話すことに。
家の中に入ると$sherlockは自分が色々な難事件や面倒なことを解決してきたが、その大半が王室経由の厄介事だったと吐露する。
だからもう二度と受けないと決めたと。
と、そこに王子の書簡を持った秘書の$adelがやってくる。
"""


# Episode
def main(w: World):
    return w.episode("便利屋$sherlock",
            # NOTE
            w.plot_setup("$wilsonは便利屋$sherlockに仕事を依頼に訪れる"),
            w.plot_turnpoint("$sherlockは$wilsonが話す前から彼の素性までを全て推理して言い当てる"),
            w.plot_develop("だが$sherlockは$wilsonが話す前から全てを言い当て、挙げ句に「王室からの依頼は受けない」と言い出す。$wilsonは何とか$sherlockに仕事を受けてもらおうとするが"),
            w.plot_turnpoint("$ignesに財布をすられたお陰で、$sherlockは家の中に入れてくれた"),
            w.plot_resolve("そこに王室執務官秘書$adelがやってきて王子からの依頼の書簡を置いていった"),
            w.plot_turnpoint("書簡には王室の印がされていた"),
            outline=ABSTRACT)

