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

# NOTE: outlines
OUTLINES = [
        "$maryが同居人になり彼女が家事を買って出てくれたが上手ではなかった。$sherlockは$wilsonからの依頼も調査しつつ事件記事を探す。市場から帰ってきた$maryはそんな$sherlockに相談があると、謎の鎧騎士を連れてきた",
        "$limeという名の鎧騎士は喋れなかった。筆談による説明で彼が質屋の守衛以外にも紹介された奇妙なバイトをしていると話す。それが赤鎧クラブだった。しかし$sherlockは彼にすぐそのバイトを辞めるよう忠告した",
        "数日後、再び$limeが訪れる。突然赤鎧クラブが閉鎖され、バイトがなくなったという。$sherlockは一緒にいき、質屋の地下に掘られていた抜け穴を見つける。それは近所の国営銀行の大金庫に繋がっていた。その中で$limeの仕事仲間の$jakinsが死んでいた",
        # $limeが容疑者となる
        "$limeが殺人と宝石強盗の容疑者となり逮捕される。$sherlockは赤鎧クラブが$limeを店から遠ざけておくための口実で、本来の目的は銀行強盗だったと説明する。赤鎧クラブを作った男を調べていくと、強盗団に繋がる。その強盗団が爆発現場で死体で発見された",
        "盗まれたものは見つからずに事件は解決を見る。$limeは世話になっていたオーナー夫婦を離れ、$sherlockのもとを訪れる。そこで彼女は自分が失踪中の第二王女だと告白した",
        "$limeは失踪した訳ではなく自分で誘拐犯に捕まった。事情があって王室を離れたかったと語る。王室に帰ることもできず、$limeは$sherlockの家でしばらく世話になることになった",
        ]

# NOTE: charas
#   ・$nowlis（本物の$wilsonだが、色々隠れて世界の動向を伺っている。元勇者の仲間。永遠の生命を持つ、外の世界から来た男
#   ・$lime（初出。実は第二王女だが最後の方まで明かされない
#   ・$jakins（ここのみ。質屋オーナー。$limeを拾ってくれた。孤児院に寄付をしている
#   ・$jeena（ここのみ。質屋オーナーの妻。人を疑うことを知らない

# NOTE: stages
#   ・市場（$maryがよく行く場所になる。ここでしっかり描いておく
#   ・国営銀行（改装中。コレクタ$philoの$bossの遺品が保管されている

# NOTE: items
#   ・$white_stone（銀行にあった

# NOTE: case
#   ・赤い鎧騎士だけ募集していた奇妙な仕事　→$limeを店から遠ざける為で、その間に国営銀行の大金庫へ繋がる抜け穴を掘っていた
#   ・$jakins殺害事件　→仲間割れと口封じで殺された。その強盗団も港の船の事故？爆発によって死去

# NOTE: tech
#   ・

def silent_knight(w: World):
    return w.episode("沈黙の騎士",
            #   NOTE
            #   ・$maryが加わって
            w.plot_setup("$maryが$sherlockの家で同居するようになった"),
            w.plot_setup("$maryは$sherlockを慕っているのに、いつも冷たい態度で憤慨"),
            w.plot_setup("$sherlockは新聞記事から失踪事件に関係するものを集めていた"),
            w.plot_setup("$wilsonは第二王女失踪についての情報を集めている"),
            w.plot_turnpoint("$maryは市場に買い出しに行く"),
            "ここで市場をしっかり描く",
            #   ・市場の$mary
            w.plot_develop("市場に頻繁に顔を出している$maryは、知人が増えていた"),
            w.plot_develop("少年探偵団の$ignesも普段は市場で働いている"),
            w.plot_develop("$maryは$sherlockの愚痴を言うが、$ignesは憧れている"),
            w.plot_develop("肉屋の$nowlisはいつもおまけしてくれる"),
            w.plot_turnpoint("$maryは不審な鎧騎士を見つけた"),
            #   ・闇マーケット
            w.plot_develop("$sherlockは情報収集のために裏通りにやってくる"),
            w.plot_develop("$sherlockは待ち合わせていた情報屋$flenから今の動向を聞く"),
            w.plot_develop("妙な動きがあるが、よくわからないと言われる"),
            w.plot_develop("最近出回っている改造$gunについての情報を得る"),
            #   ・経過報告
            w.plot_develop("$sherlockは$wilsonに失踪人調査の経過報告をする"),
            w.plot_develop("ちょっと記事を調べただけでこの一年あまりの間に二十名以上が失踪している"),
            w.plot_develop("ただどれが事件の関係者で、そうでないのか分からない"),
            w.plot_develop("そもそも記事に載らない失踪者の方が多く、誰も気にしていないこと"),
            w.plot_develop("少年探偵団にも声をかけているが、まだ先は長そうだと"),
            w.plot_turnpoint("そこに$maryが謎の鎧騎士を連れて戻ってくる"),
            outline=OUTLINES[0])


def strange_part_time_job(w: World):
    return w.episode("奇妙なアルバイト",
            # NOTE
            #   ・謎のアルバイト
            w.plot_setup("$maryが連れてきた鎧騎士は$limeと名乗った"),
            w.plot_setup("$limeは口がきけず、筆談で話す"),
            w.plot_setup("困っているところを助けたと$maryは言う"),
            w.plot_develop("$limeは$sherlockに相談をした"),
            w.plot_develop("$limeは呪いの鎧を着てしまい、それが外せなくなり、困っていたところを今の質屋夫婦に拾われた"),
            w.plot_develop("今は質屋で守衛をやっている"),
            w.plot_develop("一月ほど前に同僚の$jakinsからあるバイトを紹介された"),
            w.plot_develop("それが奇妙なバイトで赤い鎧を着た人間だけを募集していた"),
            w.plot_develop("面接で合格し、毎日三時間だけ通うことになった"),
            w.plot_develop("その間、店番と守衛は$jakins一人でやってくれるという"),
            w.plot_develop("$limeは拾ってもらったお礼をしたくて、小遣いが欲しかった"),
            w.plot_develop("それでも黙ってやっていて悪いんじゃないかと、気になっているらしい"),
            w.plot_turnpoint("$sherlockは彼女にそのバイトをすぐ辞めるように、とだけアドバイスをした"),
            #   ・$limeと質屋夫婦
            w.plot_develop("$maryは$limeを送っていく"),
            w.plot_develop("$limeの質屋は雑居店街にあった"),
            w.plot_develop("少し出ると大通りで改装中の国営銀行なども並ぶ"),
            w.plot_develop("オーナー夫婦の家は近所で、$maryは顔合わせだけした"),
            w.plot_develop("いい夫婦で$maryに遊びにくるように言ってくれた"),
            #   ・事情説明
            w.plot_develop("戻った$maryは$sherlockに何故あんなことを言ったのか問い詰める"),
            w.plot_develop("$sherlockはそんな赤い鎧を着た人間だけを集めている仕事がある訳がないと"),
            w.plot_develop("別の目的があって彼女をその場所に置いておきたいか、監視したいか、そういったものだと"),
            w.plot_develop("彼女に何の特もないし、すぐにやめた方が安全だと"),
            w.plot_turnpoint("後日、$maryは$limeから、突然赤鎧クラブが閉鎖になったと報告があったと聞いた"),
            outline=OUTLINES[1])


def bank_robbery(w: World):
    return w.episode("銀行強盗",
            # NOTE
            #   ・バイト仲間失踪
            w.plot_setup("$maryから$limeのバイトが突然なくなったと伝え聞いた"),
            w.plot_setup("$sherlockは何か変化がなかったかと尋ねる"),
            w.plot_setup("店にいったらこの前会った店員の$jakinsがいなかったと"),
            w.plot_turnpoint("$limeがやってきて、$jakinsが失踪したと言ってきた"),
            w.plot_develop("警察に届け出は出したものの、店はとりあえずオーナーに任せて、探して歩いていると言う"),
            w.plot_develop("$sherlockは$ignesたちに指示をして、探してもらう"),
            w.plot_develop("その間に気になるからと店に案内してもらった"),
            #   ・店の調査
            w.plot_develop("質屋にやってくる$sherlock"),
            w.plot_develop("オーナーと出会い、$jakinsがどんな人物だったか話を聞く"),
            w.plot_develop("$jakinsは好青年で、前働いていた夫人が産休で長く店を開けるからと、張り紙をしておいて、募集でやってきた"),
            w.plot_develop("あまり給料は払えないが、それでも社会勉強になるからと働き始めた"),
            w.plot_develop("物覚えも手際もよく、もっと他の仕事につけそうだった"),
            w.plot_develop("やがて店を一人で任せられるまでになった"),
            w.plot_develop("一月前に$limeを拾ってからは、彼女の宿泊代として守衛をやってもらった"),
            w.plot_develop("少額ながら慈善事業もやっていたので、一人くらいなら寝食の世話もいとわなかった"),
            w.plot_turnpoint("そこに$patsonがやってきて、オーナーを逮捕すると言い出した"),
            outline=OUTLINES[2])


def the_end_of_case(w: World):
    return w.episode("事件の顛末",
            # NOTE
            #   ・銀行強盗
            #   ・$limeの容疑を晴らす
            w.plot_setup("失踪した$jakinsを探して店に調べにやってきた$sherlock"),
            w.plot_setup("オーナーを逮捕しに$patsonが現れた"),
            w.plot_setup("$patsonは銀行強盗の容疑で逮捕すると言う"),
            w.plot_setup("改装中の国営銀行の大金庫に穴があいていて、そこを辿るとこの店の地下に繋がっていた"),
            w.plot_turnpoint("更にその地下道で$jakinsの遺体が発見される"),
            #   ・殺人事件
            w.plot_develop("$jakins殺害の容疑者として$limeが逮捕される"),
            w.plot_develop("オーナー夫婦も参考人として聴取される"),
            w.plot_develop("$sherlockは$limeが店を離れている間に穴を掘っていたと言う"),
            w.plot_develop("それを仕組んだのは$jakinsだが、仲間に口封じで殺されたんだろうと"),
            w.plot_develop("殺害手口は弾の残らない改造$gunだった"),
            w.plot_develop("一連のつながりを感じつつ、$limeたちの無実を証明するためにアリバイを探す"),
            w.plot_develop("オーナー夫婦は地元の商工会の会合にでかけていてアリバイがあった"),
            w.plot_turnpoint("$limeは$maryと一緒にオーナー夫婦へのプレゼントを選びに出かけていたのが証明された"),
            outline=OUTLINES[3])


def her_identity(w: World):
    return w.episode("鎧騎士の正体",
            # NOTE
            #   ・事件解決
            w.plot_setup("$limeたちの容疑が晴れた"),
            w.plot_setup("しかし質屋は閉店することが決まった"),
            w.plot_turnpoint("後日、銀行強盗の一団と見られる集団が、火事になった空き家で死んでいるのが発見された"),
            w.plot_develop("事件は盗まれたものが見つからないまま解決になった"),
            #   ・盗まれたもの
            w.plot_develop("$sherlockは改装が終わった銀行を訪れる"),
            w.plot_develop("そこにいたのは兄の$mikelだった"),
            w.plot_develop("$mikelは$sherlockに自分が斡旋する仕事につけと命じる"),
            w.plot_develop("$sherlockは無視して、役員から盗まれたものを聞き出す"),
            w.plot_develop("盗まれたのは宝石以外に$white_stoneも含まれていた"),
            #   ・$limeの事情
            w.plot_turnpoint("$limeを$maryが連れてくる"),
            w.plot_resolve("家を出た$limeは、行き場を失って困っていた"),
            w.plot_resolve("そこを再び$maryが拾ったらしい"),
            w.plot_resolve("$sherlockは知人の神官に頼み、$limeの呪いを解いてもらった"),
            w.plot_resolve("話せるようになった$lime"),
            w.plot_turnpoint("$limeは失踪中の第二王女だと告白した"),
            outline=OUTLINES[4])


def limes_reason(w: World):
    return w.episode("$limeの事情",
            # NOTE
            #   ・$limeの告白
            w.plot_setup("口がきけるようになった$limeは失踪中の第二王女と告白する"),
            w.plot_setup("$limeは$sherlockたちに事情を話し始めた"),
            w.plot_develop("$limeは正室の子ではなく、王が遊女に産ませた存在だった"),
            w.plot_develop("そのことを隠しつつ育てられたが周囲はなんとなく知れ渡り、扱いがぞんざいだった"),
            w.plot_develop("政略結婚の道具としてしか存在価値がなく、そんな自分が嫌だった"),
            w.plot_develop("そんな$limeの部屋にある日誘拐犯が現れる"),
            w.plot_develop("$limeは頼み込んでその泥棒に誘拐してもらう"),
            w.plot_develop("泥棒は$limeを売り飛ばすつもりだったが、彼女はそこにあった鎧を着て逃げ出す"),
            w.plot_develop("その鎧が呪いの鎧だったためにしゃべれなくなり、現在に至る"),
            #   ・$limeも一緒に暮らし始める
            w.plot_turnpoint("$limeはここにしばらく置いてもらえないかとお願いする"),
            w.plot_develop("$sherlockはこれ以上住人が増えるとどうしようもないと言い、断る"),
            w.plot_develop("$maryが$limeのぶんも働いてなんとかすると言い出す"),
            w.plot_develop("$sherlock一人が反対となり、孤立する"),
            w.plot_resolve("仕方なく承諾し、$limeも$sherlockの家でしばらく一緒に暮らすことになった"),
            outline=OUTLINES[5])


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


