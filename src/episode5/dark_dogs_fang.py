# -*- coding: utf-8 -*-
'''
Episode 5-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "魔獣の牙"

# NOTE: outlines
ABSTRACT = """
$sherlockは$jamosに通信機が使えるようにならないか試してもらう。
$hugarは消えた$carlをずっと怪しんでいて単独で捜査してどこかに行ってしまう。
$maryはずっと姿を見ていない$cherryが気になっていたが、部屋には鍵がかかったままだった。
$sherlockは再度、城内を調査する。人の手によるものだとし、最初の談話室の事件が可能だった人物を挙げていく。
そこに$hugarがお手伝いの$bettyも殺されているのを見つけたとやってくる。$hugarと$sherlockは互いを疑い合う。
その時、$limeが談話室で抜け道を見つけた。
地下通路を進むと、その先には拷問器具が置かれた部屋があり、$karlの死体が転がっていた。
更にそこには大きな黒い犬が待ち構えていた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryたちは$sherlockの指示で調べておいてほしいと言われたところを調査する"),
            w.plot_turnpoint("$cherryの寝室に入るが、彼女の姿も消えていた"),
            w.plot_develop("$limeが抜け道に気づいて寝室から談話室に抜けられることを発見する。それが$hugarに見つかり、$limeたちが犯人にされてしまう"),
            w.plot_turnpoint("$sherlockがやってきて$maryたちと合流する"),
            w.plot_resolve("$sherlockは$maryたちから情報を聞き、談話室を調べ始める。そこで地下への階段を見つけた"),
            w.plot_turnpoint("地下に拷問部屋があり、そこで黒い巨大な犬が待ち構えていた"),
            outline=ABSTRACT)

