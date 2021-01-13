# -*- coding: utf-8 -*-
'''
Chapter "魔獣"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import Bar
from scenes import BasementInCastle
from scenes import BedroomInCastle
from scenes import Church
from scenes import InShip
from scenes import InTrain
from scenes import Island
from scenes import Library
from scenes import LoungeInCastle
from scenes import OldCastle
from scenes import Port
from scenes import SherlockHouse
from scenes import Station
from scenes import Street


# Episodes
# NOTE
#   .魔獣伝説＞パーティの招待状が届く
#   .第一の殺人＞事件解決専門家が死体で発見される
#   .第二の殺人＞$mochが失踪した
#   .地下室＞地下室を発見した
#   .魔犬＞$cherryが魔犬に殺された
#   .儀式＞復活の儀式があることを知る

# NOTE: outlines
ABSTRACT = """
ある島には$bossがいた時代には沢山存在していた魔獣が今も棲んでいて人を喰らっているという。
その島にある城の城主から$sherlockの許にパーティの招待状が届く。旅行気分で$sherlockに同行する$maryたちだったが、島へのガイドを担当した地元の観光課勤務の$mochから実際に魔獣によるものと見られる連続殺人が起こっていると脅される。
城には$sherlock以外にも元刑事や新聞記者、社会学者、心霊学者、地元の歴史研究家なども呼ばれていた。更にパーティ用に料理人や使用人も雇われていた。$mochの説明では島からほとんどの住民が避難してしまった惨状をどうにかしようと、魔獣伝説にまつわるイベントを開催して、何とか観光資源にできないかという話だった。
だがその夜、社会学者の$reuiが惨殺死体で発見される。
元刑事の$hugarは独自の推理を展開し、$sherlockたちや心霊学者の$karlや地元の学者$jamosを疑う。
しかし次の日に姿を消したのは地元観光課の$mochだった。
$mochが犯人として探したが、彼は最初に魔獣伝説の発端となった殺人事件があった雑木林で無残な姿で発見された。
船は流され、海は大時化で、警察に連絡を取ることもできず、$sherlockたちは孤立する。
一方、城主の$cherryは部屋に閉じこもり、出てこなくなった。妙に思った$hugarが強引にドアを破って中に入ると、彼女の姿も消えていた。
心霊学者の$karlも失踪し、多くの人間が既に被害に遭っているのではないかという話になる。
$sherlockは$cherryの寝室に抜け道を発見し、更に談話室で地下への階段を見つける。
地下には昔の拷問部屋があったが、そこに現れたのは城主$cherryと巨大な黒い犬だった。
部屋に犬とともに閉じ込められた$sherlcok。しかし$transformした$maryにより傷つけられた黒犬は部屋を抜け出し、逃げ出した。
$cherryも後を追って姿を消したが、ようやく駆けつけた警察とともに捜索した結果、黒犬に食われて亡くなっているところが発見され、黒犬は警察により射殺された。
事件後、地下の別の部屋から、復活の儀式を行った跡が発見された。黒犬は闇の技法により蘇った闇の生き物だったのだ。$cherryはそれを維持するために人を殺してその肉を与えたいたのだと分かった。
"""
OUTLINES = [
"""
$maryや$limeが同居して一月、賑やかな生活にも慣れてきた頃に、巷で連続猟奇殺人事件が発生していた。それらが人間ではないモノの仕業と有名になっていた。
$sherlockはこんな事例を紹介する。
ある孤島には魔獣の伝説があった。城の城主が住民を奴隷のように扱い、好きな娘を城に呼んでは自分の思い通りにして遊んだ。その城主は猟犬を飼っていて、気に入らない奴隷を追いかけさせては殺して楽しんでいたらしい。まだ$bossが生きていた頃の時代だ。
ある時、城に呼ばれた娘は自力で逃げ出した。その娘を猟犬に追わせ、自分も馬で探しに出た城主だったが、後に住民によって発見されたのは自分の猟犬により食い殺された城主と、血まみれになって笑っている少女だった。
事実は圧政に耐えかねた村人による城主の撲殺だったとされているが、未だに人々はその伝説が本物だと信じているという。
$sherlockはそういったオカルトを信じないと切って捨てた。
その城からパーティの招待状が届いた。
""",
"""
船で島に渡る$sherlockたち。ガイド役として観光課職員の$mochが同行した。今回のイベントが観光目的だからだそうだ。
島では伝説の殺人があった雑木林に記念碑を建てていたが、その後も猟奇的な殺人事件が何度か起こり、かつて暮らしていた島民は全員外に逃げ出していた。
城では現在の城主$cherryが迎えてくれる。
既にパーティ参加者は集まっていて、それぞれ元刑事$hugar、社会学者$reui、心霊学者$karl、地元の歴史学者$jamos、新聞記者の$milkと癖のある人間が揃っていた。
他にパーティ用に臨時で雇った料理人$doldと使用人$bettyがいた。
イベントは明日行われるからと、前日はささやかな立食パーティが開かれた。
各自部屋があてがわれたが$sherlockたちは人数が多かったため、二人でひと部屋となった。
$maryと$limeはパーティ会場で食べながらそれぞれの参加者の話を苦笑しつつ聞いた。
一方$sherlockは城を興味深く歩いて見て回っていた。
しかし翌早朝、社会学者の$reuiが無残な姿で殺されているのが発見された。
""",
"""
元刑事$hugarが現場を保存し、警察を呼ぼうとする。だが外は大荒れで更に船が何者かに壊されていた。連絡手段がなく、警察が呼べないとなり、$hugarは自分が現場責任を取ると言い出す。
$sherlockを手下として使い、それぞれのアリバイを聞き出す。
$maryと$lime、$wilsonはそれぞれ$hugarに事情聴取された。彼の聴取は前時代的なもので、最初から「やったこと」にして聴取された。$maryは泣き出すし、$limeはしゃべれなくなる。$wilsonだけがひょうひょうと答えていた。
一方$sherlockは$reui、$karl、$doldらを担当する。それぞれパーティ後からのアリバイを調べた。
双方の情報を集め、$hugarはずっと部屋にこもっていた$karlが怪しいと言い出し、彼の部屋を調べる。$karlの部屋には古文書があり、そこには色々な闇の技法に関する記述があった。中には人を呪い殺す方法などもあり、$hugarは呪い殺したのではないかと疑う。
$sherlockは現場を調べ、人ではないものが殺したように見せかけたのではないかと推理する。ただそこに獣の毛を発見した。
城主の$cherryは体調を崩して部屋にこもってしまい、イベントも開催できず、そんな中、$mochが姿を消した。
""",
        # 第二の殺人事件が発生した
"""
$hugarは$mochを怪しみ、探そうとする。だが$sherlockはまず全員の安全を確保すべきと意見が割れ、$hugarから反感を持たれる。
$hugarに従おうとする$jamosや$doldたちと、反発する$sherlock。心霊学者の$karlは全てが魔獣の仕業だと騒いでいた。
$hugarは城の外を捜索すると出ていく。中に残った$sherlockは$cherryに城内調査の許可を貰おうとしたが、彼女は体調を崩したようで、すぐに自室に引っ込んでしまった。
城内を調べていると、かなり古い道具がいくつも見つかった。また改修されているのも分かった。
$hugarたちが戻ってきて$mochの死体を雑木林で発見したと言う。更に$karlの姿が消えていた。
手分けして探すが見つからない。
心配していた$cherryの寝室に入ったが、彼女の姿も消えていた。
""",
"""
$sherlockは$jamosに通信機が使えるようにならないか試してもらう。
$hugarは消えた$carlをずっと怪しんでいて単独で捜査してどこかに行ってしまう。
$maryはずっと姿を見ていない$cherryが気になっていたが、部屋には鍵がかかったままだった。
$sherlockは再度、城内を調査する。人の手によるものだとし、最初の談話室の事件が可能だった人物を挙げていく。
そこに$hugarがお手伝いの$bettyも殺されているのを見つけたとやってくる。$hugarと$sherlockは互いを疑い合う。
その時、$limeが談話室で抜け道を見つけた。
地下通路を進むと、その先には拷問器具が置かれた部屋があり、$karlの死体が転がっていた。
更にそこには大きな黒い犬が待ち構えていた。
""",
"""
伝説の魔犬が存在していたのだと騒ぐ$jamos。だが魔犬は襲いかかってくることはなく、$maryにじゃれつく。
それを外から見ていたのは城主の$cherryで、彼女は魔犬が$sherlockたちを食わないことに腹をたて、睡眠ガスを部屋に送り込もうとするが、$sherlockの機転により阻止される。
全ての事件が$cherryの手により行われたものだと言った$sherlockに対し、$cherryは皆殺しにしようと襲いかかってくるが、$maryと$limeにによって阻止される。
逃げ出した魔犬を追って$cherryも部屋から出た。
部屋に閉じ込められた$sherlockたちは何とか部屋から脱出し、$cherryを探す。
途中でやっと上陸できた警察と合流した。
$cherryは雑木林で魔犬に食われて亡くなっていて、魔犬は警察により射殺された。
$sherlockは$cherryが魔犬の餌にするために人殺しを行っていたのだと語る。
後日、地下の別の部屋から闇の技法を用いて愛犬を復活させたと考えられる儀式の形跡が見つかった。そしてその資金の為に所有していた$black_stoneが闇マーケットに売られていたことが判明した。
""",
        ]

# NOTE: charas
#   ・$cherry（ここのみ。城主。真犯人
#   ・$moch（ここにみ。観光協会の人間。共犯者

# NOTE: stages
#   ・地方（ダートムーア。ここのみ。原作とは異なり、南西部の海に浮かぶ孤島に設定
#   ・$baskervilles家（ここのみ？

# NOTE: items
#   ・$black_stone（話だけ。$baskervilles家の所有物だったが闇オークションに出されて行方不明　→？

# NOTE: case
#   ・魔犬伝説の猟奇殺人　→当時の魔術の失敗による自殺
#   ・孤島事件第一の殺人（犯罪研究家）　→$moch。最初から観光を盛り上げるための事件と割り切り計画していた
#   ・孤島事件第二の殺人（観光課の$moch）　→$cherry。仲間割れと口封じ（当初から殺す計画
#   ・孤島事件第三の殺人（霊能者）　→$cherry。犯行現場を見られた

# NOTE: tech
#   ・通信技術（モールス信号？）


def legend_of_dark_dog(w: World):
    return w.episode("魔獣の伝説",
            # NOTE
            w.plot_setup("ある孤島で猟奇的殺人事件が発生したが、それは魔獣によるものだという伝説があった"),
            w.plot_develop("$sherlockはオカルトを信じない。$maryたちのようにこういった都市伝説には興味はないと自分の研究に必死だった"),
            w.plot_resolve("孤島の城の主からパーティの招待状が届いたが、$sherlockは用事で行けないというので$maryたちが行くことになった"),
            outline=OUTLINES[0])


def first_murder(w: World):
    return w.episode("第一の殺人",
            # NOTE
            w.plot_setup("パーティに参加する為に島にやってきた$maryと$lime、$wilsonだったが城に集められていたのは曲者の面々だった"),
            w.plot_develop("イベントでは島に伝わる魔獣伝説が地元の歴史研究家$jamosにより語られ、それについて元刑事$hugarなどが持論を展開する"),
            w.plot_resolve("しかし翌朝、社会学者$reuiが遺体となって発見された"),
            outline=OUTLINES[1])


def missing_person(w: World):
    return w.episode("失踪者",
            # NOTE
            w.plot_setup("殺人事件が発生したが外は荒れていて船も何者かに壊され、孤島に閉じ込められることになった"),
            w.plot_develop("心霊研究家$karlは魔獣の仕業だと騒ぎ出すが、元刑事$hugarはそれを無視して主導権を握り、$maryたちに手伝わせて全員の事情聴取を行う"),
            w.plot_resolve("頼りにしていた観光課の$mochが失踪してしまった"),
            outline=OUTLINES[2])


def second_murder(w: World):
    return w.episode("第二の殺人",
            # NOTE
            w.plot_setup("元刑事の$hugarは$mochを容疑者とみて全員に捜索させる"),
            w.plot_develop("失踪した$mochが雑木林で発見され、その間に$reui遺体の第一発見者の使用人$bettyが失踪し、城主の$cherryは自室に籠もったまま出てこない。現場は混乱してしまう"),
            w.plot_resolve("$sherlockから島に向かっていると連絡が入った"),
            outline=OUTLINES[3])


def dark_dogs_fang(w: World):
    return w.episode("魔獣の牙",
            # NOTE
            w.plot_setup("失踪者が多く出て城主の$cherryの姿もなくなり困り果てたところに$sherlockが現れる"),
            w.plot_develop("$sherlockは最初の事件が起こった談話室から、改めて調査を行う。$hugarには文句をつけられつつも、事件が人為的に行われた情報を集めていく"),
            w.plot_resolve("地下には拷問部屋があり、そこでは黒い巨大な犬が待ち構えていた"),
            outline=OUTLINES[4])


def sorrow_end(w: World):
    return w.episode("悲しみの結末",
            # NOTE
            w.plot_setup("本当に魔獣の仕業だったと騒ぎ立てるが$sherlockは殺人が犬の仕業ではないことを伝えて、隠れていた$cherryを呼び出した"),
            w.plot_develop("$cherryは自分の罪を告白しながらも部屋に毒ガスをまこうとするが、犬が共倒れになりそうになって中止し、犬とともに逃亡する"),
            w.plot_resolve("事件は$cherryの死により結末を迎えた。後日城の地下で儀式の跡が見つかった"),
            outline=OUTLINES[5])


# Chapter
def main(w: World):
    return w.chapter(TITLES[5],
            # NOTE
            #   事件：犬による猟奇殺人／孤島の招待客連続殺人
            #   被害者：数名の地域の人／
            #   容疑者：伝説の魔犬
            #   犯人：$cherry（犬の餌として必要だった）
            #   依頼人：城主の$cherry
            #   トリック：偽装（歯型の凶器を使い、犬がやったように見せかけた
            #   結果：二人が死亡（うち一人は共犯）、城主の$cherryは飼い犬に食い殺され、魔犬は射殺
            #   ポイント：蘇りの$sorcery／$stone黒の行方情報（闇オークションに出回った）
            legend_of_dark_dog(w),
            first_murder(w),
            missing_person(w),
            second_murder(w),
            dark_dogs_fang(w),
            sorrow_end(w),
            outline=ABSTRACT)


