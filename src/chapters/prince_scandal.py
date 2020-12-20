# -*- coding: utf-8 -*-
'''
Chapter "皇太子の醜聞"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AilyHouse
from scenes import CurioDealer
from scenes import InCar
from scenes import InCity
from scenes import Market
from scenes import Orphanage
from scenes import SherlockHouse
from scenes import Street
from scenes import StSarpentain


# Episodes
def visit_sherlock(w: World):
    return w.episode("訪問者",
            InCity.magic_and_tech_city(w),
            Street.baker_street(w),
            Street.he_is_sherlock(w),
            "$sherlockの家の中",
            SherlockHouse.about_sherlock(w),
            )


def prince_letter(w: World):
    return w.episode("皇太子からの密書",
            SherlockHouse.read_prince_letter(w),
            )


def that_lady(w: World):
    return w.episode("その女",
            InCar.goto_aily_house(w),
            StSarpentain.rumor_of_aily(w),
            AilyHouse.her_absence(w),
            AilyHouse.found_corpse(w),
            )


def murder_case(w: World):
    return w.episode("殺人事件",
            AilyHouse.hello_restrade(w),
            AilyHouse.investigation_aily_room(w),
            )


def orphanage(w: World):
    return w.episode("孤児院",
            InCar.goto_orphanage(w),
            Orphanage.a_orphanage(w),
            Orphanage.teachers_talk(w),
            Orphanage.secret_treasure(w),
            )


def she_is_not_exist(w: World):
    return w.episode("彼女は存在しない",
            CurioDealer.rumor_treasure_sword(w),
            Market.mystery_of_aily_corpse(w),
            SherlockHouse.important_than_sword(w),
            )


def her_the_identity(w: World):
    return w.episode("彼女の正体",
            Orphanage.investigation_her(w),
            Orphanage.aily_confession(w),
            )


def prince_wedding(w: World):
    return w.episode("皇太子の結婚式",
            Street.later_talk_of_aily(w),
            Street.prince_wedding(w),
            )



# Chapter
def main(w: World):
    return w.chapter(TITLES[1],
            # NOTE
            #   事件：密室殺人
            #   犠牲者：謎の女性　→本物の$aily
            #   容疑者：不明　→$aily
            #   犯人：自殺
            #   トリック：偽装（密室殺人に見せかけた自殺
            #   依頼人：皇太子
            #   結果：宝剣を取り戻したが肝心の$stoneは付いていなかった
            #   ポイント：$science技術／毒薬／$jack／$stone赤／王室
            w.plot_setup("謎の失踪事件が頻発していた"),
            w.plot_setup("街は$scienceにより技術革命が起こり、近代化が進んでいた"),
            w.plot_setup("街では怪盗$jackが富豪や国の宝を奪い、恵まれない人たちに寄付して回っていた"),
            w.plot_setup("$wilsonは第二王女失踪を極秘に調査してもらうために便利屋$sherlockの許を訪れる"),
            w.plot_setup("$sherlockは変わった男で$wilsonが話す前に全ての事情を推理して話し、自分は王室からの依頼は受けないと断った"),
            w.plot_turnpoint("皇太子から依頼の書簡が届く"),
            w.plot_develop("書簡にはある女性にプレゼントしてしまった宝剣を取り戻してほしいと書かれていた"),
            w.plot_develop("王室からの依頼は受けないはずの$sherlockだが、恩があるので依頼を受けると言う"),
            w.plot_develop("$sherlockは$wilsonとともに$ailyのことを調べる"),
            w.plot_turnpoint("$ailyの自宅で謎の殺人死体を発見した"),
            w.plot_develop("警察から$restradeと$patsonがやってきて、事件の担当であると告げる"),
            w.plot_develop("見つかった死体は最近頻発している謎の失踪事件の失踪者の一人だった"),
            w.plot_develop("密室殺人で、凶器も不明。$ailyが重要参考人として指名手配される"),
            w.plot_develop("$sherlockは皇太子の依頼そっちのけで密室殺人解決に興味を抱く"),
            w.plot_turnpoint("$ailyがよく寄付していた孤児院を知る"),
            w.plot_develop("孤児院で女教師（実は$jack）から$ailyがここ出身で如何に苦労して今の立場を得たかを聞く"),
            w.plot_develop("女教師から$ailyの無実を証明してくれたら、宝剣を返すよう説得すると約束された"),
            w.plot_develop("$sherlockは$ailyという女性について調べる"),
            w.plot_turnpoint("亡くなっていた女性が$ailyだと判明する"),
            w.plot_develop("警察は毒薬による自殺と発表して、事件を解決させようとした"),
            w.plot_develop("$sherlockは再度孤児院を訪れ、女教師と話す"),
            w.plot_develop("彼女が何故$ailyに偽装しなければならなかったかを語る$sherlock"),
            w.plot_turnpoint("女教師の正体が$jackと見抜く$sherlock"),
            w.plot_resolve("実は最初に書簡を配達した女配達員こそが$jackであり、最初に中身を見て自分に手が及ぶことを知っていた"),
            w.plot_resolve("本物の$ailyの死体については本当に自殺で、彼女の名誉のために$jackが偽装したのだと騙った"),
            w.plot_resolve("$jackは$sherlockに彼女から預かっていた宝剣を返して、自分は姿を消した"),
            w.plot_resolve("しかし取り戻した宝剣には$stoneが付いていなかった"),
            w.plot_resolve("皇太子は偽物の$stoneをつけた宝剣を使って婚姻の儀式を行った"),
            #
            visit_sherlock(w),
            prince_letter(w),
            that_lady(w),
            orphanage(w),
            she_is_not_exist(w),
            her_the_identity(w),
            prince_wedding(w),
            )


