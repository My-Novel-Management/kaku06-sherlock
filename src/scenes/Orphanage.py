# -*- coding: utf-8 -*-
'''
Stage: "孤児院"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   アイリーが育った孤児院。運営の大本は協会
#   [裏庭]
#   [寝室][寝室]
#   [応接間]
#   [ホール]


## scenes
def a_orphanage(w: World):
    return w.scene("ある孤児院",
            w.plot_note("孤児院に到着し、そこに入る"),
            w.plot_note("なぜここにきたのか尋ねると、$ailyという女性が寄付をしていた場所だったと"),
            w.plot_note("寄付をするとそこの孤児たちが作った栞がもらえるが、それが落ちていたのだ"),
            w.plot_note("尋ねたが、$ailyという女性に心当たりはないらしい"),
            )


def teachers_talk(w: World):
    return w.scene("教師の話",
            "同・部屋",
            w.plot_note("応対してくれた教師（実は$aily）は、ここは養子としてもらわれていく子もいるが、大半は自立して働いて暮らしていると"),
            w.plot_note("その場所に支援してくれているその女性も素晴らしい人だろうと、彼女は言った"),
            w.plot_note("$sherlockはそこで子供たちが自分のことをいつもくる女性の知人と思って話しかける"),
            )


def secret_treasure(w: World):
    return w.scene("子供たちの宝物",
            w.plot_note("子供が彼女からあるものを預かっていることを知った"),
            w.plot_note("それは宝剣だった"),
            "孤児院・前",
            w.plot_note("$sherlockは宝剣をレプリカとすり替え、持ち帰る"),
            )


def investigation_her(w: World):
    return w.scene("女教師の調査",
            w.plot_note("数日後、$sherlockは再び孤児院を訪れていた"),
            w.plot_note("事件は暗礁に乗り上げ、$ailyを重要参考人として警察が探しているらしい、という情報だけが$sherlockに届いた"),
            w.plot_note("$sherlockは孤児院の女教師に話しかける"),
            w.plot_note("$ailyさんですね、と"),
            w.plot_note("彼女は観念し、孤児院の裏庭に出て話す"),
            )


def aily_confession(w: World):
    return w.scene("$ailyの告白",
            w.plot_note("宝剣についてはすぐに返すつもりだったが、それが価値あるものと知り、お金に変えた"),
            w.plot_note("この孤児院を存続させたいがための行動だった"),
            w.plot_note("$sherlockはあの宝剣が本物だったことを告げると、彼女は子供たちを呼びつける"),
            w.plot_note("その子どもたちに囲まれている間に彼女は姿を消してしまった"),
            w.plot_note("$sherlockは子供たちからここに寄付している本当の人間の名前を聞く"),
            w.plot_note("それは$jackという、巷で噂の盗賊だった"),
            )
