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
# NOTE
#   .皇太子の依頼＞書簡到着
#   .謎の女＞遺体発見
#   .密室殺人＞容疑者$aily
#   .女と孤児院＞$ailyは死んでいた
#   .怪盗$jack＞宝剣を取り戻した
#   .皇太子の結婚式

# NOTE
#   ・$sherlockの家（初出。
#   ・$sherlock（顔出しなど初めて。格好、特に帽子や姿勢を詳しく描写。ロリポップを咥えている
#   ・皇太子（名前のみ。結婚式で遠くから姿は見える

def prince_matter(w: World):
    return w.episode("皇太子の問題",
            "ここで$sherlockは自分の血液を研究していることを見せる",
            w.plot_turnpoint("皇太子から書簡が届く"),
            )


def mysterious_lady(w: World):
    return w.episode("謎めいた女",
            w.plot_turnpoint("居間に謎の女性の遺体が転がっていた"),
            )


def locked_room_murder(w: World):
    return w.episode("密室殺人",
            w.plot_turnpoint("$ailyが寄付していた孤児院の場所を突き止めた"),
            )


def lady_of_orphanage(w: World):
    return w.episode("孤児院の女",
            w.plot_turnpoint("$ailyという女はもともと存在していないことが分かった"),
            )


def phantom_thief_jack(w: World):
    return w.episode("怪盗$jack",
            w.plot_setup(""),
            w.plot_turnpoint("$jackは$sherlockに負けを認めて宝剣の隠し場所を教えた"),
            )


def prince_wedding(w: World):
    return w.episode("皇太子の結婚",
            w.plot_setup(""),
            w.plot_turnpoint("宝剣にハマっている$stoneが偽物だと判明した"),
            w.plot_resolve("知り合いの宝石技師$casselにより、精巧なレプリカを作ってもらう"),
            w.plot_resolve("皇太子は偽物の$stoneを使った宝剣で、無事に結婚式を済ませた"),
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
            prince_matter(w),
            mysterious_lady(w),
            locked_room_murder(w),
            lady_of_orphanage(w),
            phantom_thief_jack(w),
            prince_wedding(w),
            )


