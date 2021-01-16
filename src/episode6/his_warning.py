# -*- coding: utf-8 -*-
'''
Episode 6-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$morianoの警告"


# NOTE: outlines
ABSTRACT = """
$morianoは$sherlockに対して自分は$steinの死とは無関係だと言う。証拠がないだろうと。
$sherlockは$morianoがどんな犯罪も自分で直接手をくださず、故に現在の司法では立件できず罪に問えないと言う。
だがそこを何とか見つけ出し、必ず罪を償わせると豪語する$sherlock。
その$sherlockに対し、$morianoは$maryに毒入りの飴を与えたことで脅し、これ以上は深入りしないようにと警告した。
その上で、$morianoは$sherlockが人の気持ちより謎解きの方を大切にすると指摘し、$maryたちも捨てられると予言する。$morianoは$sherlockに犯罪をなくすことは不可能だと言い、これ以上自分を追うと余計な犠牲者が出ると脅した。
その翌日、全員が出払っていた間に$sherlockの家は放火されてしまう。全焼こそ免れたが、中も荒らされていて、しばらく使えないという判断から、少しの間$wilson宅で暮らすことにした。
後日、$maryが市場に買い出しに出かけたまま帰ってこなかった。彼女は失踪した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryが連れてきた老人は$morianoで、$sherlockはすぐに逮捕すべきだと言う"),
            w.plot_turnpoint("$morianoは$maryに毒を飲ませたと言った"),
            w.plot_develop("$morianoによって$sherlockが今までやってきたことが全て無駄で単なる自己満足だったことが暴露される"),
            w.plot_turnpoint("$morianoは$maryに解毒剤を渡して立ち去った"),
            w.plot_resolve("$sherlockは$morianoによる脅しに屈しないと言うが、$maryの様子は変だった"),
            w.plot_turnpoint("後日、$maryが失踪した"),
            outline=ABSTRACT)

