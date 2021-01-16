# -*- coding: utf-8 -*-
'''
Episode 3-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "閉じた赤鎧クラブ"


# NOTE: outlines
ABSTRACT = """
$sherlockはまず赤鎧クラブの場所を調べる。$limeが見たという張り紙すら消え、完全に何もなかったことになっていた。
不動産屋にその件を調べてもらうよう、大家の$lisaに頼む。
次は質屋を調べる。旧市街地にあり、すぐに大通りに繋がる場所。近所には改装中の王立銀行もあった。
質屋の店舗は小さいもので、前の店舗部分と奥の控室、更に倉庫となっている。$limeとオーナー夫婦は近所の別の家で暮らしているという。
$sherlockは普段の$limeと$jakinsの仕事内容を聞き、$jakinsに何か起こって失踪した可能性を考える。だが高額なものは置かれておらず、盗まれた形跡もない。
調べてみると、奥の部屋から地下入り口があり、そこからどこかに抜け穴が掘られていた。また近隣の聞き込みから日中頻繁に複数の男が出入りしては大きな袋を運び出していたとも。
その通路を進んでいくと、途中で失踪していた$jakinsの遺体を発見する。更にそれが改装中の銀行の大金庫へと繋がっていたことが分かった。
警察により殺人事件の容疑者として$limeが浮上した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$limeから赤鎧クラブが閉会したことと同僚$jakinsが失踪したことを聞く$sherlock"),
            w.plot_turnpoint("$sherlockは赤鎧クラブの調査に向かう"),
            w.plot_develop("$limeの言う通り赤鎧クラブは存在そのものが消え去っていた。続いて質屋を調べると奥に地下道を発見する"),
            w.plot_turnpoint("地下道の途中で$jakinsが殺されていた"),
            w.plot_resolve("地下道は改装中の国営銀行の大金庫まで繋がっていて、中から大量の宝石が盗まれていた"),
            w.plot_turnpoint("$jakins殺害容疑で$limeが逮捕された"),
            outline=ABSTRACT)

