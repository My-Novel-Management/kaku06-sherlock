# -*- coding: utf-8 -*-
'''
Episode 5-0
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "魔獣の伝説"


# NOTE: outlines
ABSTRACT = """
$maryや$limeが同居して一月、賑やかな生活にも慣れてきた頃に、巷で連続猟奇殺人事件が発生していた。それらが人間ではないモノの仕業と有名になっていた。
$sherlockはこんな事例を紹介する。
ある孤島には魔獣の伝説があった。城の城主が住民を奴隷のように扱い、好きな娘を城に呼んでは自分の思い通りにして遊んだ。その城主は猟犬を飼っていて、気に入らない奴隷を追いかけさせては殺して楽しんでいたらしい。まだ$bossが生きていた頃の時代だ。
ある時、城に呼ばれた娘は自力で逃げ出した。その娘を猟犬に追わせ、自分も馬で探しに出た城主だったが、後に住民によって発見されたのは自分の猟犬により食い殺された城主と、血まみれになって笑っている少女だった。
事実は圧政に耐えかねた村人による城主の撲殺だったとされているが、未だに人々はその伝説が本物だと信じているという。
$sherlockはそういったオカルトを信じないと切って捨てた。
その城からパーティの招待状が届いた。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("ある孤島で猟奇的殺人事件が発生したが、それは魔獣によるものだという伝説があった"),
            w.plot_turnpoint("$sherlockはオカルトは信じないと$maryたちに言う"),
            w.plot_develop("$sherlockはオカルトや幽霊といったものに対して持論をぶち、不機嫌になって研究室にこもってしまう"),
            w.plot_turnpoint("そこに話題にしていた孤島の城の主からパーティの招待状が届く"),
            w.plot_resolve("招待状の内容は各方面の専門家を招いて魔獣伝説について議論してもらおうというイベントだった"),
            w.plot_turnpoint("$sherlockは用事があるから行けないと言った"),
            outline=ABSTRACT)

