# -*- coding: utf-8 -*-
'''
Episode 1-2: "殺人事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "殺人事件"


# NOTE: outlines
ABSTRACT = """
家の中に入る$sherlock。そこで謎の女性の遺体を発見する。
すぐ警察に連絡する。警察が到着するまでに$sherlockは部屋を調査する。
強盗に荒らされた部屋。寝室。だが台所は綺麗だった。まるで新品のよう。
一人暮らしと聞いていたが、食器もない。色々と奇妙だった。
やってきた警察は$restradeで$sherlockもよく知る人物だった。
凶器は落ちていたナイフで、亡くなっていた女性が$ailyかどうか、オペラ座の座長にきてもらい確かめてもらったが、$ailyではなかった。
警察は家主の$ailyを参考人として指名手配する。
"""


# Scenes


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$ailyの家の中を調べる$sherlockと$wilson"),
            w.plot_turnpoint("寝室のドアを破壊して中を見ると知らない女の遺体が転がっていた"),
            w.plot_develop("事件として警察に届け出た後$sherlockは彼女が働いていたオペラハウスに向かう。そこで歌手$ailyのことを聞き込みした"),
            w.plot_turnpoint("$ailyが寄付していた孤児院の存在を知る"),
            w.plot_resolve("$sherlockは王子の言う性悪女$ailyと周囲の評判のいい$ailyのギャップに違和感を覚える"),
            w.plot_turnpoint("警察が$ailyを指名手配にしたことを知った"),
            w.plot_note("家の中に入った$sherlockは表情が引き締まる"),
            w.plot_note("静まり返った家の中"),
            w.plot_note("物はほとんど置かれていない"),
            w.plot_note("まるで新居のよう。引っ越してくる前の"),
            w.plot_note("「彼女は綺麗好きなんだね」と$wilson。それに対して「観察眼がない」と$sherlock"),
            w.plot_note("ほとんどものがない棚にはうっすらホコリがある"),
            w.plot_note("リビングには小さなテーブル"),
            w.plot_note("いくつか部屋があるが、どれも使われてない"),
            w.plot_note("キッチンはわずかに使用形跡がある"),
            w.plot_note("最新機器の冷蔵庫があった。$scienceの力で冷気を巡回させて一定温度に保つらしい。だが中身はない。飲み物のボトルだけ"),
            w.plot_note("棚に酒がいくつか並ぶ"),
            w.plot_note("奥の寝室らしき部屋のドアだけが施錠されていた"),
            w.plot_note("ノックして応答を確かめる$sherlock。だが何もない"),
            w.plot_note("$sherlockは花瓶を取り出して鍵のところを破壊する"),
            w.plot_note("「こういうのは後であいつらに請求することになっている」と"),
            w.plot_note("室内に入ると、すぐにベッドの上で女性が倒れているのが見つかる"),
            w.plot_note("胸にナイフが突き立てられて亡くなっている"),
            w.plot_note("「密室殺人だ」と$sherlockは言った"),
            #
            w.plot_note("警察がやってくる"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

