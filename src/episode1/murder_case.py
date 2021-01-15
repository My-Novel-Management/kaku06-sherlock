# -*- coding: utf-8 -*-
'''
Episode 1-2: "殺人事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Scenes
# NOTE

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


# Episode
def main(w: World):
    return w.episode("殺人事件",
            # NOTE
            w.plot_setup("$ailyの家の中を調べる$sherlockと$wilson"),
            w.plot_turnpoint("寝室のドアを破壊して中を見ると知らない女の遺体が転がっていた"),
            w.plot_develop("事件として警察に届け出た後$sherlockは彼女が働いていたオペラハウスに向かう。そこで歌手$ailyのことを聞き込みした"),
            w.plot_turnpoint("$ailyが寄付していた孤児院の存在を知る"),
            w.plot_resolve("$sherlockは王子の言う性悪女$ailyと周囲の評判のいい$ailyのギャップに違和感を覚える"),
            w.plot_turnpoint("警察が$ailyを指名手配にしたことを知った"),
            outline=ABSTRACT)

