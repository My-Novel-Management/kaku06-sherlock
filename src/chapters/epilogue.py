# -*- coding: utf-8 -*-
'''
Chapter "エピローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[-1],
            w.plot_setup("$wilsonが偽物だったと$sherlockが説明する"),
            w.plot_setup("偽$wilsonは最初から$sherlockが$heroと知って近づき、$boss復活に利用しよとした"),
            w.plot_turnpoint("本物の$wilsonが現れる"),
            w.plot_develop("$wilsonは$sherlockたちから全ての事情を聞く"),
            w.plot_develop("$wilsonは$sherlockの仕事を手伝うという"),
            w.plot_develop("$sherlockは立ち退きを命じられている"),
            w.plot_turnpoint("$wilsonが金策の提案をする"),
            w.plot_resolve("$wilsonは$sherlockの活躍を本にして出版することにした"),
            w.plot_resolve("正式に探偵事務所$heroとして営業を開始した"),
            #
            w.plot_setup("一連の事件の黒幕が$morianoではなく$wilsonだったと$sherlockは語る"),
            w.plot_turnpoint("本物の$wilsonがやってくる"),
            w.plot_develop("$wilsonは既に解決した事件の正式な書簡を見せ、$sherlockに仕事を依頼しようとする"),
            w.plot_develop("事情を全て聞かされた$wilson"),
            w.plot_turnpoint("そんな$wilsonに新しい書簡が届く"),
            w.plot_resolve("勇者直系の国王が暗殺されたという"),
            w.plot_resolve("その調査を依頼されるのだ"),
            w.plot_resolve("王室からの依頼は受けないといっていたが、それが自分の兄だと知り、仕方なく出向くことになった"),
            "全ての顛末",
            w.plot_note("事件は偽$wilsonが仕組んでいた「$boss復活」のための一連のものだったと判明する"),
            w.plot_note("失踪していた$heroの末裔たちはみな施設の裏庭に白骨となって見つけられた"),
            w.plot_note("$morianoの自宅からは$wilsonと思われる人物と会ったことを記した手記が見つかり、それにより彼との関係が明らかとなった"),
            "本物の$wilson",
            w.plot_note("そして長い旅行から帰ってきた本物の$wilsonがやってくる"),
            w.plot_note("「はじめまして」と挨拶する"),
            w.plot_note("顔立ちも全然違ったし、事情もよく知らなかったが、$maryたちに教わる"),
            "これからの物語",
            w.plot_note("ここまで書いてきたのは全て$wilsonである、と告白"),
            w.plot_note("$wilsonの本業はライターである"),
            w.plot_note("全てを聞いたあとに多少書き加えた"),
            w.plot_note("偽物の$wilsonの目的こそ阻止できたが、また別の誰かが蘇らせないとも限らない"),
            w.plot_note("$sherlockはあれだけ嫌がっていた冒険に出る必要もあると言い出したが、今日も本を読んでいる"),
            w.plot_note("しかしそんな彼のもとにまた奇妙な事件の依頼が訪れた"),
            w.plot_note("それはまた別の物語としよう"),
            )


