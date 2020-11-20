# -*- coding: utf-8 -*-
'''
Chapter "悲しみの谷"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Episodes
def sadness_case(w: World):
    return w.episode("悲しい事件",
            w.plot_note("$sherlockは新聞を読んでいた"),
            w.plot_note("$wilsonがやってきていつも何か読んでいるねと言う"),
            w.plot_note("$sherlockは新聞に掲載されていた田舎町の事件を説明する"),
            w.plot_note("殺人事件の多くがこういった「身内の揉め事」だと"),
            w.plot_note("ただ娘が利用した$itemが気になると言う"),
            w.plot_note("$wilsonはそんな事件よりも自分の依頼の方をがんばってほしいと言う"),
            w.plot_note("$wilsonは$sherlockに最近増えている謎の失踪事件についての調査を依頼していた"),
            w.plot_note("$sherlockは調査中とだけ答えて何も言わない"),
            w.plot_note("そこに見知らぬ男の子が訪ねてきて、その事件の容疑者を助けてほしいとお願いされた"),
            )


def country_town(w: World):
    return w.episode("田舎町",
            w.plot_note("$keanはある屋敷に務める使用人の一家の息子だった"),
            w.plot_note("彼は自分が使えている家でその殺人事件があったと言う"),
            w.plot_note("その容疑者になっているのがその家の一人娘だが、彼女は絶対にそんなことをしないと力説する"),
            w.plot_note("なけなしの金を見せて$sherlockに頼む"),
            w.plot_note("$wilsonがそんなはした金で受けるのかと尋ねたが$sherlockは「仕事だよ」と席をたった"),
            w.plot_note("駅から$trainにのって$Dartmourに向かう"),
            w.plot_note("そこに迎えにきていた$keanに案内され、まずは屋敷に向かう"),
            w.plot_note("屋敷の主となった、残された母親の$jeanに出会う"),
            w.plot_note("$jeanはどうしてこんなことになったのか分からないと嘆く"),
            w.plot_note("ただ使用人の$kailが二人が言い争うのを聞いていて、それが決定的な証拠になっているらしい"),
            # TODO
            w.plot_note("容疑者として警察に捕まっている少女に会えることになった"),
            )


def suspect_girl(w: World):
    return w.episode("容疑者の少女",
            w.plot_note("$sherlockは$wilsonに彼女が$animalであると告げた"),
            )


def her_mother(w: World):
    return w.episode("彼女の母親",
            w.plot_note("そこに$maryが連れてこられた"),
            )


def real_murder(w: World):
    return w.episode("真犯人",
            w.plot_note("$maryが獣化した"),
            )


def animal_girl(w: World):
    return w.episode("獣の少女",
            w.plot_note("$cherryは自分を守った$maryのことを「それでもお前のことを好きになれない」と言って、警察に逮捕された"),
            )


def living_girl(w: World):
    return w.episode("新しい同居人",
            w.plot_note("$maryが$sherlockたちの家に居候することになった"),
            )



# Chapter
def main(w: World):
    return w.chapter(TITLES[2],
            w.plot_setup("田舎町で$gunを使った殺人事件が発生する"),
            w.plot_turnpoint("$sherlockのところにその容疑者になった女の子を助けてくれと電報が届く"),
            w.plot_develop("$sherlockと$wilsonはその田舎町に向かい、情報を集める"),
            w.plot_turnpoint("$maryが$animalだと$sherlockは言う"),
            w.plot_develop("$maryのことを調べていくと彼女が拾われた子供だと分かる"),
            w.plot_turnpoint("$maryが犯人に断定される"),
            w.plot_develop("$sherlockは真犯人を解明するために$maryの母親と使用人に再度話を聞く"),
            w.plot_turnpoint("$maryが獣化する"),
            w.plot_develop("母親を始末しようとした男から$maryが守るが、彼女の姿を見て殺人の自白をする母。逮捕された"),
            w.plot_turnpoint("$maryは財産贈与の全てを放棄した"),
            w.plot_resolve("保護者と住居を失った$maryが$sherlockの許にやってきて、居候させてとお願いした"),
            sadness_case(w),
            country_town(w),
            suspect_girl(w),
            her_mother(w),
            real_murder(w),
            animal_girl(w),
            living_girl(w),
            )


