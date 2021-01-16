# -*- coding: utf-8 -*-
'''
Episode 3-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "奇妙なアルバイト"


# Scenes
# NOTE

# NOTE: outlines
ABSTRACT = """
しゃべれない鎧騎士は筆談で$limeと名乗った。困っていたのは自分のアルバイトについて。
こんな状態になり、拾ってもらった質屋オーナー夫婦宅に居候していて、その代わりに質屋の守衛をやっていたが、仕事の同僚$jakinsからある奇妙なアルバイトを紹介された。
それが赤鎧クラブという聞いたこともない集まりだった。
赤い鎧を着た者だけが仕事を受けられ、$limeは見事にそれに合格し、週に五日、午後の三時間を赤鎧クラブに出向いて、そこの大事な古文書を写本するだけでかなりいい給料がもらえる。
$limeはそれでオーナー夫婦に何か恩返しをしたいと思っているというが、守衛の仕事をサボっていることと、黙ってアルバイトをしていることが引っかかっているという。
$sherlockはすぐそのアルバイトを辞めるよう進言する。理由は話さない。
落ち込む$limeを送っていく$maryだった。
後日、再び訪れた$limeは突然赤鎧クラブが閉鎖になり、更には同僚の$jakinsが失踪したと言った。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("筆談で$limeと名乗った喋れない鎧騎士は$sherlockに相談したいことがあると言った"),
            w.plot_turnpoint("$limeは自分がしている奇妙なアルバイトについて語り出す"),
            w.plot_develop("$limeは仕事の同僚に紹介された赤鎧クラブという赤い鎧を来た者だけが資格のある不思議なアルバイトをしていた。給料がよかったが、仕事を途中でサボっているみたいで気が進まないと相談する"),
            w.plot_turnpoint("$sherlockは$limeにすぐアルバイトを辞めるように進言した"),
            w.plot_resolve("$maryは$sherlockの失礼を謝りつつも$limeを質屋まで送っていく"),
            w.plot_turnpoint("後日、再度$limeがやってきて赤鎧クラブが閉会されたと言った"),
            outline=ABSTRACT)

