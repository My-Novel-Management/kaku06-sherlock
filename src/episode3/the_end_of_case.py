# -*- coding: utf-8 -*-
'''
Episode 3-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "事件の顛末"


# NOTE: outlines
ABSTRACT = """
$sherlockは$maryに、赤鎧クラブが$limeを店から遠ざけておくための口実だったと語る。
その間に地下道を掘り、大金庫から何かを盗み出した。現金や金の延べ棒、宝石など多数が強奪されていたという。
$limeの証言が赤鎧クラブが存在しなかったことで嘘とみなされ、容疑を晴らせない。
$sherlockは$jakinsがどこから来たのかを辿っていく。やがて賭け事で借金を背負い、裏組織とつながりがあることが判明した。
ただそこから先が辿れず、$sherlockは情報屋に宝石の売買などを洗ってもらっていた。
その後、強盗団が火災現場で遺体となって発見されたことが$restradeから伝えられた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryに頼まれて$sherlockは$limeの容疑を晴らすために調査を開始する"),
            w.plot_turnpoint("$sherlockは赤鎧クラブの存在が$limeを店から遠ざけるためだったと語る"),
            w.plot_develop("質屋オーナー夫婦から聞き取りをして$jakinsがそもそも銀行の大金庫から宝石を盗み出す目的で近づいたこと等を突き止める"),
            w.plot_turnpoint("$jakinsが大量に借金をしていたことが判明する"),
            w.plot_resolve("$jakinsの昔の知人から組織とつながりがあり脅されていたことを知る"),
            w.plot_turnpoint("$jakinsの仲間と見られる強盗団が火災現場から遺体となって発見された"),
            outline=ABSTRACT)

