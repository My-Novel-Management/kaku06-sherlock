# -*- coding: utf-8 -*-
'''
Chapter "最後の事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episode


# Chapter
def main(w: World):
    return w.chapter(TITLES[6],
            w.plot_setup("$sherlockは全ての黒幕として$morianoに辿り着く"),
            w.plot_turnpoint("$morianoのメッセージ（暗号）が新聞に掲載される"),
            w.plot_develop("$sherlockが$morianoについて説明する"),
            w.plot_turnpoint("$morianoが現れる"),
            w.plot_develop("$morianoは$sherlockに全てから手を引くよう警告する"),
            w.plot_turnpoint("$maryが人質として連れ去られる"),
            w.plot_develop("$morianoの手がかりを見つけ出し、$maryの居所を見つける"),
            w.plot_turnpoint("$maryを助け出す"),
            w.plot_develop("$sherlockは$maryたちを騙して単身$morianoの隠れ家に向かった"),
            w.plot_turnpoint("$sherlockから手紙が届く"),
            w.plot_resolve("$sherlockからの最後の手紙で彼が$morianoと共に穴に落ちたことを知る"),
            "序文",
            w.plot_note("（$wilsonの回顧録）あとになって考えるとこの事件が彼にとっての最後のものになるとは、当初は誰も考えていなかった"),
            w.plot_note("けれどこれまでの微々たる伏線を思い返せば、そうなるべくしてそうなった、と言わざるを得ない"),
            w.plot_note("その事件について、振り返ってみよう"),
            "不穏な空気",
            w.plot_note("あれから一ヶ月。$maryたちのいる暮らしにも慣れた"),
            w.plot_note("$limeが意外と料理を覚えるのが早くて、二人でわいわいやっている"),
            w.plot_note("$sherlockは新聞を見ながらうなっている"),
            w.plot_note("最近さまざまな、不可解な犯罪が増えている"),
            w.plot_note("そこに一通の書簡が届く"),
            w.plot_note("書簡には$morianoに注意されたしとだけ書かれていた"),
            w.plot_note("連絡が取れなくなった情報通のやり方で、彼が失踪したのも$morianoの手によるものだと$sherlock"),
            "$morianoについて",
            w.plot_note("$sherlockは$morianoについて語る"),
            w.plot_note("いくつか起こった犯罪事件"),
            w.plot_note("それらの裏には彼の名前があった。$morianoは直接手を下さないが、人を操って犯罪を起こす特殊な犯罪者だという"),
            w.plot_note("その彼が今なにかに執心していて、その計画には四つの$stoneが必要だということまで突き止められた"),
            w.plot_note("なんとかしてその先にある巨大な陰謀を阻止したいと$sherlock"),
            "$moriano出現",
            w.plot_note("呼び鈴が鳴り、$maryが応対に出るが、小さな悲鳴が上がる"),
            w.plot_note("そこには老人がいた。$morianoだと名乗った"),
            w.plot_note("$morianoは$sherlockに警告をする"),
            w.plot_note("計画の障害になる場合は容赦なく大事な人たちを殺すと"),
            w.plot_note("$sherlockは$gunを取り出すが、相手の方が早くそれを制する"),
            w.plot_note("$morianoは$maryを突き刺し、逃亡した"),
            w.plot_note("しかしそれは手品で、$maryは傷ひとつ付いていなかった"),
            "居場所を掴む",
            w.plot_note("それからしばらくして、情報が届く"),
            w.plot_note("それは遂に$morianoの居場所を突き止めたというものだった"),
            w.plot_note("$sherlockは単身で彼のところに向かい、全てを終わらせると語る"),
            w.plot_note("$wilsonたちは警察に任せればいいと説得しようとするが、警察にも$morianoの手下がいて、今までに何度も逃げられたのだと語る"),
            w.plot_note("$sherlockは「これが最後の事件になる」と語った"),
            "対決に備えて",
            w.plot_note("$sherlockは最後の晩餐めいたものをふるまう"),
            w.plot_note("普段は料理などしないが、そのサイエンスの知識をいかした料理をふるまう"),
            w.plot_note("$maryはそれが悲しくて泣き出す"),
            w.plot_note("それには睡眠薬が入っていて、みんなが寝てしまったのをベッドに移動させると、$sherlockは一人、夜の街に出た"),
            w.plot_note("あとの手はずを$ignesらに頼み、姿を消す"),
            "$sherlockが穴に落ちた",
            w.plot_note("彼が事前に出した手紙が届く"),
            w.plot_note("そこにはこの手紙が届いたということは自分が亡くなった可能性があると書かれている"),
            w.plot_note("$sherlockは自分を殺したのは$morianoで、彼が亡くなったときには新聞のある部分に知らせが出るとある"),
            w.plot_note("$wilsonがその知らせを見つける"),
            w.plot_note("$sherlockからの手紙には$morianoが倒れても彼の意志を貫くと"),
            w.plot_note("それに気になるところがあり、自分が知っている人間にその情報を探らせているともあった"),
            "まだ生きているはず",
            w.plot_note("$sherlockが本当になくなったとは信じたくない$maryは、探すと言い出して街に出ていく"),
            )


