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
            "孤児院",
            w.plot_note("数日後、$sherlockは再び孤児院を訪れていた"),
            w.plot_note("事件は暗礁に乗り上げ、$ailyを重要参考人として警察が探しているらしい、という情報だけが$sherlockに届いた"),
            w.plot_note("$sherlockは孤児院の女教師に話しかける"),
            w.plot_note("$ailyさんですね、と"),
            w.plot_note("彼女は観念し、孤児院の裏庭に出て話す"),
            "同・裏庭",
            w.plot_note("宝剣についてはすぐに返すつもりだったが、それが価値あるものと知り、お金に変えた"),
            w.plot_note("この孤児院を存続させたいがための行動だった"),
            w.plot_note("$sherlockはあの宝剣が本物だったことを告げると、彼女は子供たちを呼びつける"),
            w.plot_note("その子どもたちに囲まれている間に彼女は姿を消してしまった"),
            w.plot_note("$sherlockは子供たちからここに寄付している本当の人間の名前を聞く"),
            w.plot_note("それは$jackという、巷で噂の盗賊だった"),
            )


def prince_wedding(w: World):
    return w.episode("皇太子の結婚式",
            "$sherlockの家",
            w.plot_note("殺人の謎は改造された$gunの発見により、犯人はわからないまま、解決された"),
            w.plot_note("$sherlockは犯人はプロの人間だろうという"),
            w.plot_note("そもそも$jackと関係していたかどうか分からないし、それを追うための情報もないと"),
            w.plot_note("更に彼女があの宝剣ではなく、そこにはまっていた$stoneを売り払ったのだと分かった"),
            w.plot_note("一番大事な$stoneが偽物とわかり、どうするか問題となった"),
            "メインストリート",
            w.plot_note("偽物の$stoneを使い、無事に皇太子の結婚式は行われた"),
            )



# Chapter
def main(w: World):
    return w.chapter(TITLES[1],
            w.plot_setup("$wilsonはある依頼をするために$sherlockを訪れる"),
            w.plot_turnpoint("皇太子からの書簡により$sherlockはそちらの依頼を受けることになる"),
            w.plot_develop("$sherlockは皇太子が贈った宝剣を取り戻すために$ailyの家を訪れる"),
            w.plot_turnpoint("$ailyの家で女の遺体が発見される"),
            w.plot_develop("$ailyの友人という女性に出会い、彼女の話を聞く"),
            w.plot_turnpoint("遺体は$ailyと認められた"),
            w.plot_develop("$sherlockは彼女が実在した証拠をつかみ、調べていく"),
            w.plot_turnpoint("$ailyは存在しない女だった"),
            w.plot_develop("$jackを追い詰めて$sherlockは何とか宝剣を取り戻す"),
            w.plot_turnpoint("しかし取り戻した宝剣には肝心の$stoneが付いていなかった"),
            w.plot_resolve("皇太子は偽物の$stoneをつけた宝剣を使い、婚姻の儀を終わらせた"),
            visit_sherlock(w),
            prince_letter(w),
            that_lady(w),
            orphanage(w),
            she_is_not_exist(w),
            her_the_identity(w),
            prince_wedding(w),
            )


