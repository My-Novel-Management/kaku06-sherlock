# -*- coding: utf-8 -*-
'''
Stage: "市場"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   立っている市場はどこでもここを使う。基本は古くから立っている賑わいのあるバラ市場


## scenes
def mystery_of_aily_corpse(w: World):
    return w.scene("$aily家の遺体の謎",
            w.plot_note("ただ謎の殺人事件と消えた$ailyについての謎が残った"),
            )


def shopping_enjoy(w: World):
    return w.scene("楽しいお買い物",
            w.plot_note("$maryは料理はあいかわらず下手だが、それでもよく市場に顔を出して買い物をしていた"),
            w.plot_note("$maryは今日も市場に出かける"),
            w.plot_note("この町の市場の賑わいが$maryは好きだった"),
            w.plot_note("市場には少年探偵団の$ignesも働いている"),
            w.plot_note("最近仲良くなった果物屋の$nowlisから友人からガチョウをもらったと言ってそれを分けてもらえた"),
            w.plot_note("$maryはガチョウを持って帰る"),
            )


def wanted_jack(w: World):
    return w.scene("$jackが指名手配",
            w.plot_note("$jackが改めてその殺人事件の容疑者として手配される"),
            )


def goose_jewely_mystery(w: World):
    return w.scene("ガチョウの宝石の謎",
            w.plot_note("その間に$maryたちはガチョウの中から出てくる宝石の謎を追いかける"),
            )


def meatshop_talk(w: World):
    return w.scene("肉屋の話",
            w.plot_note("肉屋の主人からどこでガチョウを仕入れてくるのかを聞いた"),
            w.plot_note("その経路を辿っていくと、飼育業者がその一箇所だと断定できた"),
            )


def wholesaler_talk(w: World):
    return w.scene("卸売業者の話",
            w.plot_note("飼育業者のおじさんに聞いてもダイヤを餌に混ぜたりはしていないと"),
            w.plot_note("仲介業者も卸業者も全然入る余地がなく、結局何も情報を得られないまま帰ってきた"),
            )