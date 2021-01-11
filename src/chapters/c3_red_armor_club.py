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
            #
            silent_knight(w),
            strange_part_time_job(w),
            bank_robbery(w),
            the_end_of_case(w),
            her_identity(w),
            limes_reason(w),
            outline=ABSTRACT)


