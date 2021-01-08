# -*- coding: utf-8 -*-
'''
Chapter "空き家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AbandonedFactory
from scenes import AbandonedHouse
from scenes import Church
from scenes import EmptyHouse
from scenes import Hideout
from scenes import Hospital
from scenes import InCar
from scenes import Market
from scenes import MountCottage
from scenes import PoliceStation
from scenes import SherlockHouse
from scenes import SlumTown
from scenes import WilsonHouse


# Episode
# NOTE
#   .$sherlockを探して＞$sherlockを空き家で見たという情報が入る
#   .空き家の冒険＞空き家の殺人事件の容疑者に$sherlock
#   .$maryの探検＞$maryが捕らえられた
#   .彼が戻ってきた＞$sherlockが戻ってきた
#   .$boss復活＞祭壇は大爆発した
#   .偽$wilsonの思惑＞偽$wilsonは山小屋で自殺しているのが見つかった

# NOTE: outlines
ABSTRACT = """
$sherlockが滝に落ちて行方不明になってから三ヶ月、未だに生存の証拠は見つからなかった。
$maryも$limeもそれぞれアルバイトを探し、$maryは市場で手伝いを、$limeは守衛のアルバイトをしつつ、$sherlockの情報を集めていた。
ある日、$wilsonが$sherlockを見かけたという情報を持ってくる。
$maryたちは$sherlockに似た男が暮らしているというその空き家を監視する。夜になり、後ろ姿が$sherlockに似た男がその空き家に入り、明かりが灯る。本を読む様は確かに$sherlockを思わせたが、そこに来客があり、しばらく後に揉めている様子が伝わり、明かりが消えた。
そこから何も音がしなくなったので、$maryたちが空き家を調べに行くと、そこで知らない男が亡くなっていた。
$sherlockが容疑者として浮上し、警察は$maryたちに事情聴取する。
$maryは$sherlockの容疑を晴らすために空き家を調べる。抜け道を見つけ、それを辿っていくと廃工場に出た。そこで今までに失踪した多くの人の遺体が転がっているのを目撃する。
だが何者かによって意識を失った。
気づいた$maryが見たのは$sherlockで、彼は今までの事件は全て自分がやったと告白する。衝動が押さえられなくなり犯行に及んでしまう、一種の病気だった。
$maryは$sherlockを信じて庇おうとするが、彼は$maryを殺そうとする。
そこをホームレスの男が助ける。彼こそが本物の$sherlockだった。警察がかけつけ、偽物の$sherlockこと連続猟奇殺人事件の犯人$jakeを捕まえる。
負傷した$maryは入院する。
これで全て解決かと思ったが、$sherlockは$limeたちにまだ解決していないと言う。
病院の$maryから$blue_stoneを返してもらう必要があると言い、病院に向かったが、$maryは$patsonにより連れ出された後だった。
改装中の大聖堂の地下、そこでは$patsonが$boss復活の儀式の準備をしていた。
$sherlockは$maryを助け出すためにやってきたが、$patsonは$sherlockの血と交換だと言う。何故ならずっと探していた$heroこそが$sherlockだったからだ。その血が儀式に必要だった。
$sherlockは$maryを助けるために血を盃に注ぐ。それにより四つの$stoneと$heroの血が揃い、儀式が始まる。
だが$blue_stoneが偽物だった為に儀式は失敗し、地下のホールは大爆発した。$jackが渡した$stoneが偽物だったのだ。
そこで$patsonは$wilsonに泣きつくが、$wilsonは$patsonを撃ち殺した。彼こそが本当の黒幕、闇の世界から$boss復活のためにやってきた$zeronだった。
$sherlockはそのことに気づいていて、$wilsonの計画が失敗するように敢えて偽物だと分かって儀式を行わせた。
逃げ出した偽$wilsonは、後日、山中の山小屋で自殺しているのが発見された。$zeronの死により、全ての関連が断たれ、$boss復活にかかわる一連の事件は終焉を迎えた。
"""
OUTLINES = [
"""
$sherlockが消えてから半年、$maryは市場の手伝いをし、$limeは護衛のアルバイトしながら、彼を探し続けていた。しかし未だに何も情報がなく$patsonたちは諦めた方がいいと言っていた。
だがある日、$sherlockの家が強盗に荒らされていて、まだ$sherlockを探している人物がいることが分かる。
$maryたちは安全のために一旦$wilsonの家に移り、地道に$sherlockに関する情報を収集した。
そして遂に$wilsonが$sherlockを見たというホームレスの情報を持ってくる。
""",
"""
ホームレスからスラム街の空き家に$sherlockが出没すると言われ、そこを監視する$maryたち。
夜になると外見や風貌が$sherlockに似た男がその空き家に入り、明かりが灯った。男はいつも$sherlockがしていたように本を読んでいた。
そこに来客がある。二人はしばらく何か言い争った後で、突然明かりが消えた。
しばらく待っても動きがなく、$maryたちは調べるために空き家に突入する。
そこで殺された男の遺体を発見し、警察に通報した。
警察の事情聴取を受けた$maryたち。$maryはそこで$patsonから警察は$sherlockを容疑者として疑っている情報を得る。
$maryは単身で、$sherlockの容疑を晴らすために空き家の調査を行う。
すると、そこで抜け道を発見した。
$maryが抜け道を進むと廃工場に出た。そこで今までに失踪した人間たちの遺体を発見する。だがそこで何者かによって意識を失った。
""",
"""
$maryがいなくなり$limeは$ignesたちに協力をしてもらい、彼女を捜索する。だが警察側は$maryが$sherlockの逃亡幇助をしているのだとして、参考人として探していた。
一方目覚めた$maryの前には$sherlock（に似た男$jake）が現れていた。
$jakeは今までの失踪事件、猟奇殺人の全てが自分の手によるものだと告白する。自分も$maryと同じように闇の者の血を引く$ajinであり、普通に暮らしていると闇の血が騒ぎ、それを抑えるために誘拐、殺人を行う必要があると語る。
$jakeは真相を知った$maryを殺そうとする。
$ignesたちの情報網で、どうやら$maryに似た娘を廃工場街で見かけたという情報が入る。そこに向かう$limeたち。
$maryは$animal化して$jakeに抵抗していたが、どうしても$sherlockを傷つけることができず、追い詰められる。
そこに$maryを助けにあのホームレスの男が入ってくる。そのホームレスの正体こそが、$sherlockだった。
""",
        # $maryの前に殺人鬼$sherlockが現れた
"""
変身して$sherlockたちを追い詰める$jake。しかし$sherlockの機転で工場に穴を開け、日光を浴びせかけることで$jakeは皮膚から大量に出血し、爆発した。
その爆音を聞いて$limeたちが駆けつける。$maryが身を挺して$sherlockを守っていたが、$maryは大怪我を負ってしまった。入院することになる$mary。
戻った$sherlockは、一旦$wilsonの家で$limeたちに事情を語る。
$morianoとの対決により滝壺に落下し、死を覚悟した$sherlockだったが、$maryが繕ってくれた服の裾が引っかかり、何とか死だけは免れた。
ただ大怪我をしており、そこを助けてくれたのが、$jackだった。彼女の別荘で回復するまで休養しながら各国の情報を集め、$moriano配下の動向を追いかけていた。
未だに$sherlockを探す動きが見えたので、おびき出すために空き家の件をでっち上げた。だがそれを利用した$jakeにより$maryがおびき出された、というのが今回の一件だった。
$sherlockは$maryに預けておいた$blue_stoneを取り戻す必要があると言う。
しかし$sherlockたちが病院に駆けつけると、$maryの姿が消えていた。
""",
"""
$sherlockは$maryが$patsonにより連れ出されたと知り、急いで改装中の大聖堂へと向かう。そこが$boss復活の儀式を行う場所だと言う。
大聖堂の地下には巨大なホールが広がっていた。そこはかつて$bossの居城があった場所で、封印する目的で聖堂を建てたのが今の大聖堂の元になったと説明する。
待ち構えていた$patsonは$maryを人質にして、残り一つの「捧げもの」を$sherlockに要求する。それは$heroの血液だった。
$sherlockの家を荒らしたのは$patsonだった。$sherlockが$heroだと知った彼が血液の研究をしていたのを知っての犯行だ。しかし既に$sherlockが処分した後だった。
$patsonも一部に$ajinの血が入っており、苦しい幼少期を経て今があった。$boss復活すれば$ajin優遇の世界がくると信じていた。
だが$sherlockにより過去、$bossがいた時代の$ajinの扱いがどんなに酷いものだったかが語られる。
$gunを打って$sherlockを負傷させ、$maryを人質に、その血を盃に入れさせた。
$patsonにより、$boss復活の儀式が始まった。
""",
"""
$boss復活の儀式が行われ、$stoneに封じられた力が周囲に満ち始める。
だが途中で暴走し、大爆発を引き起こした。$blue_stoneが偽物だったからだ。$jackにより偽物にすりかえられていた。
$patsonの身体は犠牲となり、肉片となって飛び散った。
$sherlockは偽物と知っていて儀式を行わせたのだ。
これで全て終わったかに思えたが、空っぽになった盃を$wilsonが拾い上げる。$wilsonは「また失敗した」と口にする。
意味が理解できない$maryたちだが、$sherlockは予測していた。
$sherlockが全てを行ってきた黒幕が$morianoではなく$wilsonだったと語る。いや、偽物の$wilsonだ。
彼の家を見たときに$wilsonが偽物だと分かった。そこから目的を逆算し、全てを理解した。
$wislonは$zeronと名乗り、正体を現した。
彼は闇の世界から$boss復活のために遣わされた存在だった。
その力は古の魔物のもので、$sherlockたちは太刀打ちできない。$maryが守ろうとしたが負傷していて$transformできない。
追い詰められたかに思えたが、$patsonの使っていた$gunを利用して心臓を打ち抜き、$zeronが利用している体の機能を止めた。
$zeronは闇の力により脱出し、その場から逃げていった
突入した$restradeたちにより助けられ、崩れ去る地下ホールから逃げ出した$sherlockたち。
後日、指名手配で逃走中だった偽$wilson（$zeron）が山小屋で自殺しているのが発見された。
""",
        ]

# NOTE: charas

# NOTE: stages
#   ・大聖堂（中は初出
#   ・イーストエンド（スラム街。少し扱ってきたが本格的はここで
#   ・空き家（事件に使われる場所。ここのみ
#   ・抜け道（EE内に数多くある、地下道の一つ。ここのみ
#   ・廃工場（EE内にいくつもある。ここのみ

# NOTE: items
#   ・$red_stone
#   ・$blue_stone
#   ・$white_stone
#   ・$black_stone
#   ・$bossの杯
#   ・$bossのドクロ（大聖堂の地下に厳重に保管されていたはずのもの

# NOTE: case
#   ・空き家殺人事件　→失踪者の一人の遺体を放置し、$sherlockに容疑が向かうようにした。実行犯は$jake

# NOTE: tech
#   ・

def lookfor_sherlock(w: World):
    return w.episode("$sherlockを探して",
            # NOTE
            w.plot_setup("$sherlockが$morianoとともに滝壺に落ち、行方不明のまま三ヶ月が過ぎていた"),
            w.plot_note("$sherlock失踪から三ヶ月が経っていたが、彼に関する情報は一切入ってこなかった"),
            w.plot_note("$maryは市場で花屋の手伝いをし、$limeは守衛のアルバイトを始めた"),
            w.plot_note("彼が帰ってくると信じて家の掃除をし、空いた時間に街を歩き回り、情報を集めていた"),
            w.plot_note("$ignesたちも情報網を使って調べていたが、何も引っかからないと嘆いていた"),
            w.plot_note("$wilsonは本業の方が忙しいと最近あまり顔を出していない"),
            w.plot_note("$sherlockが消えたことで街では治安が悪くなっていた"),
            w.plot_note("街角に警察が立つようになり、息苦しい社会になっていた"),
            w.plot_note("連続殺人事件はたまに起こるが、頻度は減っていた"),
            w.plot_note("何度か$patsonが訪れ、$sherlockのことを調べたいと家の中を調査していた"),
            w.plot_turnpoint("$wilsonがスラム街の空き家で$sherlockを見かけたというホームレスの情報を掴んだ"),
            w.plot_develop("$maryたちはホームレスの情報をもとに、その空き家を監視する"),
            w.plot_note("$maryと$limeは$wilsonについて、見たというホームレスにまず話を聞く"),
            w.plot_note("スラム街にある空き家の一つで、最近夜になると明かりが灯る家があり、そこに入っていくのを見た。以前に世話になっているから覚えていたと"),
            w.plot_note("$maryたちは近くの空き家にこもり、その空き家を監視する"),
            w.plot_note("$wilsonは一旦用事で離れる"),
            w.plot_note("$maryは$sherlockに謝りたいと$limeに語る"),
            w.plot_note("何も起こらないまま、$wilsonが戻ってくる"),
            w.plot_note("夜に備えて仮眠を取る$mary"),
            w.plot_note("$limeは一旦家に帰り、夜食を作って戻ってくる"),
            w.plot_turnpoint("夜になり、そこに$sherlockによく似た男が入っていく"),
            w.plot_resolve("明かりに映るシルエットは$sherlockに見えた。そこに誰かが入っていき、その人物と争っていて物音とともに明かりが消えた"),
            w.plot_note("空き家に明かりが灯り、部屋に$sherlockらしいシルエットが映る"),
            w.plot_note("いつも彼が着ていた帽子と外套が分かる"),
            w.plot_note("$maryは$sherlockだと言うが"),
            w.plot_note("そこに男（$ronald）が入っていく。一度$sherlockと出会っているところを見かけた紳士だ"),
            w.payoff("一度$sherlockとこっそり会っているのを見た紳士", flagname="$sherlockの知人"),
            w.plot_note("しばらくすると物音がして、明かりが消える"),
            w.plot_note("待ってみたが何も起こらない"),
            w.plot_note("$maryたちは中を調べてみることにする"),
            w.plot_note("暗がりの空き家を探索する$maryたち"),
            w.plot_turnpoint("家の中を調査に訪れると、そこで男の死体を発見した"),
            outline=OUTLINES[0])


def adventure_of_empty_house(w: World):
    return w.episode("空き家の冒険",
            # NOTE
            w.plot_setup("$sherlockが出入りしているという空き家を監視していた$maryたちは、そこで死体を発見した"),
            w.plot_note("空き家の中で遺体を発見する"),
            w.plot_note("その遺体が$sherlockと会っていた$ronaldと分かる"),
            w.plot_note("殺害は一連の猟奇殺人と同じくナイフにより行われていた"),
            w.plot_note("他に誰もいないことを確認する"),
            w.plot_note("$limeが警察を呼び、見回り中だった$patsonが警官を連れてかけつけた"),
            w.plot_note("$maryたちは警察に事情聴取を受けることになる"),
            w.plot_turnpoint("$maryは警察が$sherlockを容疑者として考えていることを知る"),
            w.plot_develop("$maryは$sherlockの容疑を晴らすために空き家を調べていて、廃工場への抜け道を発見する"),
            w.plot_note("警察署で、各自警察から事情聴取を受ける"),
            w.plot_note("$maryは$sherlockがいる情報を掴んで監視していた、と正直に語る"),
            w.plot_note("聴取担当の$patsonは現場が密室状態に近く、ドアを$wilsonが破ったことで出入り口ができたと言う"),
            w.plot_note("見張っていたことで密室になっていた"),
            w.plot_note("$patsonは$maryの証言から、状況からは$sherlockの容疑が硬いと言い出す"),
            w.plot_note("聴取後、$maryは$limeたちを待たずに単独で空き家を調べに向かう。$sherlockの容疑を晴らすため"),
            w.plot_note("空き家は警察が見張りをしていたが、$cultXの信者とホームレスが争いを始めたのを止めに入り、持ち場を離れた"),
            w.plot_note("$maryはその隙きに空き家を調査する"),
            w.plot_note("以前は暗くて分からなかったが、空き家にしては窓もしっかりして、扉にも鍵が掛かるような作りだった"),
            w.plot_note("$patsonから現場は密室に近い状態だったと語られていた"),
            w.plot_note("リビングに当たる部屋はドアが閉め切られ、鍵、あるいは細工により密室に見せかけられていた"),
            w.plot_note("$maryは鍵がないのに衝立棒でドアが開かないようにしてあったキッチンを調べる"),
            w.plot_note("古い絨毯の後と合致しないことが分かり、はがしてみると地下への入り口を見つける"),
            w.plot_note("地下道は昔に掘られた下水用路で、ずっと進んでいくと突き当たりだった"),
            w.plot_turnpoint("$maryは廃工場で今までの失踪者の遺体を発見する"),
            w.plot_resolve("転がっている遺体は切り刻まれ、血が抜かれていたが、$shserlockの記事にまとめてあった失踪者リストの特徴と合致することが分かった"),
            w.plot_note("古い下水用路を進むと、突き当たりで梯子を登る"),
            w.plot_note("暗くてよく分からないが、転がっている部品や規模の大きさから廃工場と分かる"),
            w.plot_note("腐った臭いと、黒い水"),
            w.plot_note("$maryは夜目をきかせて周囲を見る"),
            w.plot_note("沢山の腕を切られた遺体が転がっている"),
            w.plot_note("猟奇殺人と同じような手口だが、こっちはもっと乱雑だった"),
            w.plot_note("その遺体の中に、失踪者リストにあった特徴と合致する人間を何人か見つける"),
            w.plot_note("ここの遺体は失踪者だと分かる"),
            w.plot_turnpoint("$maryの目の前に$sherlock（によく似た男$jake）が出現する"),
            outline=OUTLINES[1])


def one_mans_confess(w: World):
    return w.episode("ある男の告白",
            # NOTE
            w.plot_setup("警察の事情聴取後に、単独行動で姿を消した$mary"),
            w.plot_note("事情聴取後に警察から姿を消した$mary"),
            w.plot_note("$limeと$wilsonは聴取を終えて$mary不在に気づく"),
            w.plot_note("$wilsonは別の用事があると$limeに任せる"),
            w.plot_note("$limeは"),# TODO
            w.plot_turnpoint("$limeは警察が$maryが$sherlockの逃亡に協力しているとして参考人として捜査していることを知る"),
            w.plot_develop("$limeたちは$maryと、空き家で見た$sherlockに似た男を探す"),
            w.plot_turnpoint("$maryの前に現れた$sherlockは、失踪事件、連続猟奇殺人事件それら全てが自分の仕業だと告白する"),
            w.plot_resolve("$maryは$sherlock（$jake）による告白を信じられず、観察しているうちに彼が偽物だと見抜いた"),
            w.plot_turnpoint("偽$sherlockは$maryを殺そうとナイフを取り出した"),
            outline=OUTLINES[2])


def he_is_back(w: World):
    return w.episode("英雄の帰還",
            # NOTE
            w.plot_setup("$maryが失踪して$limeたちは彼女を必死に探す"),
            w.plot_turnpoint("$maryを廃工場で見たという目撃情報が入った"),
            w.plot_develop("目覚めた$maryは$sherlock（$jake）から、失踪事件、連続猟奇殺人事件を全て彼が行ったという告白をされた"),
            w.plot_turnpoint("$maryは$jakeが偽物の$sherlockだと見破った"),
            w.plot_resolve("$transformした$maryは$jakeと戦うが追い詰められる。そこにホームレス（本物の$sherlock）が助けに入る"),
            w.plot_turnpoint("入院していた$maryの姿が消えていた"),
            outline=OUTLINES[3])


def revive_boss(w: World):
    return w.episode("$bossの復活",
            # NOTE
            w.plot_setup("$sherlockが$maryに預けた$blue_stoneを取りに行くと彼女の姿が消えていた"),
            w.plot_turnpoint("改装中の大聖堂内の小部屋で地下への階段を発見する"),
            w.plot_develop("地下の祭壇では$patsonが$maryを人質にして待ち構えていた"),
            w.plot_turnpoint("$sherlockこそが探していた$heroだった"),
            w.plot_resolve("$patsonは$maryを撃って脅し、$sherlockの血を盃に入れさせえた"),
            w.plot_turnpoint("$patsonにより$boss復活の儀式が始まった"),
            outline=OUTLINES[4])


def total_the_end(w: World):
    return w.episode("すべての終わり",
            # NOTE
            w.plot_setup("$patsonの手により$boss復活の儀式が行われる"),
            w.plot_turnpoint("しかし$blue_stoneが壊れ、儀式が失敗する"),
            w.plot_develop("失敗した$patsonを$wilsonが殺して処分する。実は$wilsonは偽物で一連の事件の裏側で動いていた真の黒幕だった"),
            w.plot_turnpoint("$zeronは$sherlockの奇策により負傷し、逃亡した"),
            w.plot_resolve("後日、逃亡していた偽$wilsonこと$zeronが山中の小屋で自殺しているのが発見された"),
            outline=OUTLINES[-1])


# Chapter
def main(w: World):
    return w.chapter(TITLES[7],
            # NOTE
            #   事件：空き家密室殺人／連続失踪事件
            #   被害者：$ronald卿
            #   容疑者：$sherlock
            #   犯人：$jake（$sherlockに似た$ajin）
            #   依頼者：$wilson？
            #   トリック：偽装トリック（争ったように見せかけて遺体を部屋に置いた）＆抜け道を使った密室
            #   結果：$jakeを殺して事件解決
            #   ポイント：連続失踪事件の犯人／$boss復活の儀式とその失敗
            lookfor_sherlock(w),
            adventure_of_empty_house(w),
            one_mans_confess(w),
            he_is_back(w),
            revive_boss(w),
            total_the_end(w),
            outline=ABSTRACT)


