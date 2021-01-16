# -*- coding: utf-8 -*-
'''
Episode 8-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "全ての顛末"


# NOTE: outlines
ABSTRACT = """
偽$wilsonである$zeronの自殺により$boss復活の儀式にかかわる一連の事件に一応の決着がついた。
だが$sherlockと$mary、$limeは住む場所を失い、仕方なく$wilsonの家でしばらく暮らすことになる。しかし大家が家賃滞納を理由に家から出ていけと言ってきた。
そこに本物の$wilsonが帰ってきて、$sherlockたちは彼に一連の事件と自分たちがここにいる事情を語った。
$wilsonは$sherlockの活躍を小説として新聞に掲載することで家賃分を何とかしようと提案する。
これを承諾し、ここに$sherlock探偵社が誕生した。
"""


def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("偽$wilsonである$zeronの死により一連の事件に決着がついた"),
            w.plot_turnpoint("$sherlockは$wilsonが偽物だと気づいていた、と告白する"),
            w.plot_develop("$sherlockは最初の時点でおかしいと思い、更に$wilsonの家に行って気づいたと語る。全ての事件に巧妙に$zeronが関わり、更に$boss復活の儀式の祭具を揃える動きを行っていたと語る"),
            w.plot_turnpoint("本物の$wilsonが帰ってくる"),
            w.plot_resolve("$sherlockたちは$wilsonに全ての事情を説明する"),
            w.plot_turnpoint("$wilsonは$sherlockの活躍を小説にして稼ぐことを提案した"),
            outline=ABSTRACT)

