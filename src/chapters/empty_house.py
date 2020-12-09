# -*- coding: utf-8 -*-
'''
Chapter "空き家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AbandonedFactory
from scenes import AbandonedHouse
from scenes import Church
from scenes import EmptyHouse
from scenes import Hideout
from scenes import Hospital
from scenes import Market
from scenes import MountCottage
from scenes import PoliceStation
from scenes import SherlockHouse
from scenes import SlumTown
from scenes import WilsonHouse


# Episode
def lookfor_sherlock(w: World):
    return w.episode("$sherlockを探して",
            SherlockHouse.believed_his_alive(w),
            Market.shal_disappearance_talk(w),
            Market.new_religions(w),
            SherlockHouse.news_of_sherlock_alive(w),
            )


def empty_house(w: World):
    return w.episode("空き家の冒険",
            SlumTown.goto_empty_house(w),
            EmptyHouse.strange_empty_house(w),
            EmptyHouse.resident_of_empty_house(w),
            EmptyHouse.night_and_light(w),
            EmptyHouse.silent_house(w),
            EmptyHouse.discover_dead(w),
            )


def fake_reunion(w: World):
    return w.episode("偽りの再会",
            PoliceStation.interrogation(w),
            PoliceStation.shal_is_suspect(w),
            SherlockHouse.consideration_of_sherlock(w).omit(),
            EmptyHouse.searching_house(w),
            EmptyHouse.mystery_subway(w),
            AbandonedFactory.many_dead(w),
            AbandonedFactory.sherlocks_confession(w).omit(),
            )


def in_the_darkness(w: World):
    return w.episode("暗闇の中で",
            AbandonedFactory.in_the_darkness(w),
            SherlockHouse.help_from_sherlock(w),
            AbandonedFactory.desparete_escape(w),
            SlumTown.rescue_mary(w),
            AbandonedFactory.hero_appairs(w),
            )


def his_alive(w: World):
    return w.episode("$sherlockの帰還",
            Hospital.shal_comes_back(w),
            SherlockHouse.injured_wilson(w).omit(),
            SherlockHouse.burned_shal_home(w),
            )


def truth(w: World):
    return w.episode("真実",
            Hideout.visit_hideout(w),
            Hideout.sherlocks_talk(w),
            Church.cult_facility(w),
            Church.lookfor_ritual_place(w),
            Church.goto_ritual_room(w),
            Church.basement_hall(w),
            )


def strange_end(w: World):
    return w.episode("奇妙な結末",
            Church.betray_man(w),
            MountCottage.his_dead(w),
            WilsonHouse.strange_end(w),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[7],
            w.plot_setup("$maryたちは$sherlockが生きていると信じて捜索を続けていた"),
            w.plot_turnpoint("$sherlockに似た人を空き家で見かけたという情報が入る"),
            w.plot_develop("空き家の調査を行い、そこで身元不明の遺体を発見する"),
            w.plot_turnpoint("空き家の遺体の犯人が$sherlockとして指名手配される"),
            w.plot_develop("$sherlockから$maryたちに秘密の連絡がある"),
            w.plot_turnpoint("$sherlock（偽物）に捕まえられ、$maryたちは監禁される"),
            w.plot_develop("$maryたちは暗闇に閉じ込められ、同じ手法で殺されそうになる"),
            w.plot_turnpoint("刑事の一人が改造$gunを使って殺そうとしたところを逮捕される"),
            w.plot_develop("助け出された$maryたちは$sherlockが生きていると$restradeから知らされる"),
            w.plot_turnpoint("$wilsonが指名手配される"),
            w.plot_develop("$sherlockと再会し、全ての事情を聞く"),
            w.plot_turnpoint("$wilsonが偽物だと$sherlockが教える"),
            w.plot_resolve("偽$wilsonが遺体となって発見された"),
            #
            "事件：空き家での密室殺人事件",
            "設定：$sherlock失踪？中で捜索中",
            "イベント：",
            "裏イベント：$boss復活の儀式（そのために$sherlockの心臓が必要）",
            "解決：$sherlockが$wilsonを偽物と見抜いた。ただ$wilsonは不思議な力で逃亡し、自殺した",
            #
            lookfor_sherlock(w),
            empty_house(w),
            fake_reunion(w),
            his_alive(w),
            truth(w),
            strange_end(w),
            )


