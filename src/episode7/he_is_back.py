# -*- coding: utf-8 -*-
'''
Episode 7-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "英雄の帰還"


# NOTE: outlines
ABSTRACT = """
変身して$sherlockたちを追い詰める$jake。しかし$sherlockの機転で工場に穴を開け、日光を浴びせかけることで$jakeは皮膚から大量に出血し、爆発した。
その爆音を聞いて$limeたちが駆けつける。$maryが身を挺して$sherlockを守っていたが、$maryは大怪我を負ってしまった。入院することになる$mary。
戻った$sherlockは、一旦$wilsonの家で$limeたちに事情を語る。
$morianoとの対決により滝壺に落下し、死を覚悟した$sherlockだったが、$maryが繕ってくれた服の裾が引っかかり、何とか死だけは免れた。
ただ大怪我をしており、そこを助けてくれたのが、$jackだった。彼女の別荘で回復するまで休養しながら各国の情報を集め、$moriano配下の動向を追いかけていた。
未だに$sherlockを探す動きが見えたので、おびき出すために空き家の件をでっち上げた。だがそれを利用した$jakeにより$maryがおびき出された、というのが今回の一件だった。
$sherlockは$maryに預けておいた$blue_stoneを取り戻す必要があると言う。
しかし$sherlockたちが病院に駆けつけると、$maryの姿が消えていた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("連続殺人犯$jakeは$maryを殺そうとする"),
            w.plot_turnpoint("そこにホームレスが助けに入る"),
            w.plot_develop("$sherlockは$jakeがどんな人生を歩んできたかを全て言い当て$jakeの牙を無力化しようとする"),
            w.plot_turnpoint("$transformした$maryにより$sherlockが守られるが、彼女が負傷する"),
            w.plot_resolve("$sherlockが呼んでおいた警察により$jakeは捕らえられた。$maryは入院し、$sherlockも治療を受ける"),
            w.plot_turnpoint("入院している$maryから$blue_stoneを貰おうと思ったが$patosonにより連れ出された後だった"),
            outline=ABSTRACT)

