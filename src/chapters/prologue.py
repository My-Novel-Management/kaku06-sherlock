# -*- coding: utf-8 -*-
'''
Chapter "プロローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episodes
def troublesome(w: World):
    return w.episode("厄介事",
            w.plot_note("私（$wilson）は出かける準備をしていた"),
            w.plot_note("テーブルの上には新聞記事がちらばっている"),
            w.plot_note("謎の失踪事件が多発していた"),
            w.plot_note("食べかけの朝食を片付け、部屋から出る"),
            w.plot_note("いつも厄介事を頼まれる、そういう運命の下に生まれたんだと語る"),
            )


def handyman_sherlock(w: World):
    return w.episode("便利屋$sherlock",
            w.plot_note("$wilsonは外にとめてあった$carに向かう"),
            w.plot_note("そこで大家と出会う"),
            w.plot_note("大家からは家賃を支払ってもらわないと困ると言われるが、今受けた仕事の金が入ったらと"),
            w.plot_note("同じような男がいて困っている。結婚しない男の一人暮らしはどうも信用ならないと"),
            w.plot_note("それが$sherlockという、自称便利屋だが、何をやっているのかさっぱりだと"),
            w.plot_note("$wilsonは$carに乗り込み、出かける"),
            )


def note_for_novel(w: World):
    return w.episode("作品のための注意書き",
            w.plot_note("本作品は全て三人称で記述される"),
            w.plot_note("記述者＝私により後から整理され、書かれたもの"),
            w.plot_note("聞いた時が前後しても、読んでいくのにいいように並べ替えてある"),
            w.plot_note("本作は$sherlockという男を中心に巻き起こった事件について書いた、伝記的作品である"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[0],
            w.plot_setup("$wilsonは王室からいろいろな厄介事を頼まれる存在"),
            w.plot_turnpoint("最近続いている謎の失踪事件の調査を頼まれる"),
            w.plot_develop("新聞を見ながら趣味でやっている日記を書き始める"),
            w.plot_turnpoint("$sherlockという男が街の便利屋という噂を知ったところから物語は始まる"),
            w.plot_resolve("$sherlockの家を訪問する$wilson"),
            #
            troublesome(w),
            handyman_sherlock(w),
            note_for_novel(w),
            )


