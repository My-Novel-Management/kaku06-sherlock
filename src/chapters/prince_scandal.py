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


## chapter
def main(w: World):
    return w.chapter(TITLES[1],
            "街が舞台",
            w.plot_setup("世間では怪盗$jackという謎の存在が人気を集めていた"),
            w.plot_setup("王室からの使者として$wilsonがある短刀を取り返して欲しいと依頼する"),
            w.plot_setup("実は皇太子が結婚を控えているが、過去の女に預けた宝剣を取り戻したいというのだ"),
            w.plot_setup("だが$sherlockは王室からの依頼は全て断っていた"),
            w.plot_turnpoint("翌日、その$ailyが$sherlockに依頼に訪れた"),
            w.plot_develop("$ailyの恋人が行方不明になったという"),
            w.plot_develop("その上、その男が宝剣を持ち去ったと"),
            w.plot_develop("$sherlockは調査を開始する"),
            w.plot_develop("けれど調べるほどにその男の存在は希薄だった"),
            w.plot_turnpoint("調査結果を伝えに行くと$ailyの家はもぬけの殻になっていた"),
            w.plot_resolve("自分の家に荷物を届けにきた配達人こそが$ailyと分かったが、既に彼女は高跳びした後だった"),
            w.plot_resolve("送られた小包は宝剣だった"),
            w.plot_resolve("だがそこにはまっていた宝珠は消えていた"),
            w.plot_resolve("しかし宝剣に新しい宝珠がつけられ、皇太子の結婚式は無事に行われた"),
            "$wilsonが手にメモを持ちながら、近所の少年に聞いて、$sherlock宅を訪れる",
            "ベルを鳴らすが、反応がない",
            "何度か鳴らしてようやく除き窓が開くが、何も言われない",
            "多少気分を害しつつ、用件を言おうとするが「帰れ」と言われる",
            # TODO
            )


