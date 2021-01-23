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
            w.plot_note("今日も$sherlockは外出していた"),
            w.plot_note("$maryは失敗したものの、焼いた焼き菓子を前にして$limeと$wilsonとお茶をしていた"),
            w.plot_note("そこで普段は見ない新聞を見て、こんな記事を見つける"),
            w.plot_note("ある孤島で殺人事件が発生した。猟奇的な惨状だったそうだ"),
            w.plot_note("最近街でも連続猟奇殺人が発生していて、その名前が$jackと名付けられている"),
            w.plot_note("その孤島はかつて百名ほどの島民がいたが、ある伝説があって、今はほとんど人がいないらしい"),
            w.plot_note("亡くなっていたのは地元の船乗り"),
            w.plot_note("発見したのは島にある城の主人の女性だった"),
            w.plot_note("その孤島の伝説というのが、魔獣伝説"),
            w.plot_note("昔、ひどい領主がいて、その領主が猟犬を飼っていたが、集落の娘を好き放題していた"),
            w.plot_note("その娘の一人が城から逃げ出し、猟犬をけしかけたが、犬は娘になついていて、薬で錯乱状態だった犬は娘を殺してしまう"),
            w.plot_note("それに怒り狂った猟犬が今度は領主まで殺してしまい、その後魔獣として島に残っているという都市伝説だった"),
            w.plot_note("三人はこういったオカルトについてそれぞれの態度だった"),
            w.plot_note("$maryは怖がり、$limeは興味津々で、$wilsonは現実的だった"),
            w.plot_note("そこに$sherlockが戻ってくる"),
            w.plot_note("$sherlockに話すとすぐに「オカルトは信じない」とばっさり"),# TODO
            outline=ABSTRACT)

