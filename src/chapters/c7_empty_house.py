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
            #   ・それぞれの事情
            w.plot_setup("$sherlockが見つからないまま、$maryたちは彼の生存情報を求めつつ自分たちの新しい生活を送っていた"),
            w.plot_note("$sherlockは$morianoとともに滝壺に落ちたまま、見つからない"),
            w.plot_note("$sherlockがいなくなってから三ヶ月経つ"),
            w.plot_note("世間は治安が悪くなり、犯罪が頻発し、街角に警官が立つようになっていた"),
            w.plot_note("新興宗教$clutX信者が街頭で救世を叫び、ビラを配る"),
            w.plot_turnpoint(""),
            w.plot_develop(""),
            w.plot_turnpoint("$wilsonが$sherlock目撃情報を持ってくる"),
            w.plot_resolve(""),
            # TODO
            w.plot_setup("$sherlockは$morianoとともに滝に落ちて行方不明になった"),
            w.plot_setup("$sherlockを亡くなったと警察は見ている（$patson談）"),
            w.plot_setup("$maryは自分のせいで$sherlockがいなくなったと後悔している"),
            w.plot_setup("少年探偵団などに$sherlockを探してもらっている"),
            w.plot_develop("$maryが家事も買い出しもしなくなり、$limeが一人で担っていた"),
            w.plot_develop("$limeに王室の執事が会いに来て、戻ってほしいと頼む"),
            w.plot_develop("$wilsonは新聞社などを当たって情報を集めていた"),
            w.plot_develop("その中で、記者$milkからホームレスが$sherlockに似た人を見たという目撃情報を仕入れる"),
            w.plot_turnpoint("$wilsonが$sherlock目撃情報を持ってくる"),
            #   ・空き家の冒険
            w.plot_develop("$sherlockらしい人影を見たというホームレスの情報で、スラム街の空き家にやってくる"),
            w.plot_develop("$maryたちは遠くから空き家を監視する"),
            w.plot_turnpoint("$shelrockらしき人影が、空き家に入っていった"),
            outline=OUTLINES[0])


def adventure_of_empty_house(w: World):
    return w.episode("空き家の冒険",
            # NOTE
            #   ・空き家の殺人
            w.plot_setup("$sherlock目撃情報があり、その空き家を見張っていた$maryたち"),
            w.plot_setup("夜になり、そこに明かりがともり、$sherlockに似た人物が入っていった"),
            w.plot_turnpoint("人影は$sherlockに見えたが、そこに男（$ronald）が入っていく"),
            w.plot_develop("監視していると、男二人が争っている姿がシルエット越しに見えた"),
            w.plot_develop("静まり返った中、ずっと監視していた"),
            w.plot_develop("何事も起こらないので$maryたちは注意して空き家に近づく"),
            w.plot_turnpoint("家の中を捜索すると、そこに男の死体があった"),
            #   ・殺人事件
            w.plot_develop("警察に連絡する"),
            w.plot_develop("警察に事情聴取を受ける$maryたち"),
            w.plot_develop("$patsonは状況から$sherlockを容疑者として考えていた"),
            w.plot_turnpoint("$sherlockの容疑を晴らすために$maryは独自で調査し始めた"),
            #   ・家の調査
            w.plot_develop("$maryは一人で家の調査をする"),
            w.plot_develop("抜け穴を見つけて、そこを進むと、先は廃工場だった"),
            w.plot_develop("今までの失踪者が殺されて転がっていた"),
            w.plot_turnpoint("目撃した$maryは誰か（$jake）の手により意識を失った"),
            outline=OUTLINES[1])


def one_mans_confess(w: World):
    return w.episode("ある男の告白",
            # NOTE
            #   ・$jakeの告白
            w.plot_setup("$maryは抜け道から廃工場に捨てられた死体を見つけた"),
            w.plot_setup("そこで$maryは誰かに殴られて気を失った"),
            w.plot_setup("目覚めるとどこかの廃墟の中"),
            w.plot_turnpoint("そこに現れたのは$sherlockによく似た男（$jake）だった"),
            w.plot_develop("$jakeは訳のわからないことを話す"),
            w.plot_develop("連続猟奇殺人は$jakeがやったことだった"),
            w.plot_develop("普通に生きていると自分の内側の何かが衝動を突き動かし、やってしまう"),
            w.plot_develop("自分もまた、闇の住人の血が流れているのだと告白する"),
            w.plot_develop("$maryは$morianoが言っていた「$sherlockの本性に気づいてない」というから勘違いする"),
            w.plot_turnpoint("$jakeは$maryも殺そうとナイフを構える"),
            #   ・$maryを探して
            w.plot_develop("一方、$limeと$wilsonはいなくなった$maryを探していた"),
            w.plot_develop("警察は$maryが$sherlockの逃亡を幇助していると考えていた"),
            w.plot_develop("$limeは$ignesから廃工場の方で見たという話を手に入れる"),
            w.plot_develop("廃工場に向かい、$maryを探す"),
            w.plot_turnpoint("その時、$maryの悲鳴が聞こえた"),
            outline=OUTLINES[2])


def he_is_back(w: World):
    return w.episode("英雄の帰還",
            # NOTE
            #   ・英雄の帰還
            w.plot_setup("$maryを探して廃工場へとやってきた$limeたち"),
            w.plot_setup("そこで$maryの悲鳴を聞く"),
            w.plot_turnpoint("悲鳴の場所にかけつけると、$maryが血まみれの男の前で立っていた"),
            w.plot_develop("$maryは茫然自失で、立ち尽くしていた"),
            w.plot_develop("そこに一人の男が警官を連れて戻ってくる"),
            w.plot_turnpoint("現れたのはホームレスに扮した$sherlockだった"),
            #   ・全ての真相
            w.plot_develop("$maryは一旦病院に運ばれた"),
            w.plot_develop("家に戻った$sherlockは$limeたちに自分がどうやって生き残ったかを話した"),
            w.plot_develop("逃げた$morianoを追いかけて滝に追い詰めた後、$morianoは$sherlockを犠牲にするように崖から飛び降りた"),
            w.plot_develop("$sherlockも死を覚悟したが$maryが繕ってくれた袖が途中でひっかかり、落下の衝撃がゆるくなった"),
            w.plot_develop("それでも大怪我を負った$sherlockだったが、彼を救ったのは$jackだった"),
            w.plot_develop("しばらく彼女の下で休養しながら、各国の情報を集めていた"),
            w.plot_develop("空き家の噂は$sherlockを追う勢力をあぶり出すために彼自身が巻いた嘘だったが、それを利用して殺人を犯したのが$jakeだった"),
            w.plot_develop("$jakeは連続猟奇殺人犯で、失踪事件の大半も彼の仕業だった"),
            w.plot_develop("彼は闇の血が入った混血で、陽の光の下では長く生きられない"),
            w.plot_develop("殺人も失踪も常に夜か明け方だったため、そういう推理を立てていた"),
            w.plot_develop("廃工場で$maryが捕虜になったのを知り、助けるために計画し、すんでのところで鏡を使って光を集めた"),
            w.plot_develop("血まみれだったのは、日光を浴びて肉体が破裂したからだった"),
            w.plot_turnpoint("$sherlockは$maryに預けていた$blue_stoneの場所を聞く。それが必要になったと"),
            outline=OUTLINES[3])


def revive_boss(w: World):
    return w.episode("$bossの復活",
            # NOTE
            #   ・$mary誘拐
            w.plot_setup("$shserlockは儀式を阻止するために戻ってきた"),
            w.plot_setup("儀式に必要な$blue_stoneを預けた$maryは、病院に入院中"),
            w.plot_turnpoint("$maryに$blue_stoneを返してもらいにくると、彼女の姿が消えていた。看護師の話では刑事（$patson）が連れて行ったと"),
            w.plot_develop("改装中の大聖堂に向かう"),
            w.plot_develop("実は半年前の大地震、あれは地震ではなかったと語る"),
            w.plot_develop("大聖堂の修理中になっている部屋の中で、地下に繋がる穴を見つける"),
            w.plot_develop("地下に向かうと、その道は巨大なホールに続いていた"),
            w.plot_develop("地下のホールは酷い有様で、惨殺が行われた後のよう"),
            w.plot_develop("$sherlockはここにかつて$bossの居城があったと語る"),
            w.plot_develop("その跡地に封印目的で建てられたのが大聖堂だったのだ"),
            w.plot_develop("儀式は地震の日に一度行われたが、そこでは必要なものが足りずに失敗した。それが大地震を引き起こした"),
            w.plot_develop("$steinの研究から必要な四つの$stoneを集め、それに加えて$heroの血を探した"),
            w.plot_turnpoint("そこに$maryを人質とした$patsonが現れる"),
            #   ・$boss復活の儀式
            w.plot_develop("$patsonは$sherlockこそがその$heroだと語る"),
            w.plot_develop("$gunにより負傷させる$patson"),
            w.plot_develop("$boss復活の儀式を行う"),
            w.plot_develop("手伝っているのは$cultXの信者たちだった"),
            w.plot_develop("ある人物が$boss復活のために作った宗教だったらしい"),
            w.plot_develop("$morianoが最後に語った「あの方」だ"),
            w.plot_develop("四つの$stoneと血を入れた盃により、儀式が始まる"),
            w.plot_turnpoint("しかし儀式は途中で失敗し、大ホールで爆発が起こる"),
            outline=OUTLINES[4])


def total_the_end(w: World):
    return w.episode("すべての終わり",
            # NOTE
            #   ・偽物の$wilson
            w.plot_setup("$patsonにより$boss復活の儀式が行われた"),
            w.plot_setup("しかしそれは何故か失敗に終わり、爆発が発生する"),
            w.plot_turnpoint("見れば$blue_stoneが割れていた"),
            w.plot_develop("$sherlockは$maryに預けたものが偽物だったと理解する"),
            w.plot_develop("$jackに諮られたのだが、それを知っていて黙っていたのだ"),
            w.plot_turnpoint("$patsonは$wilsonに何故失敗したのかと詰め寄る。彼こそが「あの方」だった"),
            w.plot_develop("$wilsonは$patsonを殺してしまう"),
            w.plot_develop("これで全てが終わったと言うが、$sherlockは許さない"),
            w.plot_develop("$wilsonの嘘を$sherlockが暴いていく"),
            #   ・全ての顛末
            w.plot_develop("そもそも$wilsonの家を一度見たときにそこにあった違和感に気づいた"),
            w.plot_develop("いつも帰っているはずなのに、全然住んでいる雰囲気がない"),
            w.plot_develop("$maryはずぼらだと笑ったけれど、自分の家で置いているものが把握できていなかった"),
            w.plot_develop("それから注意深く調べると$wilsonという男は確かに王室の案件をこなしていたが、今はある件で遠出中だったのだ"),
            w.plot_develop("$wilsonは$zeronと名乗った"),
            w.plot_develop("自分が闇の世界で生まれ、ただ$boss復活をするためだけにこちら側に遣わされた存在だと語る"),
            w.plot_develop("計画は失敗に終わり、嘘も見抜かれた"),
            w.plot_develop("観念したかに見えた$zeron"),
            w.plot_turnpoint("闇の翼をはやした$wilson（$zeron）は隙きを見て開いた穴から外へと逃げてしまった"),
            #   ・最後
            w.plot_turnpoint("山小屋で自殺している$wilsonが発見されたと、報告があった"),
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


