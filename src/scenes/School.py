# -*- coding: utf-8 -*-
'''
Stage: "王立学園"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   この国一番の学校
#   教育機関の最高峰で、大学は別途ある


## scenes
def sherlocks_school(w: World):
    return w.scene("思い出の学校",
            w.plot_note("$sherlockがきたのは自分がかつて通っていた学園だった"),
            w.plot_note("そこの臨時教師になっていた$jackと出会う"),
            )


def ailys_confession(w: World):
    return w.scene("$ailyの告白",
            w.plot_note("$jackは自分の将来の夢が教師だったと告白する"),
            w.plot_note("生まれたときから孤独で、孤児院で大勢の小さい子のために物心ついたころから盗みを働いていた"),
            w.plot_note("あの$stoneを集めようとしたのは、その孤児院を救うためだったと言う"),
            w.plot_note("そのクライアントが、なくなっていたもと研究員だった"),
            w.plot_note("一体なにの研究をしていたのかは分からないが、どこで稼いだのか、かなり金を持っていた"),
            w.plot_note("実際に家にいったのは一度だけで、その時には既に彼が殺された状態だった"),
            w.plot_note("仕組んだのは$stoneを手に入れたい別の人間"),
            w.plot_note("$sherlockはそれを理解した上で、あの$stoneを渡してはいけないと言う"),
            w.plot_note("$jackは$sherlockに条件を出す"),
            w.plot_note("それを飲んでくれたら$stoneを渡すと"),
            )


def terms_of_exchange(w: World):
    return w.scene("交換条件",
            w.plot_note("$sherlockは泥棒の頼みは聞けないというが、一度助けてもらった恩があるといい、その条件を聞く"),
            w.plot_note("$jackはしばらく遠方に身を隠しながら、孤児院の支援を続けるから、ここが潰れないようにはからってほしいと"),
            w.plot_note("$jackは自分が狙われた原因が$stoneにあると、持っていたそれを見せる"),
            w.plot_note("それは三つ目の$stoneだった"),
            w.plot_note("$jackは$sherlockに$stoneを渡す"),
            w.plot_note("誰かがこれを四つ集めて何かしようと企んでいると告げる"),
            w.plot_note("$sherlockになんとしてもそれを阻止してほしいと頼み、彼女は姿を消す"),
            w.plot_note("$sherlockはその$stoneを見ながら考え込んだ"),
            )
