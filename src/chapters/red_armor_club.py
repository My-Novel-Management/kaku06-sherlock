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
from scenes import JakinsHouse
from scenes import Museum
from scenes import PawnShop
from scenes import SherlockHouse
from scenes import Street


# Episodes
def missing_persons(w: World):
    return w.episode("失踪者たち",
            SherlockHouse.housemate_mary(w),
            SherlockHouse.mary_has_worry(w),
            SherlockHouse.about_missings(w),
            SherlockHouse.strange_armor_knight(w),
            )


def strange_work(w: World):
    return w.episode("不思議な仕事",
            SherlockHouse.strange_work(w),
            )


def bank_robbery(w: World):
    return w.episode("銀行強盗",
            Street.mary_walked_lime(w),
            PawnShop.limes_job_place(w),
            JakinsHouse.orners_home(w),
            SherlockHouse.reason_for_lime_work(w),
            )


def truth_of_club(w: World):
    return w.episode("クラブの真相",
            SherlockHouse.help_lime_please(w),
            Street.meaning_for_his_advice(w),
            Museum.alibi_proof(w),
            )


def what_was_stolen(w: World):
    return w.episode("盗まれたもの",
            JakinsHouse.orners_talk(w),
            SherlockHouse.limes_talk_of_strange_case(w),
            )


def new_living(w: World):
    return w.episode("新しい居候",
            SherlockHouse.lime_was_royal_family(w),
            SherlockHouse.newcommer_lime(w),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[3],
            # NOTE
            #   事件：赤鎧クラブという奇妙な仕事　→銀行強盗／バイトの$bins殺害
            #   被害者：銀行の大金庫の宝石群／$bins
            #   容疑者：オーナー夫婦／$lime
            #   犯人：$binsたち強盗団／強盗団（$bins殺害）
            #   依頼人：$maryと$lime
            #   トリック：奇妙な仕事による偽装（割のいいバイトで遠ざけている間に地下通路を掘り、銀行の大金庫から物を奪う
            #   結果：銀行から大量の宝石が盗まれた、中には国宝の$stoneも含まれていた／$limeが解雇され、住居がなくなった
            #   ポイント：古代の武具（非$science的装備）／第二王女／裏で手を引く何者か
            w.plot_setup("$maryが一緒に暮らすようになり、家事の担当を彼女がするようになった"),
            w.plot_setup("しかし$maryは料理経験もなく、掃除もうまくいかない"),
            w.plot_setup("それでも健気に市場に買い出しに行く、$wilsonの金で"),
            w.plot_setup("$sherlockは新聞を見て今日も事件を探していた"),
            w.plot_setup("$jackの活動が沈静化していた"),
            w.plot_setup("国営銀行が改装中で、完成すると世界一堅牢な大金庫ができるとあった"),
            w.plot_turnpoint("$maryが事情を抱えた謎の鎧騎士$limeを連れてくる"),
            w.plot_develop("その騎士$limeはしゃべることができず、筆談で話す"),
            w.plot_develop("今は質屋を経営する老夫婦の許に世話になっている"),
            w.plot_develop("質屋の仕事は自分とアルバイトの$binsに任せられているが、今はもう一つ別のバイトもしていると"),
            w.plot_develop("それが奇妙な募集で、赤い鎧を着た者だけに資格がある赤鎧クラブというものだった"),
            w.plot_develop("見事合格し、毎日平日の午後に三時間、そこの大切な書物の写本を作っている"),
            w.plot_develop("世話になったオーナー夫婦に何か返してあげたいとの思いからだが、こんなことをしていていいのかなと不安があると"),
            w.plot_develop("$sherlockはすぐそのバイトを辞めた方がいいとだけ忠告した"),
            w.plot_turnpoint("後日、突然$limeの赤鎧クラブは閉鎖した"),
            w.plot_develop("新聞記事に小さく載ったその記事を見つけて、$maryに事情を説明する$sherlock"),
            w.plot_develop("何か事情があって$limeが店から遠ざけられていたんだと"),
            w.plot_develop("いい人だというその$binsを疑うべきだ、と説明した"),
            w.plot_turnpoint("しかし$binsは死体となって発見された"),
            w.plot_develop(""),# TODO
            w.plot_turnpoint("銀行強盗の容疑者にオーナー夫婦と$limeがなる"),
            w.plot_turnpoint("強盗団が殺害されて発見される"),
            w.plot_turnpoint("$maryが途方に暮れていた$limeを連れてくる"),
            w.plot_develop("$sherlockは$limeを教会に連れていき、知人の神官に騎士の呪いを解かせた"),
            w.plot_develop("しゃべれるようになった$limeだったが、ほとんど口をきかない"),
            w.plot_develop("$maryを通して$limeがどうして呪いの鎧を着てしまったのか、事情を聞く"),
            w.plot_turnpoint("$limeは自分が失踪中の第二王女だと語った"),
            w.plot_resolve("$maryのお願いで、$limeを居候させることになった"),
            #
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


