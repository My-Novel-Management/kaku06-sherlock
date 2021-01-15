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
ABSTRACT = """
$maryが同居人となり家事全般を担当するようになった$sherlock宅。しかし彼女は致命的に下手だった。何度も失敗し、落ち込んで市場に買い出しに向かった$maryは、そこで自分よりも更に落ち込んでいる謎の鎧騎士を見つける。彼（彼女）は言葉が喋れず、身振り手振りの会話で困っていることが分かり、便利屋$sherlockを紹介する。
$limeと名乗った鎧騎士は拾ってもらった質屋オーナー夫婦の店の守衛を仕事にしているが、店の管理の方を担当している店員の$jakinsから特別な仕事を紹介された。それは赤い鎧を着た者だけに資格があり、赤鎧クラブという名前の古くからある団体の機密文書の写本をするというものだった。
割のいいバイトだが、午後から三時間程度黙って店を離れているので気がかりだと相談する。
$sherlockはすぐにその仕事を辞めるように忠告したが、$limeにも事情があるようだった。
数日後、$limeは再び$sherlock宅にやってくる。突如赤鎧クラブが解散してアルバイトが無くなり、おまけに店員の$jakinsが失踪してしまったというのだ。
$sherlockは$limeたちにあのアルバイトも赤鎧クラブも本当の目的のためのダミーであり、それは$jakinsを含めた集団が仕組んだもので、既に目的が達成された為にいなくなったと説明する。
その目的が改装中の国営銀行の大金庫に質屋の地下から抜け道を掘って宝石を盗み出すことだったと判明するが、その地下道で$jakinsが殺されているのが発見され、$limeは殺人の容疑者になってしまった。
$sherlockは彼の容疑を晴らす為、事件の調査に乗り出す。だが別件で、火災現場から見つかった謎の複数名の焼死体が銀行強盗団だったと分かり、強奪された宝石が見つからないまま事件は解決になった。
後日、世話になったオーナー夫婦の家を出た$limeは、自分が失踪中の第二王女だと告白し、事情があるからしばらく置いて欲しいと$sherlockに依頼した。
"""
OUTLINES = [
"""
$maryが一緒に暮らすようになり、彼女が家事に関する全てを買って出てくれた。だが$maryは経験がなく、おまけに壊滅的に下手だった。
今日も料理を失敗し、落ち込んで市場に買い出しに行く$maryを見送りつつ、$sherlockは$wilsonからの依頼で記事を調査する。
謎の失踪事件についての記事はいくつかあったが、関連性が見えてこない。それとは別の最近猟奇的な殺され方をしている事件があった。そちらはまだ話題になっていなかったが気になるという$sherlock。
一方買い物に出かけた$maryは$ignesたちと面識ができ、少し喋れるようになっていた。彼らに色々と紹介してもらい、市場の人間たちとも馴染みつつあった。彼女が$animalということで最初は奇異に見られたが、それも今でもマスコット的な存在となっていた。
帰り道、$maryは真っ赤な鎧を着た騎士を見つける。彼は困惑した様子で、$maryは思わず声を掛けた。
$maryが謎の鎧騎士を連れてくる。しかしその鎧騎士は話すことができなかった。
""",
"""
しゃべれない鎧騎士は筆談で$limeと名乗った。困っていたのは自分のアルバイトについて。
こんな状態になり、拾ってもらった質屋オーナー夫婦宅に居候していて、その代わりに質屋の守衛をやっていたが、仕事の同僚$jakinsからある奇妙なアルバイトを紹介された。
それが赤鎧クラブという聞いたこともない集まりだった。
赤い鎧を着た者だけが仕事を受けられ、$limeは見事にそれに合格し、週に五日、午後の三時間を赤鎧クラブに出向いて、そこの大事な古文書を写本するだけでかなりいい給料がもらえる。
$limeはそれでオーナー夫婦に何か恩返しをしたいと思っているというが、守衛の仕事をサボっていることと、黙ってアルバイトをしていることが引っかかっているという。
$sherlockはすぐそのアルバイトを辞めるよう進言する。理由は話さない。
落ち込む$limeを送っていく$maryだった。
後日、再び訪れた$limeは突然赤鎧クラブが閉鎖になり、更には同僚の$jakinsが失踪したと言った。
""",
"""
$sherlockはまず赤鎧クラブの場所を調べる。$limeが見たという張り紙すら消え、完全に何もなかったことになっていた。
不動産屋にその件を調べてもらうよう、大家の$lisaに頼む。
次は質屋を調べる。旧市街地にあり、すぐに大通りに繋がる場所。近所には改装中の王立銀行もあった。
質屋の店舗は小さいもので、前の店舗部分と奥の控室、更に倉庫となっている。$limeとオーナー夫婦は近所の別の家で暮らしているという。
$sherlockは普段の$limeと$jakinsの仕事内容を聞き、$jakinsに何か起こって失踪した可能性を考える。だが高額なものは置かれておらず、盗まれた形跡もない。
調べてみると、奥の部屋から地下入り口があり、そこからどこかに抜け穴が掘られていた。また近隣の聞き込みから日中頻繁に複数の男が出入りしては大きな袋を運び出していたとも。
その通路を進んでいくと、途中で失踪していた$jakinsの遺体を発見する。更にそれが改装中の銀行の大金庫へと繋がっていたことが分かった。
警察により殺人事件の容疑者として$limeが浮上した。
""",
        # $limeが容疑者となる
"""
$sherlockは$maryに、赤鎧クラブが$limeを店から遠ざけておくための口実だったと語る。
その間に地下道を掘り、大金庫から何かを盗み出した。現金や金の延べ棒、宝石など多数が強奪されていたという。
$limeの証言が赤鎧クラブが存在しなかったことで嘘とみなされ、容疑を晴らせない。
$sherlockは$jakinsがどこから来たのかを辿っていく。やがて賭け事で借金を背負い、裏組織とつながりがあることが判明した。
ただそこから先が辿れず、$sherlockは情報屋に宝石の売買などを洗ってもらっていた。
その後、強盗団が火災現場で遺体となって発見されたことが$restradeから伝えられた。
""",
"""
$sherlockにより$limeの疑いが晴れた。
しかし$limeは質屋オーナー夫婦に悪いと、家を出る。
孤独になった$limeを、$maryが再び拾って家へと連れてきた。
$maryは自分も働くから何とか置いてもらえないかと頼む。$sherlockは思案するが。
そこで$limeはある告白を始めた。自分が何故こういう状況になっているのか。
$limeは自分が失踪中の第二王女だと告白した。
""",
"""
第二王女と告白した$limeは、事情があり、王室ではずっと肩身の狭い思いをしていて、逃げ出したいと思っていた。
ちょうどそこに泥棒が入ってきたので誘拐してもらった。けれど売り飛ばされる相談が聞こえて途中で怖くなり、物置にあった鎧を着て逃げ出したのだが、どうやら鎧に呪いがかかっていたようでしゃべれなくなり、途方にくれていたところを質屋夫婦に拾ってもらった。
出ていかなくていいと言ってはくれたが迷惑になるので、出てきたと。
$sherlockは$limeを連れ出し、知人の神官のところで呪いを解いてもらう。
$limeは事情を語った上で、$sherlockに王室に戻らなくて済むようにしばらくここで生活させてほしいと頼む。渋った$sherlockだったが王室の人間にバレたらその時は素直に戻るという条件付きで、棲まわせることにした。
""",
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
            w.plot_setup("$maryが一緒に暮らすようになり家事全般を担当してくれるようになったが彼女は壊滅的に下手だった"),
            w.plot_turnpoint("失敗して落ち込む$maryは市場に買い出しに向かう"),
            w.plot_develop("$wilsonは$sherlockにもう少し$maryに対して優しく扱ってやればと進言するが$sherlockは興味がない。ただ$wilsonの依頼である第二王女失踪に関する記事を集めてくれていた"),
            w.plot_turnpoint("$maryは市場で困っている赤い鎧騎士を見つける"),
            w.plot_resolve("$maryが困っていた鎧騎士を拾って連れて帰ってくる"),
            w.plot_turnpoint("$maryが連れてきた鎧騎士は喋ることができなかった"),
            outline=OUTLINES[0])


def strange_part_time_job(w: World):
    return w.episode("奇妙なアルバイト",
            # NOTE
            w.plot_setup("筆談で$limeと名乗った喋れない鎧騎士は$sherlockに相談したいことがあると言った"),
            w.plot_turnpoint("$limeは自分がしている奇妙なアルバイトについて語り出す"),
            w.plot_develop("$limeは仕事の同僚に紹介された赤鎧クラブという赤い鎧を来た者だけが資格のある不思議なアルバイトをしていた。給料がよかったが、仕事を途中でサボっているみたいで気が進まないと相談する"),
            w.plot_turnpoint("$sherlockは$limeにすぐアルバイトを辞めるように進言した"),
            w.plot_resolve("$maryは$sherlockの失礼を謝りつつも$limeを質屋まで送っていく"),
            w.plot_turnpoint("後日、再度$limeがやってきて赤鎧クラブが閉会されたと言った"),
            outline=OUTLINES[1])


def closed_red_armor_club(w: World):
    return w.episode("閉じた赤鎧クラブ",
            # NOTE
            w.plot_setup("$limeから赤鎧クラブが閉会したことと同僚$jakinsが失踪したことを聞く$sherlock"),
            w.plot_turnpoint("$sherlockは赤鎧クラブの調査に向かう"),
            w.plot_develop("$limeの言う通り赤鎧クラブは存在そのものが消え去っていた。続いて質屋を調べると奥に地下道を発見する"),
            w.plot_turnpoint("地下道の途中で$jakinsが殺されていた"),
            w.plot_resolve("地下道は改装中の国営銀行の大金庫まで繋がっていて、中から大量の宝石が盗まれていた"),
            w.plot_turnpoint("$jakins殺害容疑で$limeが逮捕された"),
            outline=OUTLINES[2])


def the_end_of_case(w: World):
    return w.episode("事件の顛末",
            # NOTE
            w.plot_setup("$maryに頼まれて$sherlockは$limeの容疑を晴らすために調査を開始する"),
            w.plot_turnpoint("$sherlockは赤鎧クラブの存在が$limeを店から遠ざけるためだったと語る"),
            w.plot_develop("質屋オーナー夫婦から聞き取りをして$jakinsがそもそも銀行の大金庫から宝石を盗み出す目的で近づいたこと等を突き止める"),
            w.plot_turnpoint("$jakinsが大量に借金をしていたことが判明する"),
            w.plot_resolve("$jakinsの昔の知人から組織とつながりがあり脅されていたことを知る"),
            w.plot_turnpoint("$jakinsの仲間と見られる強盗団が火災現場から遺体となって発見された"),
            outline=OUTLINES[3])


def her_identity(w: World):
    return w.episode("鎧騎士の正体",
            # NOTE
            w.plot_setup("強盗団が全員死んだことと$sherlockの調査により$limeの疑いが晴れた"),
            w.plot_turnpoint("$limeが釈放されたと連絡を受ける"),
            w.plot_develop("無実となった$limeだったが迷惑をかけたとオーナー夫婦の許を去った。だが路上でどうしようと困っていて、再び$maryに拾われる"),
            w.plot_turnpoint("$maryが$limeを連れてくる"),
            w.plot_resolve("$limeは$sherlockたちに自分がどうしてこうなっているのか、事情を話す"),
            w.plot_turnpoint("$limeは$sherlockたちに自分は失踪中の第二王女だと語った"),
            outline=OUTLINES[4])


def limes_reason(w: World):
    return w.episode("$limeの事情",
            # NOTE
            w.plot_setup("第二王女だと語った$limeは自分がどうしてこうなっているのかという事情を$sherlockたちに話した"),
            w.plot_turnpoint("$limeは泥棒に自分から誘拐してくださいと頼んだ、と語る"),
            w.plot_develop("$limeは誘拐された先で売り飛ばされる計画を聞いて、逃げ出す時に物置にあったこの呪いの鎧を着てしまい、困っていたところを質屋オーナー夫婦に拾われたと語る"),
            w.plot_turnpoint("$sherlockは$limeの呪いを知人の神官に解いてもらう"),
            w.plot_resolve("$limeは王室に戻りたくないのでしばらくここで置いてもらえないかと頼み込んだ"),
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
            #
            silent_knight(w),
            strange_part_time_job(w),
            closed_red_armor_club(w),
            the_end_of_case(w),
            her_identity(w),
            limes_reason(w),
            outline=ABSTRACT)


