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
from scenes import ReadingRoom
from scenes import WilsonHouse


# Episodes
# NOTE
#   .問題はいつも山積み＞便利屋$sherlock
#   .便利屋$sherlock＞$sherlockの家の前までやってきた
#   .注意書き


def troublesome(w: World):
    return w.episode("厄介事",
            )


def handyman_sherlock(w: World):
    return w.episode("便利屋$sherlock",
            )


def note_for_novel(w: World):
    return w.episode("作品のための注意書き",
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[0],
            w.plot_setup("$wilsonは王室からいろいろな厄介事を頼まれる存在"),
            w.plot_turnpoint("最近続いている謎の失踪事件の調査を頼まれる"),
            w.plot_develop("新聞を見ながら趣味でやっている日記を書き始める"),
            w.plot_turnpoint("$sherlockという男が街の便利屋という噂を知ったところから物語は始まる"),
            w.plot_resolve("$sherlockの家を訪問する$wilson"),
            #
            troublesome(w),
            handyman_sherlock(w),
            note_for_novel(w),
            )


