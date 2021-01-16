# -*- coding: utf-8 -*-
'''
Episode 5-5
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "悲しみの結末"


# NOTE: outlines
ABSTRACT = """
伝説の魔犬が存在していたのだと騒ぐ$jamos。だが魔犬は襲いかかってくることはなく、$maryにじゃれつく。
それを外から見ていたのは城主の$cherryで、彼女は魔犬が$sherlockたちを食わないことに腹をたて、睡眠ガスを部屋に送り込もうとするが、$sherlockの機転により阻止される。
全ての事件が$cherryの手により行われたものだと言った$sherlockに対し、$cherryは皆殺しにしようと襲いかかってくるが、$maryと$limeにによって阻止される。
逃げ出した魔犬を追って$cherryも部屋から出た。
部屋に閉じ込められた$sherlockたちは何とか部屋から脱出し、$cherryを探す。
途中でやっと上陸できた警察と合流した。
$cherryは雑木林で魔犬に食われて亡くなっていて、魔犬は警察により射殺された。
$sherlockは$cherryが魔犬の餌にするために人殺しを行っていたのだと語る。
後日、地下の別の部屋から闇の技法を用いて愛犬を復活させたと考えられる儀式の形跡が見つかった。そしてその資金の為に所有していた$black_stoneが闇マーケットに売られていたことが判明した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("本当に魔獣の仕業だったと騒ぎ立てるが$sherlockは殺人が犬の仕業ではないことを伝えて、隠れていた$cherryを呼び出した"),
            w.plot_turnpoint("$cherryは自分が犬にやるために人を殺したと告白する"),
            w.plot_develop("$cherryは自分の罪を告白しながらも部屋に毒ガスをまこうとするが、犬が共倒れになりそうになって中止し、犬とともに逃亡する"),
            w.plot_turnpoint("$cherryが犬に食い殺されているのが発見された"),
            w.plot_resolve("事件は$cherryの死により結末を迎えた。後日城の地下で儀式の跡が見つかった"),
            outline=ABSTRACT)

