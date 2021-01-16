# -*- coding: utf-8 -*-
'''
Episode 5-1
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "第一の殺人"


# NOTE: outlines
ABSTRACT = """
船で島に渡る$sherlockたち。ガイド役として観光課職員の$mochが同行した。今回のイベントが観光目的だからだそうだ。
島では伝説の殺人があった雑木林に記念碑を建てていたが、その後も猟奇的な殺人事件が何度か起こり、かつて暮らしていた島民は全員外に逃げ出していた。
城では現在の城主$cherryが迎えてくれる。
既にパーティ参加者は集まっていて、それぞれ元刑事$hugar、社会学者$reui、心霊学者$karl、地元の歴史学者$jamos、新聞記者の$milkと癖のある人間が揃っていた。
他にパーティ用に臨時で雇った料理人$doldと使用人$bettyがいた。
イベントは明日行われるからと、前日はささやかな立食パーティが開かれた。
各自部屋があてがわれたが$sherlockたちは人数が多かったため、二人でひと部屋となった。
$maryと$limeはパーティ会場で食べながらそれぞれの参加者の話を苦笑しつつ聞いた。
一方$sherlockは城を興味深く歩いて見て回っていた。
しかし翌早朝、社会学者の$reuiが無残な姿で殺されているのが発見された。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockの代役として$maryと$lime、$wilsonが行くことになり、島に向かう"),
            w.plot_turnpoint("案内の観光課職員$mochは$wilsonを$sherlockだと勘違いする"),
            w.plot_develop("城に到着するとそこでは元刑事$hugarや社会学者$reui、心霊学者$karlなどの癖の強い面々が待ち構えていて、やってきた$wilsonたちに持論を語る"),
            w.plot_turnpoint("$maryが犬の鳴き声を聞いた、と言った"),
            w.plot_resolve("翌日のパーティの余興として地元の歴史学者$jamosより魔獣伝説の講義があった"),
            w.plot_turnpoint("しかし翌朝、社会学者$reuiが遺体で発見された"),
            outline=ABSTRACT)

