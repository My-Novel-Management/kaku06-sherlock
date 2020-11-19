# -*- coding: utf-8 -*-
'''
Chapter "赤鎧クラブ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episodes
def missing_persons(w: World):
    return w.episode("失踪者たち",
            "$maryは困っていたという謎の鎧騎士を連れてくる",
            w.plot_note("同居するようになった$maryはやたらと$sherlockにまとわりつく"),
            w.plot_note("$sherlockは大好きな読書もできず、困っていた"),
            w.plot_note("$maryは彼の迷惑になりたくなくて、$wilsonに相談する"),
            w.plot_note("女手が不足しているから自分が役立つところをアピールしてみたら、と助言を受ける"),
            w.plot_note("$maryは掃除や買い物を買って出る"),
            w.plot_note("やっと外に出てくれてほっとした$sherlockは$wilsonに事件について相談する"),
            w.plot_note("最近謎の失踪者が増えていた"),
            w.plot_note("失踪事件として新聞や雑誌も特集を組んでいる"),
            w.plot_note(""),
            # TODO
            )


def strange_work(w: World):
    return w.episode("不思議な仕事",
            "$sherlockは$limeにその仕事をすぐ辞めるように進言したが、理由は話さなかった",
            )


def bank_robbery(w: World):
    return w.episode("銀行強盗",
            "$limeが仕事を首になったらしいと$maryから伝え聞いた",
            )


def truth_of_club(w: World):
    return w.episode("クラブの真相",
            "$limeが助けてほしいとやってくる",
            )


def what_was_stolen(w: World):
    return w.episode("盗まれたもの",
            "$limeは自分が王室の人間であることを告白した",
            )


def new_living(w: World):
    return w.episode("新しい居候",
            w.plot_note("$limeは自分が誘拐された訳ではなく、普通に家出をしたのだと告白する"),
            w.plot_note("王室はそんな品の悪い発表をできないから失踪事件にして公表したのだと言った"),
            w.plot_note("もともと妾の子で、周囲から浮いていて、王室にも自分の居場所がなく帰りたくないと泣く"),
            w.plot_note("$maryは$sherlockに$limeを一緒に住まわせてほしいとお願いする"),
            w.plot_note("$sherlockは金銭的な問題さえ解決できればと提案する"),
            w.plot_note("$wilsonは金のことなら大丈夫だと、なぜか大金を手にして言う"),
            w.plot_note("$wilsonは$sherlockの秘蔵コレクションを売り払っていた"),
            w.plot_note("こうして新しい住人$limeをここに加えることになった"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[3],
            w.plot_setup("失踪者のリストの中に第二王女も含まれている"),
            w.plot_turnpoint("$maryは困っている赤鎧の騎士を連れてくる"),
            w.plot_develop("$limeは赤鎧の人間にだけできる不思議なアルバイトをしていると告白する"),
            w.plot_turnpoint("$sherlockはすぐやめるよう忠告するが$limeは断れず続けてしまう"),
            w.plot_develop("大規模な強盗事件が発生し、$limeの店の主人が逮捕される"),
            w.plot_turnpoint("$limeは仕事をクビになる"),
            w.plot_develop("事情を聞いて、赤鎧クラブの仕組みを$sherlockが解説する"),
            w.plot_turnpoint("$sherlockはそのいなくなった同僚が犯人と指摘する"),
            w.plot_develop("犯人たちは既に逃げたあとで同僚の兵士は殺されて見つかった"),
            w.plot_turnpoint("$limeは事情があって王室に戻れないと告白した"),
            w.plot_resolve("$limeが$sherlockの家に居候することになった"),
            missing_persons(w),
            strange_work(w),
            bank_robbery(w),
            truth_of_club(w),
            what_was_stolen(w),
            new_living(w),
            )


