# -*- coding: utf-8 -*-
'''
Episode 1-5: "王子の結婚"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "王子の結婚"


# NOTE: outlines
ABSTRACT = """
$ailyは$sherlockが見抜いたことに驚く。
$sherlockは警察を連れてきていると脅し、$royalswordを取り戻そうとする。
しかも$ailyが$jackだと見抜いていた。
$jackの表の顔がオペラ歌手$ailyだった。
亡くなっていたのは最初にスカウトされた$ailyで、ただ彼女は歌以外は駄目だった。
そこで提案し、$jackが$ailyに成り代わったのだ。
亡くなっていたのは本物の$ailyで、自殺だった。彼女を他殺に見せかけ、オペラ歌手$ailyの最後が自殺という風にならないように仕組んだ。ついでに$royalswordを返さなくて済むようにした。
だが全てバレて、$jackはおとなしく$sherlockに返却すると約束する。
後日、孤児院で子供から$royalswordを返してもらった。
だがそこには$red_stoneがついておらず、考えた$sherlockは宝石技師に頼みレプリカを作ってもらった。
こうしてなんとか無事に王子の結婚式が迎えられた
"""


# Scenes


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$ailyこと怪盗$jackは$sherlockに全て見抜かれていたことで本性を現す"),
            w.plot_turnpoint("$jackは最初から$royalswordが目的で王子に近づいたと告白する"),
            w.plot_develop("$sherlockは$jackが本物の$ailyの自殺を偽装するために、強盗を装ったこと等を推理で当てた。彼女はすんなりと$sherlockに$royalswordの返却を約束する"),
            w.plot_turnpoint("しかし後日届けられた$royalswordには肝心の$red_stoneが付いていなかった"),
            w.plot_resolve("$stoneのレプリカを作ってもらい、何とか無事に王子の結婚式は行われた"),
            w.plot_note("$sherlockは$yilaに対して「$ailyですよね？」と言った"),
            w.plot_note("$yilaは分からないふりをする"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

