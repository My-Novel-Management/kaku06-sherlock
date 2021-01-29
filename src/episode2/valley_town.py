# -*- coding: utf-8 -*-
'''
Episode 2-1: "谷の田舎町"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "谷の田舎町"


# NOTE: outlines
ABSTRACT = """
$sherlockは$keanから事件のあらましを聞く。おおむね新聞記事の通りだったが、$keanは絶対に娘の$maryが父親を殺すはずはないと断言している。
なけなしの小銭で依頼する$keanに応える$sherlockは、$wilsonとともに事件のあった街に向かう。
電車で向かう最中に、どんな地域なのかを教わる。あまり産業のない土地だったが$royd氏が見つけた$stone鉱脈により潤っていた。それで駅も誕生したと。
街に到着すると、$sherlockたちは事件のあった沼地を訪れる。そこで現場を訪れていた地元の刑事$patsonと遭遇。怪しまれる。
$sehrlockが$restradeの名前を出すとすぐに縮こまり、協力してなんでも教えてくれるという。
どうやらただ証言だけで$maryを犯人と決めている訳ではないと語る。
それについては教えてもらえなかったが、$sherlockは現場で動物の毛を採取した。
$royd邸にやってきた$sherlockは、使用人の$kailと未亡人となった$jeanから話を聞く。
それぞれに互いのアリバイの証言を行う。また娘の$maryが父$roydと事件当日夜、外で出会ったことも目撃証言があった。
二人以外からも外で歩いているのを見たというものもあり、外出し、実際に現場で会ったことは確からしい。
また凶器となった$gunは$maryの部屋から$kailが発見した。
$sherlockは何とかして$maryからも話を聞く必要があると、警察に向かう。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("事件のあった田舎町にやってくる$sherlockと$wilsonは$keanの案内で事件の調査を行う"),
            w.plot_turnpoint("地元新聞社の記者$milkから事件に関する記事や情報をもらう"),
            w.plot_develop("事件現場を確認した後に$royd氏の邸宅で$jean夫人と使用人$kailから話を聞く"),
            w.plot_turnpoint("$maryは警察に勾留され、面会できないと聞く"),
            w.plot_resolve("警察にやってきた$sherlockは$restradeの名前を出して交渉する"),
            w.plot_turnpoint("$restradeのコネで$maryとの面会許可が降りた"),
            w.plot_note("翌朝、中央駅で待ち合わせする$wilson"),
            w.plot_note("$keanは旅馬車を捕まえてここまでやってきたというから、とりあえず$wilsonの家に泊めてやった"),
            w.plot_note("その間に$Boscombeについて話を聞いた"),
            w.plot_note("あまり産業のなかった街で、炭鉱を掘り尽くした後はほそぼそと痩せた土地で作物を育てていた"),
            w.plot_note("湿地帯で谷になっていて、日当たりも悪く、作物にも向かない"),
            w.plot_note("そこで$royd氏が$enagyが取れる不思議な鉱石を見つけ、一躍街の産業になったと"),
            w.plot_note("今では街の人の多くが関連産業で飯を食っているらしい"),
            w.plot_note("また地道な努力で土壌改善も行っている最中だと言っていた"),
            w.plot_note("$royd氏のバラ園を管理していると自慢げに語る$kean"),
            w.plot_note("$sherlockは遅れてやってくる"),
            w.plot_note("どうやら夜更けまで研究していたらしい。目にくまがあった"),
            w.plot_note("では行こうか、と"),
            #
            w.plot_note("$trainを前にして声をあげる$kean。まだ乗ったことがないと"),
            w.plot_note("$wilsonのお金で乗ることになる"),
            w.plot_note("$sherlockは$trainが整備されて大陸の行き来が楽になった反面、今までは交流がなかった場所同士にも接点が生まれるから大変だと語る"),
            w.plot_note("動き出す$train"),
            w.plot_note("蒸気を使っていたがその元となっているのは$scienceだと語る"),
            w.plot_note("$enagyを取り出してそれにより水を蒸発させている"),
            w.plot_note("ヘローンという人物が大昔に技法を見つけ、蒸気で動かす実験をしていると語る"),
            "ヘロンは古代アレクサンドリアの工学者・数学者",
            w.plot_note("車窓から景色を楽しむ$wilsonと$kean"),
            w.plot_note("$sherlockは眠っていた"),
            w.plot_note("どんどん都会から離れて、景色に田園が増えてくる"),
            w.plot_note("$wilsonは持ち出してきた小説を手にして、開いた"),
            #
            w.plot_note("$Herefordまでやってきて更に$Boscombeまで行く"),
            w.plot_note("$sherlockを起こして駅で降りる"),
            w.plot_note("$sherlockはまず$keanに自分を紹介した新聞社に連れて行ってもらう"),
            w.plot_note("馬車しかなく、徒歩で向かうことに文句をいう$sherlock"),
            #
            w.plot_note("地元新聞社"),
            w.plot_note("そこで眼鏡をした$milkが出迎えてくれる"),
            w.plot_note("「噂はかねがね聞いてました」と喜んでいる女性記者$milk。まだまだ三年目の新人"),
            w.plot_note("キャップから「もう終わった事件いつまでもやってるんじゃねえ」とどやされる"),
            w.plot_note("応接室にいき、そこで話を聞く$sherlock"),
            w.plot_note("事件は十日前に起こった"),
            w.plot_note("第一発見者は学校の教師で、そこから警察に連絡がいき、一連の流れは新聞記事にあった通りだった"),
            w.plot_note("$sherlockは次に$keanに案内してもらい$royd邸に向かう"),
            #
            w.plot_note("$royd邸では使用人であり$keanの父である$kailが出迎える"),
            w.plot_note("$jean夫人は体調を崩していて、とても話せる状態ではないと言われた"),
            w.plot_note("$sherlockは$kailの話だけ聞くことにする"),
            w.plot_note("$kailはいつものように朝やってきて、掃除から始めるが、$royd氏の部屋に彼がいないことを妙に思い、夫人などに聞いて回った"),
            w.plot_note("夜出かけたまま戻っていないというので、深酒が過ぎたのかと考えた"),
            w.plot_note("だが昼前になっても戻らず、そこに警察から連絡が入る"),
            w.plot_note("$maryは$jeanの話で前日から部屋にこもったままだと教わる"),
            w.plot_note("$jeanに付き添い、警察まで遺体の確認に向かい、そこで$roydの死亡を確認した"),
            w.plot_note("傷心した$jeanを家に戻し、更に$maryに伝えるべく部屋に向かうと彼女は寝ていて、部屋で$gunを見つけたという"),
            w.plot_note("$kailは$maryがやったものと思い、すぐ警察に連絡をした"),
            w.plot_note("$maryはやっていないと言い張っていたが$gunによる殺人で、そんな珍しいものはこの田舎で誰も持っていないことが判明する"),
            w.plot_note("一連の流れはこうだった"),
            #
            w.plot_note("$sherlockは警察に向かう"),
            w.plot_note("何とか$maryに面会し、話を聞く必要があると"),
            outline=ABSTRACT)

