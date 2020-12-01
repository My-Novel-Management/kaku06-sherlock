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
from scenes import MountCottage
from scenes import PoliceStation
from scenes import SherlockHouse
from scenes import SlumTown


# Episode
def lookfor_sherlock(w: World):
    return w.episode("$sherlockを探して",
            SherlockHouse.believed_his_alive(w),
            SherlockHouse.news_of_sherlock_alive(w),
            )


def empty_house(w: World):
    return w.episode("空き家の冒険",
            SlumTown.goto_empty_house(w),
            EmptyHouse.strange_empty_house(w),
            EmptyHouse.searching_empty_house(w),
            EmptyHouse.night_and_light(w),
            EmptyHouse.silent_house(w),
            )


def fake_reunion(w: World):
    return w.episode("偽りの再会",
            PoliceStation.interrogation(w),
            SherlockHouse.consideration_of_sherlock(w),
            EmptyHouse.re_searching_house(w),
            AbandonedFactory.many_dead(w),
            AbandonedFactory.sherlocks_confession(w),
            )


def in_the_darkness(w: World):
    return w.episode("暗闇の中で",
            AbandonedFactory.in_the_darkness(w),
            AbandonedFactory.desparete_escape(w),
            )


def his_alive(w: World):
    return w.episode("$sherlockは生きている",
            AbandonedFactory.hero_appairs(w),
            SherlockHouse.injured_wilson(w),
            )


def truth(w: World):
    return w.episode("真実",
            Hideout.visit_hideout(w),
            Hideout.sherlocks_talk(w),
            Church.cult_facility(w),
            Church.basement_hall(w),
            )


def strange_end(w: World):
    return w.episode("奇妙な結末",
            Church.unexpected_end(w),
            MountCottage.his_dead(w),
            w.plot_note("その後、警察の捜査により$sherlockが調べ上げた偽$wilsonが協力をしたと思われる人物リストを全て調査したが、全員失踪あるいは自殺、事故死していた"),
            w.plot_note("$sherlockは$wilsonの住居から何か情報がないかと探す"),
            w.plot_note("しかし偽$wilsonは何もかも綺麗に処分をしていた"),
            w.plot_note("ただ一つだけ、この世界のものとは思えないものを発見する"),
            w.plot_note("それは$wilsonが愛用していた謎の端末だった"),
            w.plot_note("$sherlockは確信するのだ。まだ偽$wilsonは生きていると"),
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
            lookfor_sherlock(w),
            empty_house(w),
            fake_reunion(w),
            his_alive(w),
            truth(w),
            strange_end(w),
            )


