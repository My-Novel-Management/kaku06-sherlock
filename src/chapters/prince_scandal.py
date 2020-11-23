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


# Episodes
def visit_sherlock(w: World):
    return w.episode("訪問者",
            w.plot_note("$wilsonは$carで$sherlockの家の前までやってくる"),
            w.plot_note("$wilsonは近くにいた子供（$ignes）に家を尋ねて教えてもらう"),
            w.plot_note("そこで子供たちがもめ始めて、困惑"),
            w.plot_note("なんとか場が収まり、$sherlockの家を訪問する"),
            w.plot_note("$sherlockは何も言っていないのに$wilsonの素性を言い当てる"),
            w.plot_note("その上で王室からの依頼は受けないと言って断る"),
            w.plot_note("最後に「さっきの子供に財布をすられてるよ」と"),
            w.plot_note("$wilsonは振り返ったがもう子供たちの姿は消えていた"),
            w.plot_note("知っていたならなぜ忠告してくれなかったんだ、と$wilsonが$sherlockに文句をいい、なんとか家に入れてもらえる"),
            w.plot_note("中に入るとそこら中に本や資料がちらばっていた"),
            w.plot_note("$wilsonはそこで依頼をしようと思ったが、"),
            w.plot_note("そこに何も記載のない手紙が投げ込まれた"),
            )


def prince_letter(w: World):
    return w.episode("皇太子からの密書",
            w.plot_note("$sherlockは$wilsonにその女性の家まで送ってほしいと頼んだ"),
            )


def that_lady(w: World):
    return w.episode("その女",
            w.plot_note("女の家で謎の女性の遺体が発見された"),
            )


def she_is_not_exist(w: World):
    return w.episode("彼女は存在しない",
            w.plot_note("そこに$ailyという女が存在していた証拠は何もなかった"),
            )


def jack_the_identity(w: World):
    return w.episode("$jackの正体",
            w.plot_note("$jackは名前も戸籍も存在しない、悲しい捨て子だった"),
            )


def prince_wedding(w: World):
    return w.episode("皇太子の結婚式",
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
            she_is_not_exist(w),
            jack_the_identity(w),
            prince_wedding(w),
            )


