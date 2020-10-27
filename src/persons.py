# -*- coding: utf-8 -*-
'''
About: "人物"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# world settings
def main_notes(w: World):
    return (
            characters_note(w),
            )


def characters_note(w: World):
    return w.writer_note('人物設定',
            w.tag.title("主人公（勇者で探偵）"),
            "シャーロックという名前は使いたい",
            "知的でどこか病的でもあり勇者の血筋も引いていて$enagyの能力も秘めている",
            "ただそういったものを彼は「呪い」と捉えていてあまり人に知られたくはない",
            "第一巻では「勇者」であることを彼が認める、つまり自認の物語である",
            w.tag.title("ワトソン役（かつモリアーティ）"),
            "叙述トリックの肝心",
            "かつて王国の大神官にまでなった男を騙る、闇の住人",
            "かなり頭が切れ、主人公を途中まで見事に騙す",
            "しかし勇者である確証を得てからの行動でミスり、彼に誘導されて事故死に見せかけて処分したように勘違いさせられた",
            "名前はできればワトソンから何かもじったものがいい",
            "同じ名前の本人が二巻目以降、記述者の役割を担うことになる",
            w.tag.title("元パンナ"),
            "ヒロイン枠",
            "口うるさいタイプで感情豊か",
            "体型は子どもっぽいのがいいかな",
            "感が鋭いところが知的長所",
            w.tag.title("鎧役（女騎士）"),
            "第二のヒロイン枠",
            "呪いの鎧のせいでしゃべれない（後に呪いを解除されるがそれでも無口）",
            "実は王国の第二王女",
            "誘拐されたが呪いの鎧により逃亡に成功するも、そのせいで放浪の旅に",
            "何とか拾われて食い扶持を与えてもらっていた",
            w.tag.title("モリアーティ枠"),
            "ダミーとしてだが、とにかくモリアーティが必要になる",
            "最後の事件で$wilsonの手先として活躍する必要があるが、それなりに実力者じゃないと困る",
            "裏で糸を引いているのは$wilsonだが、その影武者としての存在",
            )


def chara_sherlock(w: World):
    return w.chara_note("$sherlock履歴書",
            "$heroの血筋に生まれる",
            "兄とは別の母親で、元王族の男の下に生まれたが、すぐに母親と二人で放り出される",
            "ずっと父は死んだと聞かされて育つ",
            "小さい頃から気になったことは最後まで解明しなければ気がすまず、それに根気よく付き合ってくれた母親により、自分で謎を解く快感を知った",
            "母親は知恵は人を助けると教えた",
            "十歳の時に母親が病気で亡くなり、兄が迎えにきた",
            "その時に「$heroの血を引く正当な人間」と教わるが、自分に父親はいないとその申し出を断った",
            "ただそれ以来、養育費としていくらかの支払いを毎月送ってくる",
            "全寮制の学校に入り、そこで十代を過ごす",
            "",
            # TODO
            )

def chara_mary(w: World):
    return w.chara_note("$mary履歴書",
            )

def chara_lime(w: World):
    return w.chara_note("$lime履歴書",
            )

def chara_wilson(w: World):
    return w.chara_note("（偽）$wilson履歴書",
            )

def chara_wilson2(w: World):
    return w.chara_note("（真）$wilson履歴書",
            )

def chara_moriano(w: World):
    return w.chara_note("$moriano履歴書",
            )

def chara_aily(w: World):
    return w.chara_note("$aily履歴書",
            )

def chara_rudy(w: World):
    return w.chara_note("$rudy履歴書",
            )

