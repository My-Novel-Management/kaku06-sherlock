# -*- coding: utf-8 -*-
'''
Episode 7-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$sherlockを探して"


# NOTE: outlines
ABSTRACT = """
シャーロックが消えてから半年、メアリーは市場の手伝いをし、ライムは護衛のアルバイトしながら、彼を探し続けていた。しかし未だに何も情報がなくパットソンたちは諦めた方がいいと言っていた。
だがある日、シャーロックの家が強盗に荒らされていて、まだシャーロックを探している人物がいることが分かる。
メアリーたちは安全のために一旦ウィルソンの家に移り、地道にシャーロックに関する情報を収集した。
そして遂にウィルソンがシャーロックを見たというホームレスの情報を持ってくる。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$sherlockが滝壺に落ちてから三ヶ月が経つが何も生存情報が見つからず、$maryたちは新しい生活に馴染み始めていた"),
            w.plot_turnpoint("$wilsonが$sherlockに似た男を目撃したという情報を持ってくる"),
            w.plot_develop("ホームレスから情報を得て、$maryたちは$sherlockに似た男が現れるという空き家を監視する"),
            w.plot_turnpoint("夜になり$sherlockに似た男が空き家に入っていく"),
            w.plot_resolve("シルエットは$sherlockを思わせたが、その空き家に別の男性が入っていくのを目撃する"),
            w.plot_turnpoint("争う音がして、明かりが消えた"),
            outline=ABSTRACT)

