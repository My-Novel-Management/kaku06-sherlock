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
            # NOTE
            #   事件：犬による猟奇殺人／孤島の招待客連続殺人
            #   被害者：数名の地域の人／
            #   容疑者：伝説の魔犬
            #   犯人：$cherry（犬の餌として必要だった）
            #   依頼人：城主の$cherry
            #   トリック：偽装（歯型の凶器を使い、犬がやったように見せかけた
            #   結果：二人が死亡（うち一人は共犯）、城主の$cherryは飼い犬に食い殺され、魔犬は射殺
            #   ポイント：蘇りの$sorcery／$stone黒の行方情報（闇オークションに出回った）
            w.plot_setup("その島では魔獣伝説が残っていた"),
            w.plot_setup("実際に近年も犬に食い殺されたような猟奇殺人が発生している"),
            w.plot_setup("$sherlockは特集記事を読みながらも怪奇伝説や幽霊は信じないと豪語する"),
            w.plot_turnpoint("$sherlockのもとにその孤島からパーティの紹介状が届く"),
            w.plot_develop("$sherlockたちは船で孤島に渡る"),
            w.plot_develop("城の主である$cherryは島に人が戻ってくるようにと、探偵や心霊研究家などに声を掛けて集めた"),
            w.plot_develop("それぞれ伝説について持論を展開する"),
            w.plot_develop("$sherlockは観光課の職員$mochに最初の事件があった場所に案内してもらう"),
            w.plot_develop("事件があった雑木林は立て札が立てられ、整備されてしまっていた"),
            w.plot_develop("観光課の$mochは観光によって人を呼び戻したいと言う"),
            w.plot_develop("夜、地元の学者からこの島がどこかの魔族の成れの果てが落ち延びてきた場所だと話す"),
            w.plot_turnpoint("翌朝、事件解決専門家が酷い姿で発見される"),
            w.plot_develop("警察を呼ぼうということになるが、海が荒れていて船を出せない"),
            w.plot_develop("元刑事は自分たちの力で問題解決しようと提案する"),
            w.plot_develop("心霊研究家は魔犬が出たと騒ぐ"),
            w.plot_develop("$sherlockは事件があった部屋を調べる"),
            w.plot_develop("確かに犬のような獣に仕業に見えたが、少し気になる部分があると$sherlockは言った"),
            w.plot_develop("$sherlockは$cherryに許可をもらい、城内を調べて回る"),
            w.plot_develop("古い城で、アンティークな鎧や槍、剣などの飾りがあった"),
            w.plot_turnpoint("何も情報が得られずホールに戻ると、元刑事が心霊研究家を犯人にしたてていた"),
            w.plot_develop("実は心霊研究家ではなく、詐欺師だったのだ"),
            w.plot_develop("その人物を個室に閉じ込めて、事件解決したことにした元刑事"),
            w.plot_develop("$sherlockは厨房に向かい、パーティのために呼ばれた料理担当と昨日のアリバイを聞く"),
            w.plot_develop("手配はすべて観光課の$mochが行ったと聞いた"),
            w.plot_develop("夜、情報を整理する$sherlock"),
            w.plot_turnpoint("翌朝、$mochが失踪した"),
            w.plot_develop(""),# TODO
            w.plot_resolve(""),
            #
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


