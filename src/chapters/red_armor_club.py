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
# NOTE
#   .沈黙の鎧騎士＞謎の鎧騎士を連れてくる
#   .奇妙なバイト＞$sherlockはバイトを辞めるよう忠告
#   .銀行強盗＞$limeが容疑者となる
#   .事件の結末＞強盗団の死
#   .鎧騎士の正体＞$limeは第二王女
#   .事情あり、にて＞$limeが同居人となる

# NOTE：初出
#   ・市場
#   ・$nowlis

def silent_knight(w: World):
    return w.episode("沈黙の騎士",
            w.plot_setup("$maryが$sherlockの家で同居するようになった"),
            w.plot_setup("$maryは$sherlockを慕っているのに、いつも冷たい態度で憤慨"),
            w.plot_setup("$sherlockは新聞記事から失踪事件に関係するものを集めていた"),
            w.plot_setup("$wilsonは第二王女失踪についての情報を集めている"),
            w.plot_turnpoint("$maryは市場に買い出しに行く"),
            "ここで市場をしっかり描く",
            w.plot_develop("市場に頻繁に顔を出している$maryは、知人が増えていた"),
            w.plot_develop("少年探偵団の$ignesも普段は市場で働いている"),
            w.plot_develop("$maryは$sherlockの愚痴を言うが、$ignesは憧れている"),
            w.plot_develop("肉屋の$nowlisはいつもおまけしてくれる"),
            w.plot_turnpoint("$maryは不審な鎧騎士を見つけた"),
            w.plot_develop(""),
            w.plot_turnpoint("$maryが謎の鎧騎士を連れて戻ってくる"),
            )


def strange_part_time_job(w: World):
    return w.episode("奇妙なアルバイト",
            w.plot_turnpoint("$sherlockは彼女にそのバイトをすぐ辞めるように、とだけアドバイスをした"),
            w.plot_turnpoint("$maryは$limeから、突然赤鎧クラブが閉鎖になったと報告があったと聞いた"),
            )


def bank_robbery(w: World):
    return w.episode("銀行強盗",
            w.plot_turnpoint("$limeが容疑者になった"),
            )


def the_end_of_case(w: World):
    return w.episode("事件の顛末",
            w.plot_turnpoint(""),
            )


def her_identity(w: World):
    return w.episode("鎧騎士の正体",
            w.plot_turnpoint("$limeは失踪中の第二王女だった"),
            )


def limes_reason(w: World):
    return w.episode("$limeの事情",
            w.plot_resolve("$limeも$sherlockの家でしばらく一緒に暮らすことになった"),
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
            #   ポイント：古代の武具（非$science的装備）／第二王女／裏で手を引く何者か／$stone白
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
            w.plot_turnpoint("しかし$binsは失踪し、後日死体となって発見された"),
            w.plot_develop("$bins殺害の容疑者としてオーナー夫婦と$limeが逮捕される"),
            w.plot_develop("またその捜査の過程で、質屋から地下通路によって改装工事中の国営銀行に繋がっていることが判明"),
            w.plot_develop("オーナー夫婦と$limeは大金庫から宝石を盗んだ罪にも問われる"),
            w.plot_turnpoint("$maryからの頼みで、$limeたちの容疑を晴らすために$sherlockは調査する"),
            w.plot_develop("$sherlockは$binsが最初から質屋オーナー夫婦に近づいたと話す"),
            w.plot_develop("最初は自分一人で店番をしていたが、$limeが現れて邪魔になり、仕方なく今回の赤鎧クラブを考え出したと"),
            w.plot_develop("しかし$binsが殺されていることから、首謀者は他にいて、その人物たちが銀行から宝石を持ち出した"),
            w.plot_develop("$sherlockは闇のマーケットにそれらが出ていないか情報を調べる"),
            w.plot_turnpoint("しかし強盗団が殺害され、宝石も一緒に発見された"),
            w.plot_develop("事件は謎を残したまま強盗団の事故死により解決した"),
            w.plot_develop("だが現場検証した$restradeはみんな殺されてから放火されていたことに言及し、$sherlockに意見を求める"),
            w.plot_develop("$sherlockは盗まれた宝石が全て見つかったのかと尋ねる"),
            w.plot_develop("宝石の中で国宝の白$stoneが消えていたと語った"),
            w.plot_turnpoint("$maryが途方に暮れていた$limeを連れてくる"),
            w.plot_develop("$limeは迷惑をかけたのでオーナー夫婦の好意を断り、家を出てきたと"),
            w.plot_develop("$sherlockは$limeを教会に連れていき、知人の神官に騎士の呪いを解かせた"),
            w.plot_develop("しゃべれるようになった$limeだったが、ほとんど口をきかない"),
            w.plot_develop("$maryを通して$limeがどうして呪いの鎧を着てしまったのか、事情を聞く"),
            w.plot_turnpoint("$limeは自分が失踪中の第二王女だと語った"),
            w.plot_resolve("$wilsonから依頼されていた第二王女失踪事件は、ただの家出と判明する"),
            w.plot_resolve("そしてその誘拐を計画した連中が今回の強盗団に混ざっていたことも分かった"),
            w.plot_resolve("$limeは彼らが誰かからお金をもらって誘拐や強盗などを行っていたと語る"),
            w.plot_resolve("$maryのお願いで、$limeを居候させることになった"),
            #
            silent_knight(w),
            strange_part_time_job(w),
            bank_robbery(w),
            the_end_of_case(w),
            her_identity(w),
            limes_reason(w),
            )


