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
            w.plot_setup("$scienceにより夜でも明るい街"),
            w.plot_setup("$bossが$heroによって倒され、世界は人間が溢れていた"),
            w.plot_setup("それでも問題は山積で、$wilsonはそんな問題に頭を悩ませている一人"),
            w.plot_develop("$wilsonは馴染みのバーに立ち寄る"),
            w.plot_turnpoint("$wilsonに声をかける$stan"),
            w.plot_develop("$wilsonは今時分が王室から色々と頼まれて厄介事を解決する部署にいると話す"),
            "お互いに雰囲気が変わった、と話す",
            w.plot_develop(""),
            w.plot_turnpoint("知人の$stanから便利屋$sherlockのことを教わる"),
            )


def handyman_sherlock(w: World):
    return w.episode("便利屋$sherlock",
            w.plot_setup("翌朝、$sherlockの家に向かう$wilson"),
            w.plot_setup("$sherlockの家は$Baker街にある"),
            w.plot_develop("$carを準備して、$sherlockの家に向かう"),
            w.plot_develop("産業革命が起こり、街は急成長している"),
            w.plot_develop("ただところどころに旧時代の名残がある"),
            w.plot_turnpoint("$carから降りると子供たち（$ignes）に囲まれる"),
            w.plot_develop("$wilsonは"),# TODO
            w.plot_turnpoint("何とか$sherlockの家のドアをノックした"),
            )


def note_for_novel(w: World):
    return w.episode("作品のための注意書き",
            w.plot_setup(""),
            w.plot_resolve(""),
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


