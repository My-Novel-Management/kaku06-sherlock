# -*- coding: utf-8 -*-
'''
Episode 4-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "事件解決"


# NOTE: outlines
ABSTRACT = """
$jackは$maryを外へと逃してくれようとする。しかし男たちに気づかれ、逆に閉じ込められてしまう。それでも$jackは$sherlockがくると言う。
$maryは$jackも$ajinだと知り、自分の悩みを相談する。$sherlockはどんな人種であろうがそこに妙な感情は抱かないと言う。時折本当に感情があるんだろうかと疑うくらいで、その点で彼は信頼していいと。$maryはほっとする。
一方$sherlockは$limeからの情報を得て、警察に手配する。
その間に再度被害者宅とガチョウの卸業者を調査する。そこで事件の犯人がガチョウクラブの人間ではなく、それに見せかけた彼女の愛人の仕業だと見破る。
ナイフの指紋が検出できないように細工していたのは、その技術が存在することを知っていたかららしい。男の出自が謎だったが、どうも別の国からやってきた人物らしかった。
ただの痴情のもつれが原因と知り、偽装しただけで、凶器の隠し場所に悩んだ末のガチョウに食べさせるというやり口だった。
そして$ignesから警察により$maryが保護されたという連絡が入った。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryは謎の女性（$jack）によって助け出される"),
            w.plot_turnpoint("しかし逃げ出したのがバレて追われる身となった"),
            w.plot_develop("$sherlockの指示でガチョウクラブに警察の捜査が入る。しかしそこに$maryの姿はなかった"),
            w.plot_turnpoint("男たちの誰もナイフから指紋検出されなかった"),
            w.plot_resolve("全て空振りだった$shelrockの前に$maryと謎の女（$jack）が現れる"),
            w.plot_turnpoint("$sherlockにより事件の犯人が逮捕された（$moura夫人の愛人だった）"),
            outline=ABSTRACT)

