# -*- coding: utf-8 -*-
'''
Chapter "プロローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episodes



# Chapter
def main(w: World):
    return w.chapter(TITLES[0],
            w.plot_setup("設定"),
            w.plot_turnpoint("TP"),
            w.plot_develop("展開"),
            w.plot_turnpoint("TP"),
            w.plot_resolve("結果"),
            #
            w.plot_setup("新聞を読んでいる$sherlock"),
            w.plot_setup("再び$bossが？という見出しに苦笑"),
            w.plot_setup("部屋に入ってきた$wilsonが「また何か面白そうな事件でも見つけたかね？」と問う"),
            w.plot_develop("$sherlockの御託並べが始まる"),
            w.plot_resolve("この物語は$sherlockという奇妙な若者との出会いの記録である"),
            w.plot_resolve("$wilsonが記述者で三人称で書き残したもの、という宣言"),
            w.plot_note("冒頭。城の前から始まる。$wilsonが魔導車に乗り込んで、行き先を告げる"),
            w.plot_note("これから会いに行く男$sherlockというのは実に変わり者だが役立つ男ですよ、と紹介する人間から教わる"),
            "プロローグとエピローグについては本物の$wilsonの行動と語りになる。だからここには作品本編そのものは書かないこと。内容を回想して触れる程度",
            "$wilsonの語り",
            w.plot_note("$wilsonは「役に立つ」という言葉の意味を考察する"),
            w.plot_note("今の時代を簡単に振り返る$wilson"),
            w.plot_note("魔導タクシーが走り始める"),
            w.plot_note("繁華街に出て、賑やかな、文明に溢れた街並み"),
            w.plot_note("産業革命と呼ばれた、と。$enegyを元とした$magicにより様々なものが動かせるようになった"),
            w.plot_note("近代化と呼ばれているが、それでもまだ人々の心のどこかではかつて存在した$bossへの脅威が見え隠れする"),
            w.plot_note("だからこそ人は$heroを未だに神聖視するのだろうと考える"),
            w.plot_note("$wilsonは手にしてものから$heroの紋章を見る"),
            w.plot_note("それから新聞を取り出してその見出しに注目する"),
            w.plot_note("見出しには失踪事件再びと"),
            "$hero関係の失踪者は簡単なリストを作る",
            w.plot_note("※ここで注釈が入る"),
            w.plot_note("本作は$sherlockとその仲間たちの活躍をまとめたもので、あとから情報を補足し「私」が記述したものだ"),
            w.plot_note("物語は「私」を含めてすべて三人称で記述され、読者が理解しやすいように時系列を整理して情報を並べてあるし、補足して書いてある"),
            w.plot_note("注釈後は「まもなく着きますよ」という声に微睡みから目覚めて、さてこの物語が始まる地点へと向かおうと"),
            )


