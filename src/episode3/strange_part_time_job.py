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
            w.plot_note("$maryが連れてきた鎧騎士は$limeと名乗った"),
            w.plot_note("だが彼は喋れなかった。すべて筆談とジェスチャーだ"),
            w.plot_note("細かい説明は文字を書いてもらう"),
            w.plot_note("$limeの文字は綺麗だった"),
            w.plot_note("この時代は以前より識字率が上がっているとはいえ、まだまだ文字が書けない人は多かった"),
            w.plot_note("$limeは今、質屋の守衛の仕事をしている"),
            w.plot_note("世話になっているのが質屋オーナー夫婦で、住み込みで働かせてもらっているらしい"),
            w.plot_note("質屋には他にも$jakinsという同僚がいて、彼は店番を担当しているらしい"),
            w.plot_note("その$jakinsの紹介でちょっと変わったアルバイトがあった"),
            w.plot_note("質屋の守衛は住まわせてもらっている分でほぼ相殺になって大した小遣いにならない"),
            w.plot_note("その珍しいバイトというのは、赤い鎧を着た者だけが資格がある赤鎧クラブというものが主催していた"),
            w.plot_note("当日面接に行くとたしかに赤い鎧騎士だらけだった"),
            w.plot_note("その中で筆記試験があり、それに合格した数名がどうやらそのバイトを行えることになっていた"),
            w.plot_note("バイトは週に五日、午後の三時間で、赤鎧クラブの施設に行き、そこで写本を行う"),
            w.plot_note("部屋は個室で、作業中は$lime一人だった"),
            w.plot_note("それだけで週給五万$Gという破格"),
            w.plot_note("それを三ヶ月続けているがこのままでいいのか不安だという"),
            w.plot_note("ただ貯めたお金でオーナー夫婦に何かお返しをしたいと考えているとも"),
            w.plot_note("$sherlockはそのアルバイトをすぐ辞めるように言う"),
            w.plot_note("理由は言わない"),
            w.plot_note("ただ「そのうちに赤鎧クラブなんてものは君の前から消えてしまうだろう」と"),
            w.plot_note("お金がもらえているだけで良心的な気になるが、おかしいと感じるその感性の方が正常だとも"),
            w.plot_note("$maryは何も考えてないと怒ってしまう"),
            #
            w.plot_note("$maryは$limeを送っていく"),
            w.plot_note("$sherlockの言い方が悪かったけれど何も考えてない訳じゃないと思う、とフォローする"),
            w.plot_note("$maryは話せない$limeに対して、自分の身の上話をする"),
            w.plot_note("自分は拾われた家で育てられ、そこである事件があり、自分はその容疑者になってしまった"),
            w.plot_note("誰もが信じていない中で、$sherlockだけが自分のことを犯人じゃないと信じて事件を調べて解決してくれた"),
            w.plot_note("決して悪い人じゃないと"),
            w.plot_note("更に困ったらいつでも頼ればいいとも。自分も押しかけたら追い出さずに置いてくれているから、質屋夫婦に追い出されても頼めば何とかなるかもと"),
            w.plot_note("$limeは$maryに感謝する"),
            #
            w.plot_note("仕事の質屋にやってくる$limeと$mary"),
            w.plot_note("$limeは$maryを$jakinsに紹介した"),
            w.plot_note("$jakinsは優しそうな男で、ただ汗かきのようだった"),
            w.plot_note("彼から$limeは本当に真面目に働いていると教わる"),
            w.plot_note("また友達になってやってほしいとも"),
            w.plot_note("また来てと言われ、$maryは帰宅する"),
            #
            w.plot_note("夜、$maryの作ったスープを食べながら$sherlockに尋ねる"),
            w.plot_note("どうしてあんな言い方をしたのか、と"),
            w.plot_note("$sherlockは説明するのが面倒そうにして"),
            w.plot_note("「少しは自分で考えてみるといい」と"),
            w.plot_note("$maryは$sherlockを真似て自分なりに推理してみる"),
            w.plot_note("赤い鎧を着た人を集めるのが趣味で、部屋に閉じ込めてにやにや監視しているとか"),
            w.plot_note("本当の目的は赤い鎧を取ることで、暑くなったりして脱いだときに偽物と変えてしまうとか"),
            w.plot_note("$maryなりの推理をしてみたが$sherlockにはことごとく否定されただけだった"),
            w.plot_note("$maryはキッチンで洗い物をしながら考える"),
            w.plot_note("$limeはしゃべれないけれど、なんとなく自分と気が合うと感じて、友達になれそうだと思って嬉しくなる"),
            #
            w.plot_note("後日、$maryは市場からの帰り道、再び困っている赤い鎧騎士を見つけた"),
            w.plot_note("それは$limeだった"),
            outline=ABSTRACT)

