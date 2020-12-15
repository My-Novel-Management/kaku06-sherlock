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
from scenes import JakinsHouse
from scenes import Museum
from scenes import PawnShop
from scenes import SherlockHouse
from scenes import Street


# Episodes
def missing_persons(w: World):
    return w.episode("失踪者たち",
            SherlockHouse.housemate_mary(w),
            SherlockHouse.mary_has_worry(w),
            SherlockHouse.about_missings(w),
            SherlockHouse.strange_armor_knight(w),
            )


def strange_work(w: World):
    return w.episode("不思議な仕事",
            SherlockHouse.strange_work(w),
            )


def bank_robbery(w: World):
    return w.episode("銀行強盗",
            Street.mary_walked_lime(w),
            PawnShop.limes_job_place(w),
            JakinsHouse.orners_home(w),
            SherlockHouse.reason_for_lime_work(w),
            )


def truth_of_club(w: World):
    return w.episode("クラブの真相",
            SherlockHouse.help_lime_please(w),
            Street.meaning_for_his_advice(w),
            Museum.alibi_proof(w),
            )


def what_was_stolen(w: World):
    return w.episode("盗まれたもの",
            JakinsHouse.orners_talk(w),
            SherlockHouse.limes_talk_of_strange_case(w),
            )


def new_living(w: World):
    return w.episode("新しい居候",
            SherlockHouse.lime_was_royal_family(w),
            SherlockHouse.newcommer_lime(w),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[3],
            # NOTE
            #   事件：赤鎧クラブという奇妙な仕事　→銀行強盗／バイトの$bins殺害
            #   被害者：銀行の大金庫の宝石群／$bins
            #   容疑者：オーナー夫婦／$lime
            #   犯人：$binsたち強盗団／強盗団（$bins殺害）
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


