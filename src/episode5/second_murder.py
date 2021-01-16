# -*- coding: utf-8 -*-
'''
Episode 5-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "第二の殺人"


# NOTE: outlines
ABSTRACT = """
$hugarは$mochを怪しみ、探そうとする。だが$sherlockはまず全員の安全を確保すべきと意見が割れ、$hugarから反感を持たれる。
$hugarに従おうとする$jamosや$doldたちと、反発する$sherlock。心霊学者の$karlは全てが魔獣の仕業だと騒いでいた。
$hugarは城の外を捜索すると出ていく。中に残った$sherlockは$cherryに城内調査の許可を貰おうとしたが、彼女は体調を崩したようで、すぐに自室に引っ込んでしまった。
城内を調べていると、かなり古い道具がいくつも見つかった。また改修されているのも分かった。
$hugarたちが戻ってきて$mochの死体を雑木林で発見したと言う。更に$karlの姿が消えていた。
手分けして探すが見つからない。
心配していた$cherryの寝室に入ったが、彼女の姿も消えていた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("元刑事の$hugarは$mochを容疑者とみて捜索させる"),
            w.plot_turnpoint("心霊学者$karlも姿を消す"),
            w.plot_develop("多くの失踪者が出て$hugarは混乱し、現場は統制が取れなくなっていた。$maryは新聞記者$milkとともに改めて情報を整理する"),
            w.plot_turnpoint("失踪した$mochが雑木林で遺体で発見される"),
            w.plot_resolve("連続殺人事件となり、容疑が一旦晴れた$jamosが出され、みんなで固まっている方が安全だという提案がなされるが、$hugarは汚名挽回とばかりに一人で出ていってしまう"),
            w.plot_turnpoint("$sherlockから島に向かっていると連絡が入った"),
            outline=ABSTRACT)

