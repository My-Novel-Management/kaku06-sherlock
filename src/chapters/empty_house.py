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


## chapter
def main(w: World):
    return w.chapter(TITLES[7],
            "ベックマン街の空き家",
            w.plot_setup("穴に落ちた$sherlockがどこかで生きていると信じて探す$maryたち"),
            w.plot_setup("しかし一ヶ月経っても何も情報が得られなかった"),
            w.plot_setup("$sherlockが残した資料にあった人物が殺される"),
            w.plot_turnpoint("$wilsonが$sherlockが隠れて生き延びているらしい空き家の情報を手に入れる"),
            w.plot_develop("$maryたちはその空き家を調査する"),
            w.plot_develop("空き家のはずが夜には明かりが灯り、誰かが中に暮らしているのが分かる"),
            w.plot_turnpoint("$maryたちは眠らされ、気づくと縛られた状態で空き家の中にいた"),
            w.plot_resolve("知らない男が入ってきて$maryたちを助け出す"),
            w.plot_resolve("その知らない男の正体は$sherlockだった"),
            w.plot_resolve("何食わぬ顔で戻ってきた$wilsonが偽物だと見抜いていて、警察が踏み込んでくる"),
            w.plot_resolve("逮捕された$wilsonだったが、連行中に自爆して消えた"),
            )


