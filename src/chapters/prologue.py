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
            )


