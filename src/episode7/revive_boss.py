# -*- coding: utf-8 -*-
'''
Episode 7-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$bossの復活"


# NOTE: outlines
ABSTRACT = """
$sherlockは$maryが$patsonにより連れ出されたと知り、急いで改装中の大聖堂へと向かう。そこが$boss復活の儀式を行う場所だと言う。
大聖堂の地下には巨大なホールが広がっていた。そこはかつて$bossの居城があった場所で、封印する目的で聖堂を建てたのが今の大聖堂の元になったと説明する。
待ち構えていた$patsonは$maryを人質にして、残り一つの「捧げもの」を$sherlockに要求する。それは$heroの血液だった。
$sherlockの家を荒らしたのは$patsonだった。$sherlockが$heroだと知った彼が血液の研究をしていたのを知っての犯行だ。しかし既に$sherlockが処分した後だった。
$patsonも一部に$ajinの血が入っており、苦しい幼少期を経て今があった。$boss復活すれば$ajin優遇の世界がくると信じていた。
だが$sherlockにより過去、$bossがいた時代の$ajinの扱いがどんなに酷いものだったかが語られる。
$gunを打って$sherlockを負傷させ、$maryを人質に、その血を盃に入れさせた。
$patsonにより、$boss復活の儀式が始まった。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$patsonが裏切り者だった。$boss復活の儀式を行うために$maryを誘拐し、改装中の大聖堂に向かう"),
            w.plot_turnpoint("改装中の大聖堂に、地下に繋がる階段が見つかった"),
            w.plot_develop("$patsonは儀式を行うために$maryを盾にして脅す。必要な祭具の残り一つが分からなかったが$sherlockによりそれが$heroの血であることを教えられる"),
            w.plot_turnpoint("$sherlockは真の$heroだった"),
            w.plot_resolve("道具が揃った$patosonは$boss復活の儀式を開始した"),
            w.plot_turnpoint("だが儀式は途中で失敗する"),
            outline=ABSTRACT)

