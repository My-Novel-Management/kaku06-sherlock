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
            w.plot_note("$sherlockに話すとすぐに「オカルトは信じない」とばっさり"),
            w.plot_note("それからオカルトが実際にどういうものか、その現実を語る"),
            w.plot_note("現実は、都市伝説というのはそれの元になる事件があり、この場合なら実際に殺された人が見つかった"),
            w.plot_note("そこに奇妙な状況ができあがっていて、たとえば野犬によって死体が荒らされていた等"),
            w.plot_note("更に領主に対する住民の不満が溜まっていて、歪んだ恨みつらみがあったと"),
            w.plot_note("それらの条件が揃った時に「魔獣によって殺された」という都市伝説が誕生するんだ、と"),
            w.plot_note("$maryはつまらないと言うが"),
            #
            w.plot_note("後日、$maryは今度こそと自分が作った菓子を食べてもらおうとする"),
            w.plot_note("そこに手紙が届く"),
            w.plot_note("それは先日噂にしていた記事の孤島の、城の城主からだった"),
            w.plot_note("イベントがあり、パーティを開催するので、そこに$sherlockに参加してほしいというもの"),
            w.plot_note("イベントは魔獣伝説についてとだけある"),
            w.plot_note("$sherlockはくだらないと言い、参加しないと言うが"),
            w.plot_note("そこにやってきた$wilsonは面白そうだから行けばいいのに、と"),
            w.plot_note("$sherlockはその日程は別の用事があるからと断る"),
            w.plot_note("$maryが$wilsonが$sherlockということにして参加すればいいと"),
            w.plot_note("$sherlockは勝手にしろと言い、$maryと$lime、$wilsonの三人で行くことになった"),
            #
            w.plot_note("駅から$trainで移動し、更に港から船に乗る"),
            w.plot_note("島の前の港では地元の観光課の職員である$mochが待っていた"),
            w.plot_note("$sherlock様、という旗に対してやってきた$wilsonたち"),
            w.plot_note("$maryを助手、$limeをボディガードと説明した"),
            w.plot_note("$mochとともに渡し船で島へと渡る"),
            w.plot_note("島との行き来は船しかないらしい"),
            w.plot_note("$maryは初めての旅行を楽しみにしていた"),
            #
            w.plot_note("島に到着する"),
            w.plot_note("$mochは途中の雑木林に立ち寄る"),
            w.plot_note("そこが伝説の殺人のあった場所だと紹介する"),
            w.plot_note("観光産業で賑わいを取り戻そうとしているらしい"),
            w.plot_note("長い坂道を登り、砦として使われていた城に到着する"),
            w.plot_note("その重々しい跳ね橋が降りて、橋になった"),
            w.plot_note("城主の$cherryが「ようこそいらっしゃいました」と笑顔で迎えた"),
            w.plot_note("$maryには犬のような獣の遠吠えが聞こえた気がした"),
            outline=ABSTRACT)

