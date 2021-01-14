# -*- coding: utf-8 -*-
'''
Chapter "青いガーネット"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import Market
from scenes import School
from scenes import SherlockHouse
from scenes import Street


# Episodes
# NOTE
#   .市場のガチョウ＞ガチョウからナイフと宝石が出てくる
#   .凶器のない殺人＞市場の$nowlisや$jackが容疑者となる
#   .ガチョウクラブ＞$maryが捕まる
#   .事件捜査＞$jackが$maryを助ける
#   .事件解決＞$sherlockが$jackとの交換条件を飲む
#   .四つの$stone＞$jackから青$stoneを預かる

# NOTE: outlines
ABSTRACT = """
$limeも同居するようになり$sherlockの周囲に賑やかな日常がやってきた。ただ$limeは$maryとは異なり、家事全般器用にこなし、$sherlockとしては非常に助かる存在になっていた。そのことが$maryには気がかりで、自分の無力さに情けなくなり、市場で仲良くなった肉屋の$nowlisに愚痴っていた。$nowlisはそんな$maryに沢山貰ったからとガチョウを一羽プレゼントしてくれる。
だが家に戻り、$maryはそのガチョウを$limeに捌いてもらったところ、中からナイフと$blue_stoneが出てきた。
警察に届けるとそのナイフに付着していた血液が、凶器が発見されていない殺人事件の被害者のものと一致するということが判明し、ガチョウを渡した$nowlisが容疑者の一人になってしまった。
$maryは容疑を晴らすために一人で事件の調査を開始する。調査の過程でガチョウクラブが浮上し、被害者がガチョウクラブ会員だったことが分かる。
しかしそのクラブが実は$drag密売の為の組織で、取引現場を目撃してしまった為に$maryは捕まってしまう。
$limeは$maryが戻ってこないことを妙に思い、探しに出る。$sherlockは$ignesたちに指示して$maryがどこにいったか探してもらう。その一方で自分は事件調査に乗り出した。
$ignesたちの情報で$maryがガチョウクラブに捕まったことが分かり、$limeは単身、彼女を助けに乗り込む。危うく二人とも殺されそうになるが、そこに警察が突入し、事なきを得た。$sherlockが指示したものだった。
一方、$sherlockは$blue_stoneが$jackによって隠されたものだと分かり、それを取り戻しにきた$jackと出会う。彼女から四つの$stoneが存在することを知らされ、何者かにより企まれていることを阻止して欲しいという依頼をされ、$blue_stoneを預かった。
"""
OUTLINES = [
"""
$limeが同居するようになり、彼女も家事を手伝うようになっていた。だが彼女は$maryと違い、料理も上手で掃除や洗濯も手際よくこなし、$maryは買い物だけが自分の役割になってしまった。そのことについて居場所を失ったような気になり、市場で仲良くなった肉屋の$nowlisに相談する。
一方$sherlockは$wilsonから頼まれていた第二王女失踪の調査が、$limeを見つけたことで一旦解決した。けれど連続失踪事件、および、最近明らかになった連続猟奇殺人事件について独自に調査を進めていた。
$wilsonは$sherlockと$limeから頼まれて、もうしばらく第二王女が見つかったことは内緒にしておくことにした、と言ったが、その裏で王室執務官の$mikelと出会っていた。何とか無事なこと、安全は確保していることを伝えると、$mikelの方で色々と考えると言われた。
$maryは$nowlisから沢山貰ったからとガチョウを一羽まるまるプレゼントしてもらえた。
喜んでそれを持ち帰り、$limeに捌いてもらうとそのガチョウの中からナイフと$blue_stoneが出てきた
""",
"""
何かの事件に関連していると$sherlockが警察に届ける。担当の$restradeがやってきて、凶器が見つからない事件のものの疑いがあると教えてくれる。
事件は資産家の$moura夫人の家から所蔵していたコレクションが数点盗まれた。強盗殺人だったが、凶器が見つからず、ずっと探していたらしい。
ナイフは鑑識に回し、その間に$sherlockに事件解決をしてほしいと依頼する$restrade。
現場に向かった$sherlockだったが、一方$maryは市場の知人、肉屋の$nowlisが容疑者候補に上がっていると聞いて、何とか力になれないかと独自に調査に乗り出す。
$maryは市場でガチョウの入手先を聞き、卸業者を当たり、その先にガチョウクラブというものが存在していると知る。
一方、以前に$sherlockが開発した指紋検出装置により、一緒に入っていた$blue_stoneから$jackの指紋が検出され、一気に$jackが容疑者に躍り出た。
""",
"""
$wilsonから$jackが容疑者として浮上していることを知らされ、$sherlockは$jackについての情報を探ってもらっている情報屋に確認を取る。
特に彼女が国内に戻ってきた情報はなく、最近は$jackによるものと見られる盗難事件もない為に$sherlockは何者かが彼女を利用していると考える。
一方、$maryは$ignesとともにガチョウクラブに潜入する。
会員制でガチョウを安く手に入れられるという表向きだったが、そこには$ignesも知るアンダーグラウンドの大物が出入りしていた。
目をつけられる$maryたちだったが、謎の女性により助けられる。
その女性からもうガチョウクラブには出入りしないように注意される。
一旦家に戻った$maryだったが、$sherlockが調べている事件の被害者がガチョウクラブの会員だと分かり、再度ガチョウクラブへの潜入を決意。
ガチョウクラブの男たちが$drag取引をしている現場を目撃した$maryは、逃げ出そうとして気づかれ、捕まってしまう。
""",
        # $maryがガチョウクラブに捕まる
"""
$limeは$maryが戻ってこないことに気づき、市場に探しに出かける。$ignesからの情報でどうやらガチョウクラブに潜入捜査をしていたことが判明する。
一旦$sherlockに話そうとするが外出中で、$wilsonに手伝ってもらってガチョウクラブに向かうことに。
外出中の$sherlockは彼女が育った孤児院にきていた。そこで教師から彼女が$ajinであることを知らされる。ここに暮らす多くが$ajinだった。
今も毎月彼女から仕送りが届いているらしい。
他にもここの卒業生で仕送りをしてくれている子は多いが、最近になって多額の寄付があったのが、今手広く事業を手がけている男だった。その男からこの前ガチョウを貰ったと喜んでいた。
そのガチョウがガチョウクラブ経由と知る$sherlock。
ガチョウクラブの男たちに捕まえられた$maryは、$animalだとバレて、売り飛ばされそうになっていた。
そこにあの女性が現れ、彼女を助けると言う。その女性$jackだった（別名を名乗るが）。
""",
"""
$jackは$maryを外へと逃してくれようとする。しかし男たちに気づかれ、逆に閉じ込められてしまう。それでも$jackは$sherlockがくると言う。
$maryは$jackも$ajinだと知り、自分の悩みを相談する。$sherlockはどんな人種であろうがそこに妙な感情は抱かないと言う。時折本当に感情があるんだろうかと疑うくらいで、その点で彼は信頼していいと。$maryはほっとする。
一方$sherlockは$limeからの情報を得て、警察に手配する。
その間に再度被害者宅とガチョウの卸業者を調査する。そこで事件の犯人がガチョウクラブの人間ではなく、それに見せかけた彼女の愛人の仕業だと見破る。
ナイフの指紋が検出できないように細工していたのは、その技術が存在することを知っていたかららしい。男の出自が謎だったが、どうも別の国からやってきた人物らしかった。
ただの痴情のもつれが原因と知り、偽装しただけで、凶器の隠し場所に悩んだ末のガチョウに食べさせるというやり口だった。
そして$ignesから警察により$maryが保護されたという連絡が入った。
""",
"""
殺人事件が解決され、また$maryも無事に戻ってきた。
ただ$blue_stoneが何故一緒にあったのか、その謎だけが$sherlockには引っかかっていた。
後日$maryを助けてくれたという女性と出会う。彼女が$jackだとすぐに分かり、$sherlockは何故戻ってきたのか尋ねる。
どうやら預けていた$blue_stoneが誰かに盗まれたと分かり、取り戻しにきたらしい。どこからどう回ったのか、殺害された$moura夫人の手に渡り、男が盗んだが、凶器と一緒にガチョウに隠してしまったということだった。
$jackは何者かが$stoneを集めようとしていると警告する。四つの$stoneを集めて何をしようとしているのかはよく分からないが、それは今の世の中にとってよくないことだと$jackは考えている。
その目的解明と何かやろうとしていることの阻止を託され、$jackから$blue_stoneを預けられた
""",
        ]

# NOTE: charas
#   ・（ここのみ。ガチョウクラブ会員
#   ・$hornet（ここにみ。ガチョウ卸問屋。容疑者の一人
#   ・$peter（ちょい出演役。ガードマン

# NOTE: stages
#   ・$moura（ここのみ。事件被害者

# NOTE: items
#   ・ナイフ（凶器凶
#   ・$blue_stone（$jackが盗んだものだが、最終的に$jackから$sherlockに預けられる

# NOTE: case
#   ・ガチョウの中からナイフと$blue_stoneが出てくる　→$blue_stoneは$jackが逃げる最中に隠した／ナイフは殺人犯が凶器を慌てて隠した
#   ・$moura夫人殺人事件（凶器が見つからない　→ガチョウの中のナイフで$jack容疑者　→ガチョウクラブの仲間割れで殺された。$jackは無関係

# NOTE: tech
#   ・


def market_and_goose(w: World):
    return w.episode("市場とガチョウ",
            # NOTE
            w.plot_setup("$limeが一緒に暮らすようになり、$maryは自分の役割を取られたような気分になっていた"),
            w.plot_turnpoint("$maryは逃げるように市場に買い出しに行く"),
            w.plot_develop("$sherlockは$wilsonの依頼を終えても失踪事件について調査を続けていた。あまり構ってくれないと憤慨する$maryは市場で仲良くなった肉屋の$nowlisに相談する"),
            w.plot_turnpoint("$nowlisからガチョウをもらう"),
            w.plot_resolve("$maryは自分も役に立つとガチョウを自慢する"),
            w.plot_turnpoint("だが$limeに捌いてもらったガチョウからはナイフと$blue_stoneが出てきた"),
            outline=OUTLINES[0])


def missing_murder_weapon(w: World):
    return w.episode("凶器のない殺人",
            # NOTE
            w.plot_setup("$sherlockはナイフと$blue_stoneについて警察に届けると共に情報を調べる"),
            w.plot_turnpoint("$restradeがやってきてナイフがある事件に関係している可能性があると言った"),
            w.plot_develop("資産家の夫人が謎の死を遂げ、その凶器が見つからなかったが、ガチョウから出てきたナイフに付着していた血液が一致した。$sherlockは知人に$blue_stoneについての鑑定を依頼する"),
            w.plot_turnpoint("$maryが単独で事件捜査していると$limeから聞く"),
            w.plot_resolve("$maryは市場の知人のツテを使ってガチョウの行方を追いかけた"),
            w.plot_turnpoint("$maryは卸先の男からガチョウクラブについて教わる"),
            outline=OUTLINES[1])


def goose_club(w: World):
    return w.episode("ガチョウクラブ",
            # NOTE
            w.plot_setup("$maryはガチョウクラブの情報を仕入れて$sherlockに相談しようとする"),
            w.plot_turnpoint("$sherlockは$jackが国内に入っているという情報を得て、出ていってしまう"),
            w.plot_develop("$maryは$limeと$ignesに頼んでガチョウクラブについて潜入捜査を試みる"),
            w.plot_turnpoint(""),# TODO
            w.plot_resolve("$maryは潜入したガチョウクラブで$dragと$gunの取引が行われているのを目撃してしまう"),
            w.plot_turnpoint("$maryは$dragと$gunの取引現場を目撃してしまう"),
            outline=OUTLINES[2])


def investigate_case(w: World):
    return w.episode("事件捜査",
            # NOTE
            w.plot_setup("$sherlockは$jackが国内に戻っているとの情報を得て、殺人事件について本格的に捜査を開始する"),
            w.plot_turnpoint(""),
            w.plot_develop("殺人現場の住宅を調査し、そこの出入りの業者等も洗う。調べていくうちに殺された$moura夫人がガチョウクラブ会員だったと判明する"),
            w.plot_turnpoint(""),
            w.plot_resolve("売り飛ばされそうになっている$maryの前に、ガチョウクラブで出会った謎の女性（$jack）が現れた"),
            w.plot_turnpoint(""),
            outline=OUTLINES[3])


def case_end(w: World):
    return w.episode("事件解決",
            # NOTE
            w.plot_setup("姿を消した$maryが残してくれたヒントから$sherlockはガチョウクラブの関係に目をつける"),
            w.plot_turnpoint(""),
            w.plot_develop("$sherlockがガチョウクラブに向かうと既にもぬけの殻で、調べるとどうやら$dragなどの取引に使っていたと判明する。警察に連絡する一方、$sherlockは別の犯人がいることに気づいた"),
            w.plot_turnpoint(""),
            w.plot_resolve("$sherlockにより夫人の愛人がガチョウクラブの犯行に見せかけようとした事件だったと判明し、逮捕される"),
            w.plot_turnpoint(""),
            outline=OUTLINES[4])


def four_stones(w: World):
    return w.episode("四つの$stone",
            # NOTE
            w.plot_setup("事件が解決し、ガチョウクラブにも捜査の手が入った"),
            w.plot_turnpoint(""),
            w.plot_develop("$maryは$jackにより助け出され、$sherlockの前に無事返された。$jackは$sherlockに話があると呼び出す"),
            w.plot_turnpoint(""),
            w.plot_resolve("$jackは$sherlockに$blue_stoneを託し、裏世界で動いている何者かの企みを阻止してほしいと依頼した"),
            outline=OUTLINES[5])


# Chapter
def main(w: World):
    return w.chapter(TITLES[4],
            # NOTE
            #   事件：$hornet夫人殺害／ガチョウから凶器（ナイフ）と$stone青が出てくる
            #   被害者：$hornet夫人
            #   容疑者：$jack／配管工や卸問屋の男
            #   犯人：$stoneは$jack／殺害は旦那
            #   依頼人：$mary（市場の知人が容疑者の一人に）／$jack（自分が容疑者になった）
            #   トリック：消失する凶器（ガチョウの中に隠す）→実は偽装で、容疑を$jackにかけるため
            #   結果：痴情のもつれから夫人の間男（ガチョウクラブ主催）が行ったもので、$jackの偽装は闇オークションに出回っていたものを利用
            #   ポイント：$stone青／$jackへの恩（最後の事件後匿ってもらう）
            #   サブ：$maryと$limeの仲が深まる（二人で探索＆調査）
            market_and_goose(w),
            missing_murder_weapon(w),
            goose_club(w),
            investigate_case(w),
            case_end(w),
            four_stones(w),
            outline=ABSTRACT)


