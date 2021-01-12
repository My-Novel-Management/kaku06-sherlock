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
    return w.episode("魔犬の伝説",
            # NOTE
            #   ・それぞれの近況
            w.plot_setup("$maryと$limeが一緒に暮らすようになり、一月が経過していた"),
            w.plot_setup("寡黙な$limeが$maryとだけはこそこそ話して時折笑うようになっていた"),
            w.plot_setup("$sherlockは$jackに言われたアンダーグラウンドの動きを調べていた"),
            w.plot_setup("かつて存在した$magicの研究者である$stein氏の論文から、亡くなった人を復活させる儀式があったと知る"),
            w.plot_turnpoint("$sherlockはあまりオカルトを信用しないと語る"),
            #   ・魔獣伝説
            w.plot_develop("$sherlockは新聞記事にのったある特集を教える"),
            w.plot_develop("孤島の話。そこでは一人の城主が村の住民を奴隷のようにこきつかっていた"),
            w.plot_develop("気に入った村の娘を城に呼んでは自分の好きなように遊んだ"),
            w.plot_develop("その娘が意を決して城から逃げ出した"),
            w.plot_develop("城主は飼っていた猟犬をけしかけた"),
            w.plot_develop("だが探しにいった城主が見つけたのは惨殺された多くの猟犬と血まみれの少女、そして生き残った知らない真っ黒な巨大な犬"),
            w.plot_develop("城主は呪いにうなされて病死した"),
            w.plot_develop("それはただ酷いことをした城主が病死しただけの話が人の伝聞で都市伝説になっただけだと、$sherlock"),
            w.plot_turnpoint("そこに、その孤島の現在の城主$cherryから招待状がくる"),
            outline=OUTLINES[0])


def first_murder(w: World):
    return w.episode("第一の殺人",
            # NOTE
            #   ・孤島上陸
            w.plot_setup("島からの招待を受けて島に渡る港までやってきた$sherlockたち"),
            w.plot_setup("港で地元の観光課の$mochと合流し、船で島に渡る"),
            w.plot_setup("$mochから魔獣伝説を観光資源にしたいから、そのためのイベントとして各方面の専門家を集めたと説明される"),
            w.plot_turnpoint("島は絶海の孤島だった"),
            w.plot_develop("$sherlockは城に行く前に、伝説の場所となっている雑木林を見せてもらう"),
            w.plot_develop("立て札や囲いがされて、観光地になっていた"),
            w.plot_develop("かつて島民がいたが、今は一人もいなくなったと説明される"),
            w.plot_turnpoint("城に入ると、既に招待客が揃っていた"),
            #   ・招待客
            w.plot_develop("パーティに招待されたのは$sherlock以外に、元刑事、犯罪研究家、心霊学者、地元の歴史研究家が集まっていた"),
            w.plot_develop("城主の$cherryは未亡人で、数年前に城主である夫をうしない、それ以来一人でここに暮らしてきた"),
            w.plot_develop("今回のパーティのために特別に料理や使用人を雇っていた"),
            w.plot_turnpoint("パーティが始まる"),
            w.plot_develop("$sherlockはその間に城内を歩き回り、調査する"),
            w.plot_develop("$maryと$limeは食べるのに懸命で、会場に残された"),
            w.plot_develop("$maryは自称犯罪研究家に、$limeは心霊学者にそれぞれ話しかけられる"),
            w.plot_develop("$wilsonは歴史研究家と地域の情報交換をしていた"),
            w.plot_develop("パーティは何事もなく終わり、明日はイベントが開催予定だった"),
            w.plot_develop("部屋はそれぞれ個室が当てられていたが、部屋割りで$maryが文句を言う"),
            w.plot_develop("それでも$sherlockと$wilson、$maryと$limeになり、それぞれ就寝する"),
            w.plot_turnpoint("明け方、使用人の$bettyの悲鳴が上がり、最初の犠牲者（犯罪研究家）が発見された"),
            outline=OUTLINES[1])


def second_murder(w: World):
    return w.episode("第二の殺人",
            # NOTE
            #   ・事件発生
            w.plot_setup("招待客の中から被害者が出る"),
            w.plot_setup("犯罪研究家が談話室で無残な姿で倒れていた"),
            w.plot_setup("元刑事によって現場は保存され、遺体は空き部屋に収められた"),
            w.plot_turnpoint("現場を見た元刑事がいう。犯人は$sherlockだと"),
            w.plot_develop("$sherlockが談話室で会話した最後の人間だった"),
            w.plot_develop("しかし$sherlockにはアリバイがあった"),
            w.plot_develop("心霊学者は伝説の魔獣が現れたと騒ぐ"),
            w.plot_develop("元刑事は殺害されたと断定する"),
            w.plot_develop("元刑事主導で全員のアリバイを確かめる"),
            #   ・それぞれのアリバイ
            w.plot_develop("元刑事$hugarは$sherlockに協力させ、全員のアリバイを調査する"),
            w.plot_develop("まず亡くなった社会学者$reuiについて、$sherlockが最後に談話室で会話した後、一人で飲んでいた。誰も自室に戻ったのは見ていない"),
            w.plot_develop("心霊研究家$karlは明日のプレゼンに備えて、資料を読み込んでいたと"),
            w.plot_develop("新聞記者$milkは他の記事の下書きを作っていたが、途中で$maryたちの部屋にいって、$sherlockの話を聞いてから寝た"),
            w.plot_develop("$maryと$limeは$milkがきて、三人で楽しく話したと証言"),
            w.plot_develop("$jamosはなかなか寝付けず、シェフに頼んで眠り用のアルコール入りのパン粥を作ってもらって食べた"),
            w.plot_develop("使用人の$bettyは明け方からの準備に備えて早めに就寝。自室に入ったのはシェフの$doldが見ている"),
            w.plot_develop("$hugarは城主の$cherryと少し話してから、ラウンジに残っていた$reuiと酒を飲みながら会話し（$sherlockより前）、自室に入って眠った"),
            w.plot_develop("城主の$cherryは$hugarが出てから、寝室にいき、すぐに寝たと"),
            #   ・失踪者発生
            w.plot_turnpoint("観光課の$mochに聴取しようとしたところで、彼がいないことが判明した"),
            outline=OUTLINES[2])


def trapped_in_castle(w: World):
    return w.episode("城壁の虜囚",
            # NOTE
            #   ・第二の殺人
            w.plot_setup("いなくなった$mochを、手分けして探す"),
            w.plot_setup("外は嵐で海に繋いでいた船は沖に流されてなくなっていた"),
            w.plot_turnpoint("雑木林で$mochが惨殺されているのが発見された"),
            w.plot_develop("一旦城に戻って情報を整理する$sherlock"),
            w.plot_develop("$hugarは犯人探しを勝手に始めた"),
            w.plot_turnpoint("$karlが行方をくらました"),
            #   ・閉じ込められた
            w.plot_develop("失踪者だらけになり、$sherlockは$jamosに頼んで通信機を準備してもらう"),
            w.plot_develop("改めて情報を整理する"),
            w.plot_develop("社会学者の$reuiが死に、失踪した$mochは遺体で発見"),
            w.plot_develop("犯人を探しにいった$hugarは失踪し、心霊学者の$karlは姿を消した"),
            w.plot_develop("城主の$cherryの部屋は鍵がかかったまま"),
            w.plot_develop("外から戻ってきたシェフの$doldは孤島に閉じ込められたと話す"),
            w.plot_turnpoint("$bettyの死体を見つけたと、$hugarが戻ってきた"),
            outline=OUTLINES[3])


def dark_dogs_fang(w: World):
    return w.episode("魔犬の牙",
            # NOTE
            #   ・犯人は心霊学者？
            w.plot_setup("$hugarは心霊学者$karlが怪しいと言い出す"),
            w.plot_setup("$sherlockは全員が固まっていた方がいいと言う"),
            w.plot_setup("城主$cherryの部屋の鍵を壊して中に入る"),
            w.plot_turnpoint("部屋の中が荒らされて、$cherryの服と血液が散乱していた"),
            #   ・地下室
            w.plot_develop("本当に魔獣がいるんじゃないかという話が持ち上がる"),
            w.plot_develop("$cherryもどこかで死んでいるという話に"),
            w.plot_develop("$sherlockは一連の事件が人間の仕業によるものだと言うが"),
            w.plot_develop("$maryが城主の寝室から抜け道があるのを見つけた"),
            w.plot_develop("抜け道はホール脇に繋がっていることが分かり、これを使って誰かが殺したと"),
            w.plot_develop("$doldの姿が見えないことから、今度は彼を疑う$hugar"),
            w.plot_develop("$sherlockは最初の事件の現場を確認する"),
            w.plot_turnpoint("談話室で地下への階段を発見した"),
            #   ・拷問部屋
            w.plot_develop("階段を降りていくとそれは地下の一室に繋がっていた"),
            w.plot_develop("部屋は拷問器具が沢山置かれていた"),
            w.plot_develop("そこに消えた$karlの遺体があった"),
            w.plot_develop("$sherlockはそれを見て事件の謎が解けたというが"),
            w.plot_develop("そこに城主$cherryが現れる"),
            w.plot_develop("$sherlockたちを部屋に閉じ込める$cherry"),
            w.plot_develop("$cherryが真犯人だという$sherlock"),
            w.plot_turnpoint("だが部屋に現れたのは黒い大きな犬だった"),
            outline=OUTLINES[4])


def dark_ritual(w: World):
    return w.episode("暗黒の儀式",
            # NOTE
            #   ・魔犬
            w.plot_setup("地下の拷問部屋に閉じ込められた$sherlockたち"),
            w.plot_setup("黒い大きな犬が部屋に入れられた"),
            w.plot_setup("元刑事の$hugarは$gunを取り出す"),
            w.plot_setup("獣を撃つ"),
            w.plot_turnpoint("獣は部屋の外に逃げ出した"),
            w.plot_develop("$cherryもそれを追って出ていく"),
            w.plot_develop("部屋に閉じ込められた$sherlockたち"),
            w.plot_develop("$maryにより、なんとか扉を壊して部屋から脱出する"),
            w.plot_develop("外にいた$doldと$wilsonは警察に連絡がついたという"),
            w.plot_develop("地元の警察がかけつけるというが、それより前に外に飛び出した$cherryを探しに出る"),
            w.plot_turnpoint("$hugarが殺されていた"),
            #   ・事件の真相
            w.plot_develop("$sherlockは$cherryを説得する"),
            w.plot_develop("$cherryが餌のために人殺しをしていることを見抜いていた"),
            w.plot_develop("魔獣は弱っていて、さっきの傷が致命傷になり、衰弱していく"),
            w.plot_develop("$cherryは自分の体を与えたが、魔獣は生き返らなかった"),
            w.plot_turnpoint("そこに、警察の船が到着した"),
            #   ・後日談
            w.plot_resolve("後日、$cherryの城の地下から、儀式のあとが発見される"),
            w.plot_resolve("$sherlockは$steinの論文を参照し、復活しても維持するために人肉が必要だったと語る"),
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
            second_murder(w),
            trapped_in_castle(w),
            dark_dogs_fang(w),
            dark_ritual(w),
            outline=ABSTRACT)


