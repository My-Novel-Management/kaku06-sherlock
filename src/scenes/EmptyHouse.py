# -*- coding: utf-8 -*-
'''
Stage: "空き家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   シャーロックがいたと言われる空き家。ホワイト・チャペル地区のスラム街にある。比較的ガワが残っていて、隣の家のように崩れてはいない
#   [キッチン][バス]
#   [寝室][寝室]
#   [リビング][応接間]
#   [玄関]


# alias
HOME = "EmptyHouse"

# Scenes
## in Empty House
def strange_empty_house(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    return w.scene("奇妙な空き家",
            w.change_stage(HOME),
            w.change_time("afternoon"),
            w.plot_note("$wilsonに連れられて$maryと$limeは$sherlockに似た人を見たという空き家にやってくる"),
            w.plot_note("バラックが並ぶスラム街にあるたくさんの空き家の一つ"),
            w.plot_note("見たというホームレスは夜にその空き家だけ明かりがつくのが妙だと思って監視していたと証言する"),
            mary.be(),
            wil.be(),
            lime.be(),
            )


def searching_empty_house(w: World):
    return w.scene("空き家の探索",
            w.plot_note("一度空き家の中を探索するが、確かに人が暮らしている証拠が見つかる"),
            w.plot_note("$maryたちは夜になるのを待った"),
            )


def night_and_light(w: World):
    return w.scene("夜の明かりと人影",
            w.plot_note("空き家に人影が入り、そこで明かりが灯る"),
            w.plot_note("明かりの人影は読書しているように見えた"),
            w.plot_note("もう一人の人間もいるようで、二人で会話をしている風でもある"),
            w.plot_note("しばらくするとその明かりは消えてしまう"),
            w.plot_note("誰も出てこないので、翌朝、$maryたちはその空き家に訪問してみる"),
            )


def silent_house(w: World):
    return w.scene("静まる空き家",
            w.plot_note("呼びかけても応答はなく、奥に入っていく"),
            w.plot_note("空き家の中で殺された男性の死体を発見した"),
            w.plot_note("それは先月から行方不明の神官だった"),
            w.plot_note("現場からは$sherlockの愛用していた手袋が発見される"),
            w.plot_note("警察は$sherlockを重要参考人として指名手配する"),
            )


def re_searching_house(w: World):
    return w.scene("空き家の再調査",
            w.plot_note("そこで$wilsonは抜け道を発見する"),
            )


def mystery_subway(w: World):
    return w.scene("謎多き地下道",
            w.plot_note("地下道に繋がっていて、そこを進んでいく"),
            )
