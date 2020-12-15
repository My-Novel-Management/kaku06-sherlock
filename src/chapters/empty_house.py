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
            # NOTE
            #   事件：空き家密室殺人／連続失踪事件
            #   被害者：$ronald卿
            #   容疑者：$sherlock
            #   犯人：$jake（$sherlockに似た$ajin）
            #   依頼者：$wilson？
            #   トリック：
            #   結果：
            #   ポイント：
            # TODO
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
            w.plot_develop("$limeは少年探偵団と協力して$maryを救出する"),
            w.plot_develop("$maryを人質に$sherlockを連れてくるよう要求される"),
            w.plot_develop("$sherlockを$wilsonが説得し、$maryと交換する"),
            w.plot_turnpoint("$sherlockが捕まる"),
            w.plot_develop("$sherlockは$heroだったと知られていて、儀式に利用される"),
            w.plot_develop("$maryたちは$sherlockを救出するために格方面に協力を仰ぐ"),
            w.plot_develop("儀式が修繕中の大聖堂の地下で行われると知り、警察を呼んで突入する"),
            w.plot_turnpoint("$patsonが裏切り者だった"),
            w.plot_develop("警察が入れなくなり、その間に$sherlockを捧げて儀式を敢行する$patson"),
            w.plot_develop("だが$stoneの一つがすり替えられていた為に儀式は失敗し、$patsonは死んでしまう"),
            w.plot_develop("$wilsonは$limeから本物の$stoneを受け取った"),
            w.plot_turnpoint("$wilsonは偽物だった"),
            w.plot_develop("偽$wilson（$zeron）により儀式の続きが行われる"),
            w.plot_develop("意識を取り戻した$sherlockは$wilsonにまだ儀式のために必要なものが揃っていないとブラフをかける"),
            w.plot_develop("$ignesたちに準備させていた爆弾を使い、施設を爆破する"),
            w.plot_develop("$stoneを粉々にし、突入した警官隊によって$wilsonは取り押さえられる"),
            w.plot_turnpoint("警察の留置所から$wilsonが逃亡する"),
            w.plot_resolve("山中の小屋で偽物$wilsonが自殺しているのが発見された"),
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


