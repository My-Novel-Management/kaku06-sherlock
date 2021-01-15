# -*- coding: utf-8 -*-
'''
Episode 1-1: "王子の問題"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Scenes
# NOTE

# NOTE: outlines
ABSTRACT = """
書簡には王子が結婚をすることになったが、その儀式に必要な宝具の一つ$royalswordをある女性にあげてしまったので、何をしてもいいから取り戻して欲しいというお願いが書かれていた。
この国の王子というのは$heroたちの血筋を色濃く引いている四家系の一つ$Arthur家の長男で、次期国王だったが、どうしようもない駄目男で有名だった。
あちこちで子種をばらばいては問題を起こしているらしいとも。
その王子の尻拭いは$sherlockが受けたくない依頼の中でもワースト１だった。
しかしある恩義があり、断れないので、$sherlockは仕方なくその女性について調査を行う。
$sherlockはいつも入念に調査する。資料もそうだが、何より現地調査を重要視していた。
$wilsonの$carでその女の暮らす高級住宅街に向かう。
現地に到着すると、周囲で$ailyについて聞き込みを行う。近所の評判はよく、ちゃんと言えば返してくれそうな雰囲気はある。
家を訪れると、誰も出ない。だが鍵が開いていた。
"""


# Episode
def main(w: World):
    return w.episode("王子の問題",
            # NOTE
            w.plot_setup("王子からの書簡にはある女から$royalswordを取り戻して欲しいと書かれていた"),
            w.plot_turnpoint("王室からの依頼は受けないはずの$sherlockが、王子からの依頼は受けると言った"),
            w.plot_develop("王子に何かしら弱みを握られているらしい$sherlockは仕方なく仕事を受け、$ailyという女を調査に向かう"),
            w.plot_turnpoint("$ailyの近所の評判は王子の書いていたものと異なっていて、良いものだった"),
            w.plot_resolve("$sherlockと$wilsonは$ailyの自宅を訪ねるが、応答はない"),
            w.plot_turnpoint("しかし玄関の鍵は開いていた"),
            outline=ABSTRACT)

