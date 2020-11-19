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


# Episodes
def missing_persons(w: World):
    return w.episode("失踪者たち",
            "$maryは困っていたという謎の鎧騎士を連れてくる",
            )


def strange_work(w: World):
    return w.episode("不思議な仕事",
            "$sherlockは$limeにその仕事をすぐ辞めるように進言したが、理由は話さなかった",
            )


def bank_robbery(w: World):
    return w.episode("銀行強盗",
            "$limeが仕事を首になったらしいと$maryから伝え聞いた",
            )


def truth_of_club(w: World):
    return w.episode("クラブの真相",
            "$limeが助けてほしいとやってくる",
            )


def what_was_stolen(w: World):
    return w.episode("盗まれたもの",
            "$limeは自分が王室の人間であることを告白した",
            )


def new_living(w: World):
    return w.episode("新しい居候",
            "$limeが$sherlockたちの新しい居候になった",
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[3],
            w.plot_setup("失踪者のリストの中に第二王女も含まれている"),
            w.plot_turnpoint("$maryは困っている赤鎧の騎士を連れてくる"),
            w.plot_develop("$limeは赤鎧の人間にだけできる不思議なアルバイトをしていると告白する"),
            w.plot_turnpoint("$sherlockはすぐやめるよう忠告するが$limeは断れず続けてしまう"),
            w.plot_develop("大規模な強盗事件が発生し、$limeの店の主人が逮捕される"),
            w.plot_turnpoint("$limeは仕事をクビになる"),
            w.plot_develop("事情を聞いて、赤鎧クラブの仕組みを$sherlockが解説する"),
            w.plot_turnpoint("$sherlockはそのいなくなった同僚が犯人と指摘する"),
            w.plot_develop("犯人たちは既に逃げたあとで同僚の兵士は殺されて見つかった"),
            w.plot_turnpoint("$limeは事情があって王室に戻れないと告白した"),
            w.plot_resolve("$limeが$sherlockの家に居候することになった"),
            missing_persons(w),
            strange_work(w),
            bank_robbery(w),
            truth_of_club(w),
            what_was_stolen(w),
            new_living(w),
            )


