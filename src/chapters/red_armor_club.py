# -*- coding: utf-8 -*-
'''
Chapter "赤鎧クラブ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[3],
            w.plot_setup("$maryが居候し始めた"),
            w.plot_setup("買い物にでかけた先で口論からいざこざになったところを、謎の赤鎧の騎士に助けられる"),
            w.plot_setup("王国の第二王女が失踪して半年になっていた"),
            w.plot_turnpoint("その赤鎧の騎士が相談に訪れた"),
            w.plot_develop("騎士は話せず、筆記とジェスチャによる対話となる"),
            w.plot_develop("騎士が言うには自分はある護衛のアルバイトをしているが、護衛仲間に言われて赤鎧の者だけが資格のある報酬のいい短時間仕事をしている"),
            w.plot_develop("その仕事の奇妙さを誰にも相談できずにいたと"),
            w.plot_develop("$sherlockはしばらくそのまま続けるよう指示し、独自に調査を行う"),
            w.plot_turnpoint("赤鎧の騎士が再び訪れ、仕事を首になったと告白した"),
            w.plot_resolve("$sherlockは理由を話す"),
            w.plot_resolve("その店の店長と護衛仲間が共謀し、騎士を護衛場所から一定時間離れさせるのが目的だったと"),
            w.plot_resolve("警察により彼らは逮捕され、店を閉じたから解雇されてしまった"),
            w.plot_resolve("どうやら店の地下に穴を掘り、近所の博物館に展示中のあるものを盗むのが目的だった"),
            w.plot_resolve("しかしそれを偽物に取り替えておいた$sherlockの指示により犯人たちは捕まえられたのだ"),
            w.plot_resolve("事情を理解した騎士$limeは、自分のことについて語る"),
            w.plot_resolve("呪いの鎧を着ていたのは$limeという、かつて失踪した王国の第二王女だった"),
            w.plot_resolve("$limeは事情があり、王室には帰れないというので仕方なく$sherlockたちの家に居候することになった"),
            "奇妙な仕事",
            w.plot_note(""),
            "赤鎧クラブ",
            w.plot_note(""),
            "失踪した王女",
            w.plot_note("結局犯人たちは殺されて発見された"),
            w.plot_note("解雇された鎧騎士が家にやってくる"),
            w.plot_note("彼女は自分が失踪中の第二王女だと告白する"),
            w.plot_note("ただ事情があって王室には戻れないと言う"),
            w.plot_note("ここでしばらく置いてもらえないかと頼む$lime"),
            w.plot_note("$maryは友だちができて喜ぶ"),
            )


