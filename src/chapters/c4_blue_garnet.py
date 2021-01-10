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
一方$blue_stoneは$jackにより盗まれたもので警察は$jackの事件関与も疑っていた。$sherlockは$jackからのメッセージを見つけ、一人出かける。他方、$maryはガチョウクラブに潜入していたが、調査しているのがバレて捕まってしまう

ガチョウクラブの男たちが$drag取引をしている現場を目撃した$maryは、逃げ出そうとして気づかれ、捕まってしまう。
""",
        # $maryがガチョウクラブに捕まる
"""
$limeはいなくなった$maryを探す。$maryはなんとか自力で監禁部屋から脱出しようとするが、そこを謎の女性（$jack）に助け出される。$sherlockは$limeからガチョウクラブのことを聞き、事件の謎を解明した

$sherlockは$limeたちから話を聞き、すぐに事件の犯人がガチョウクラブによるものだと言った。
""",
"""
助け出された$maryは$jackもまた$ajinだと知り、親近感を持つ。$sherlockは事件を解決し$jackの容疑を晴らした。全て解決し$maryと$limeは仲直りする。一方、$sherlockは話があると$jackに呼び出される

$jackは$sherlockに話がある、と呼び出した。
""",
"""

$sherlockは$jackから裏の世界で四つの$stoneを集めようとしている人物の存在を教わる。その目的解明と何かやろうとしていることの阻止を託され、$blue_stoneを預けられた
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
            #   ・$maryと$lime
            w.plot_setup("$limeが同居するようになり、$limeが料理や家事を担当するようになった"),
            w.plot_setup("$maryは自分の居場所が失われたような気持ちになっていた"),
            w.plot_setup("$sherlockは失踪事件について、何か気づき（関連性）を見つけていた"),
            w.plot_setup("どうやらある団体関係者に失踪者が多いと分かる"),
            w.plot_turnpoint("その団体は積極的に投資を行っている$foundationだった"),
            #   ・市場にて
            w.plot_develop("一方$maryは市場に買い出しにきていた"),
            w.plot_develop("顔見知りになり、よくしてくれるようになった肉屋の$nowlis"),
            w.plot_develop("$nowlisから最近妙な噂があるのを聞く。若い女性ばかりが酷い殺され方をして見つかっているという"),
            w.plot_develop("$nowlisは落ち込んでいた$maryに、もらったからとガチョウを譲ってくれる"),
            w.plot_develop("家に戻り、$limeにガチョウをさばいてもらう$mary"),
            w.plot_turnpoint("ガチョウの中から青い宝石と血のついたナイフが一緒に出てきた"),
            outline=OUTLINES[0])


def missing_murder_weapon(w: World):
    return w.episode("凶器のない殺人",
            # NOTE
            #   ・殺人事件
            w.plot_setup("$maryがもらってきたガチョウの中から宝石とナイフが出てきた"),
            w.plot_setup("$sherlockは盗まれた宝石かもと考え、$adelに連絡する"),
            w.plot_setup("ナイフは事件に関係あると考えて$sherlockが警察に連絡を取る"),
            w.plot_turnpoint("$restradeがやってきて、$gunがある事件に関係あると言ってきた"),
            w.plot_develop("$sherlockに事件概要を話して協力を頼んだ"),
            w.plot_develop("事件は高級住宅街に暮らす$moura夫人が廃墟で怪死していた"),
            w.plot_develop("凶器はナイフで、血液と指紋を照合しているが、ほぼガチョウから出てきたナイフで間違いないだろうと"),
            w.plot_turnpoint("$maryにガチョウを渡した$nowlisが容疑者として浮上した"),
            #   ・$maryと少年探偵団
            w.plot_develop("$maryは$nowlisの容疑を晴らすために、一人で調査を開始する"),
            w.plot_develop("市場で聞き込みをする$mary"),
            w.plot_develop("警察に連れて行かれた$nowlisから話を聞いたと$ignesたちに教わる"),
            w.plot_develop("ガチョウの卸売業者に当たる"),
            w.plot_develop("$maryはそこでガチョウクラブの存在を知る"),
            outline=OUTLINES[1])


def goose_club(w: World):
    return w.episode("ガチョウクラブ",
            # NOTE
            #   ・$jackが容疑者
            w.plot_setup("$maryが独自に調査している一方、$sherlockはナイフの事件を調べていた"),
            w.plot_setup("$sherlockは$restradeから連続殺人事件の容疑者を$jackと呼んでいることを知る"),
            w.plot_setup("失踪事件の被害者の中の何人かは猟奇殺人の被害者になっていた"),
            w.plot_turnpoint("ガチョウのナイフから検出された指紋に過去に$jackから取ったものが合致した"),
            w.plot_develop("$jackが連続殺人事件の参考人として手配される"),
            w.plot_develop("$sherlockは彼女が事件に巻き込まれたと判断し、容疑を晴らすために事件を調べ始める"),
            #   ・ガチョウクラブ
            w.plot_develop("$maryは$ignesとともにガチョウクラブに潜入する"),
            w.plot_develop("ガチョウクラブは会員制のガチョウ投資グループで、そこの会員に事件被害者$moura夫人も含まれていた"),
            w.plot_develop("しかしガチョウは名ばかりで、そこで取引されていたのは$dragや改造$gunだった"),
            w.plot_develop("取引現場を見てしまった$maryたち"),
            w.plot_turnpoint("$maryだけが逃げ遅れて、捕まってしまう"),
            outline=OUTLINES[2])


def investigate_case(w: World):
    return w.episode("事件捜査",
            # NOTE
            #   ・$sherlockの動き（$jake関連）
            w.plot_setup("$sherlockは$moura夫人の家を調べにきていた"),
            w.plot_setup("一方$limeは帰ってこない$maryを心配していた"),
            w.plot_turnpoint("$ignesが$maryが捕まったと伝えてきた"),
            w.plot_develop("$sherlockは$moura夫人がガチョウクラブの会員だったことを知る"),
            w.plot_develop("$mouraの殺され方を検死を担当した医者から聞く"),
            w.plot_develop("殺害方法がこれまでと少し違っていることに気づく"),
            w.plot_develop("ガチョウクラブのことも調べに向かう$sherlock"),
            w.plot_turnpoint("市場で$ignesの友人から、$maryが捕まったと伝言される"),
            #   ・$mary救出と事件解決
            w.plot_develop("ガチョウクラブの本部にやってくるが、すでに解散した後"),
            w.plot_develop("$sherlockは以前の銀行強盗のことを思い出して、警察に協力を頼む"),
            w.plot_develop("市場で$nowlisからガチョウの卸業者を聞く"),
            w.plot_turnpoint("$sherlockが卸業者の$hornetが犯人だと、本人を前に尋ねた"),
            outline=OUTLINES[3])


def case_end(w: World):
    return w.episode("事件解決",
            # NOTE
            #   ・$maryと$jack
            w.plot_setup("$maryはガチョウクラブに捕まっていた"),
            w.plot_setup("事件の犯人はガチョウクラブの人間だと考える$mary"),
            w.plot_setup("男たちは$maryが珍しい$ajinだと分かり、売り飛ばそうとしていた"),
            w.plot_turnpoint("そこに突然女警官が入ってきて、行方不明の少女を探していると言う"),
            w.plot_develop("男たちは嘘をつくが、$maryが騒いだことで発覚"),
            w.plot_develop("女警官を殺してしまおうとしたが返り討ちにあう"),
            w.plot_develop("男たちを縛り上げ、警察を呼ぶ"),
            w.plot_turnpoint("彼女は$maryに$sherlockの知り合いだと、説明した"),
            #   ・$jackの説明
            w.plot_develop("$maryは$sherlockがどんな人なのか尋ねた"),
            w.plot_develop("$jackは彼を頭はいいが女心はわからないつまらない男と笑う"),
            w.plot_develop("それでも結果的に助けられ、恩があったので、$maryを助けたと"),
            w.plot_develop("$jackは$maryを$sherlockのもとに送っていく"),
            w.plot_turnpoint("$sherlockは$jackを見て全てを察した"),
            outline=OUTLINES[4])


def four_stones(w: World):
    return w.episode("四つの$stone",
            # NOTE
            #   ・$jackの話
            w.plot_setup("事件は結局$hornertによるガチョウクラブがやったと思わせる偽装だった"),
            w.plot_setup("$jackの仕業に見せかけたもので、鑑定結果から$jackの指紋は検出されなかった"),
            w.plot_setup("ガチョウクラブの方はマルチによる集金と違法$dragの売買ルートになっていた"),
            w.plot_setup("$maryは$jackにより助けられた"),
            w.plot_turnpoint("$jackは$sherlockに話があると言った"),
            w.plot_develop("二人きりで話す$jackと$sherlock"),
            w.plot_develop("しばらく別の国に潜伏していたのに何故戻ってきたのか、理由を伝える$jack"),
            w.plot_develop("裏世界の動向に敏感な$jackは、最近妙な動きがあることに気づいた"),
            w.plot_develop("ガチョウクラブによる$dragの件もそうだった"),
            w.plot_develop("大きなお金が一つのところに集められつつある。そこがどこかはまだ分からない"),
            w.plot_develop("何の目的かも不明だが、どうもよくないことを考えている連中がいると"),
            w.plot_turnpoint("$blue_stoneは$jackが盗み出したものだが、知らない男に奪われそうになり、ガチョウに食べさせたと"),
            #   ・四つの$stone
            w.plot_develop("取り戻す予定がまぎれて見つけられなくなった"),
            w.plot_develop("それで新聞に記事を出していたが、それを見つけたのが$sherlockだった"),
            w.plot_develop("$jackは四つの$stoneの話をする"),
            w.plot_develop("$sherlockも知識は持っていた"),
            w.plot_develop("$stoneはかつて$bossを封じ込めた四人の英雄が持っていた聖なる武具の力の源"),
            w.plot_develop("現在$Arthur、$Percival、$Galahad、$Borsの四つの絶対王家が存在している"),
            w.plot_develop("この国は$Arthurが治めている"),
            w.plot_develop("$jackはその一つを預けるから、謎を解いて、阻止してほしいと依頼する"),
            w.plot_resolve("$jackから$blue_stoneを託された"),
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


