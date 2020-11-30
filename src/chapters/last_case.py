# -*- coding: utf-8 -*-
'''
Chapter "最後の事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AbandonedHouse
from scenes import InCar
from scenes import InCity
from scenes import Market
from scenes import MorianoHouse
from scenes import SherlockHouse
from scenes import SteinHouse


# Episode
def the_fixer(w: World):
    return w.episode("事件の黒幕",
            SherlockHouse.commision_of_murder_case(w),
            InCar.goto_incident_scene(w),
            SteinHouse.case_of_house(w),
            )


def about_moriano(w: World):
    return w.episode("$morianoについて",
            SteinHouse.restrade_meets(w),
            SteinHouse.about_moriano(w),
            )


def his_warning(w: World):
    return w.episode("$morianoの警告",
            SherlockHouse.moriano_is_here(w),
            )


def lookfor_mary(w: World):
    return w.episode("$maryの捜索",
            SherlockHouse.marys_strange(w),
            Market.strange_letter(w),
            SherlockHouse.where_is_mary(w),
            InCity.goto_moriano(w),
            MorianoHouse.broken_fire(w),
            SherlockHouse.alive_moriano(w),
            )


def rescue_mary(w: World):
    return w.episode("$mary救出劇",
            SherlockHouse.morianos_whereabouts(w),
            AbandonedHouse.awaking_mary(w),
            AbandonedHouse.escape_from_danger(w),
            SherlockHouse.vanished_sherlock(w),
            )


def his_letter(w: World):
    return w.episode("$sherlockからの手紙",
            SherlockHouse.sherlocks_information(w),
            SherlockHouse.no_sherlock_life(w),
            SherlockHouse.serching_sherlock(w),
            SherlockHouse.arrived_his_message(w),
            )


def sad_news(w: World):
    return w.episode("悲しいお知らせ",
            SherlockHouse.sadness_report(w),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[6],
            w.plot_setup("$sherlockは全ての黒幕として$morianoに辿り着く"),
            w.plot_turnpoint("$morianoのメッセージ（暗号）が新聞に掲載される"),
            w.plot_develop("$sherlockが$morianoについて説明する"),
            w.plot_turnpoint("$morianoが現れる"),
            w.plot_develop("$morianoは$sherlockに全てから手を引くよう警告する"),
            w.plot_turnpoint("$maryが人質として連れ去られる"),
            w.plot_develop("$morianoの手がかりを見つけ出し、$maryの居所を見つける"),
            w.plot_turnpoint("$maryを助け出す"),
            w.plot_develop("$sherlockは$maryたちを騙して単身$morianoの隠れ家に向かった"),
            w.plot_turnpoint("$sherlockから手紙が届く"),
            w.plot_resolve("$sherlockからの最後の手紙で彼が$morianoと共に穴に落ちたことを知る"),
            the_fixer(w),
            about_moriano(w),
            his_warning(w),
            lookfor_mary(w),
            rescue_mary(w),
            his_letter(w),
            sad_news(w),
            )


