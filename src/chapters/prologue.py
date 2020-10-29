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


## chapter
def main(w: World):
    return w.chapter(TITLES[0],
            w.plot_setup("新聞を読んでいる$sherlock"),
            w.plot_setup("再び$bossが？という見出しに苦笑"),
            w.plot_setup("部屋に入ってきた$wilsonが「また何か面白そうな事件でも見つけたかね？」と問う"),
            w.plot_develop("$sherlockの御託並べが始まる"),
            w.plot_resolve("この物語は$sherlockという奇妙な若者との出会いの記録である"),
            w.plot_resolve("$wilsonが記述者で三人称で書き残したもの、という宣言"),
            "冒頭。$wilsonが魔導車に乗り込んで、行き先を告げる",
            "通りを進みながら、文明や魔導技術、産業革命に溢れた街並みを見せる",
            "市場を通る",
            "それから回想のように語りが始まる",
            "これは私がある変わった男との出会いを通じて、様々な冒険と謎解きに遭遇した物語をまとめたものだ",
            "最後に、物語は原則三人称で記述され、記述者である私もそこに含まれることを示す",
            "それから後から仕入れた情報もそこに加えられ、脚色された文章と物語進行となっていることも示す",
            "そして私の存在は一応明かさない。そのうちに分かるだろう、とだけ書かれている",
            )


