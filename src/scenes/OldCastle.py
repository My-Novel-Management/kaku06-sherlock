# -*- coding: utf-8 -*-
'''
Stage: "古城"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   魔獣伝説の古城。今は女城主が一人で暮らしている
#   招待され、パーティに参加するが、ここで殺人事件が発生する
#   古城内の部屋は基本こちらで扱う


## scenes
def sight_of_total(w: World):
    return w.scene("古城の全景",
            w.plot_note("丘の上の古城にたどり着く"),
            w.plot_note("城の案内をただ一人でここに住んでいるという女城主$cherryが行う"),
            )



def greeting_from_castle_owner(w: World):
    return w.scene("城主からの挨拶",
            w.plot_note("パーティのために料理人やお手伝いを呼んでいて、彼らが忙しくなく準備をしていた"),
            )


def murder_case_1st(w: World):
    return w.scene("最初の殺人事件",
            w.plot_note("慌てて駆けつけると、心霊専門家が殺されていた"),
            )


def investigation_in_castle(w: World):
    return w.scene("城内の探索",
            w.plot_note("$sherlockは$cherryに申し出て、城内を調べさせてもらう"),
            w.plot_note("一通り案内してもらい、部屋を見て回ったが特に何も見つからない"),
            )


def about_kitchen(w: World):
    return w.scene("台所について",
            )


def about_hall(w: World):
    return w.scene("大広間について",
            )


def about_backyard(w: World):
    return w.scene("裏庭について",
            )


def lookfor_moch(w: World):
    return w.scene("$mochを探せ",
            w.plot_note("いなくなた$mochが怪しいと招待客たちは探し始める"),
            )


def re_investigation_castle(w: World):
    return w.scene("再調査",
            w.plot_note("彼女はあまり気が進まないようだが許可を出す"),
            )
