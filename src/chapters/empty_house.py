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
from scenes import InCar
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
            InCar.goto_wilson_house(w),
            WilsonHouse.this_is_wilson_house(w),
            )


def purpose_of_cases(w: World):
    return w.episode("事件の本当の目的",
            WilsonHouse.search_wilson_house(w),
            WilsonHouse.secret_of_sherlock(w),
            WilsonHouse.sherlocks_request(w),
            InCar.about_this_cases(w),
            )


def truth(w: World):
    return w.episode("真実",
            Hideout.visit_hideout(w).omit(),
            Hideout.sherlocks_talk(w).omit(),
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
            w.plot_setup("$sherlockが死んだことを信じられず、$maryたちは彼の捜索を続けていた"),
            w.plot_setup("$morianoがいなくなったが同時に$sherlockも消えたことで、世間では犯罪が激増していた"),
            w.plot_setup("新興宗教団体$cultXが勢力を増して、街の至るところで信者を見かけるようになった"),
            w.plot_setup("地震があり、大聖堂が修繕工事をしている"),
            w.plot_turnpoint("$wilsonが$sherlockを目撃したという情報を持ってくる"),
            w.plot_develop("$maryたちは$sherlockが入るのを見たという空き家を監視する"),
            w.plot_develop("空き家で二人が争う影を見る"),
            w.plot_develop("翌朝、失踪中だった大司祭の遺体が発見される"),
            w.plot_turnpoint("$sherlockが殺人事件の容疑者として手配される"),
            w.plot_develop("$maryは$sherlockの容疑を晴らすために空き家を調べる"),
            w.plot_develop("空き家に抜け道を発見し、それが廃工場に繋がっていた"),
            w.plot_develop("廃工場では失踪者の遺体が発見される"),
            w.plot_turnpoint("$sherlockに似た男に$maryは拉致・監禁される"),
            w.plot_develop(""),
            # TODO
            w.plot_turnpoint("$wilsonが偽物だった"),
            w.plot_resolve("偽$wilson（$zeron）は$sherlockの血を使い、$boss復活を行う"),
            w.plot_resolve("しかし$stoneの一つが偽物にすり替えられていて儀式は失敗し、$wilsonは大怪我を負う"),
            w.plot_resolve("用意していた警察隊が突入するが、$zeronは$sorceryにより脱出し、逃亡した"),
            w.plot_resolve("山中の小屋で偽物$wilsonが自殺しているのが発見された"),
            #
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
            purpose_of_cases(w),
            truth(w),
            strange_end(w),
            )


