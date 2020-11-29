# -*- coding: utf-8 -*-
'''
Chapter "魔獣"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import Bar
from scenes import BasementInCastle
from scenes import BedroomInCastle
from scenes import Church
from scenes import InShip
from scenes import InTrain
from scenes import Island
from scenes import Library
from scenes import LoungeInCastle
from scenes import OldCastle
from scenes import Port
from scenes import SherlockHouse
from scenes import Station
from scenes import Street


# Episodes
def legend_of_darkdog(w: World):
    return w.episode("魔獣伝説",
            SherlockHouse.mysterious_case(w),
            SherlockHouse.legend_of_dark_dog(w),
            SherlockHouse.invitation_from_dark_island(w),
            )


def first_murder(w: World):
    return w.episode("最初の犠牲者",
            Station.goto_dark_island(w),
            InTrain.talk_about_dark_island(w),
            Port.goto_dark_island(w),
            InShip.goto_dark_island(w),
            Island.legendary_island(w),
            Island.copse_of_murder(w),
            Island.walk_slope_for_castle(w),
            OldCastle.sight_of_total(w),
            OldCastle.greeting_from_castle_owner(w),
            LoungeInCastle.invited_guests(w),
            BedroomInCastle.marys_enjoy(w),
            OldCastle.murder_case_1st(w),
            )


def second_murder(w: World):
    return w.episode("第二の犠牲者",
            LoungeInCastle.isolation_us(w),
            OldCastle.investigation_in_castle(w),
            OldCastle.about_kitchen(w),
            OldCastle.about_hall(w),
            OldCastle.about_backyard(w),
            Island.research_first_murder_case(w),
            BedroomInCastle.vanishing_moch(w),
            )


def exist_darkdog(w: World):
    return w.episode("魔獣は存在する",
            OldCastle.lookfor_moch(w),
            Island.second_dead(w),
            LoungeInCastle.island_history(w),
            )


def basement_room(w: World):
    return w.episode("地下室",
            Island.call_rescue(w),
            OldCastle.re_investigation_castle(w),
            LoungeInCastle.find_basement_room(w),
            BasementInCastle.goto_basement_stairs(w),
            BasementInCastle.torture_room(w),
            )


def real_murder(w: World):
    return w.episode("犯人",
            BasementInCastle.confession_criminal(w),
            )


def sad_end(w: World):
    return w.episode("悲しい結末",
            BasementInCastle.runaway_cherry(w),
            LoungeInCastle.truth_of_the_case(w),
            )


def rebirth_ritual(w: World):
    return w.episode("蘇りの技法",
            BasementInCastle.ritual_room(w),
            Library.ancient_method(w),
            Church.mystery_cult(w),
            Street.back_street(w),
            Bar.underground_informater(w),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[5],
            w.plot_setup("魔獣伝説のある場所で猟奇殺人事件が起こる"),
            w.plot_turnpoint("$sherlockの許にその孤島のパーティの招待状が届く"),
            w.plot_develop("$restradeの弟から事件解明を頼まれる"),
            w.plot_turnpoint("最初の殺人事件が起こる"),
            w.plot_develop("海は荒れて脱出も不可能になり、招待客は島に閉じ込められる"),
            w.plot_turnpoint("第二の被害者が出る"),
            w.plot_develop("$sherlockは獣による犯行ではないとして調査を開始する"),
            w.plot_turnpoint("本物の魔獣が出現する"),
            w.plot_develop("魔獣を殺そうとするが女主人が体を張って守ろうとする"),
            w.plot_turnpoint("$sherlockは女主人が犯人だと説明する"),
            w.plot_develop("女主人は魔獣とともに脱出を試みる"),
            w.plot_turnpoint("魔獣は女主人を食べてしまった"),
            w.plot_resolve("蘇りの秘法を使って$boss復活を願う宗教団体だったと判明する"),
            legend_of_darkdog(w),
            first_murder(w),
            second_murder(w),
            exist_darkdog(w),
            basement_room(w),
            real_murder(w),
            sad_end(w),
            rebirth_ritual(w),
            )


