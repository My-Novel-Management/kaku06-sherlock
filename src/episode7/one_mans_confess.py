# -*- coding: utf-8 -*-
'''
Episode 7-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "ある男の告白"


# NOTE: outlines
ABSTRACT = """
$maryがいなくなり$limeは$ignesたちに協力をしてもらい、彼女を捜索する。だが警察側は$maryが$sherlockの逃亡幇助をしているのだとして、参考人として探していた。
一方目覚めた$maryの前には$sherlock（に似た男$jake）が現れていた。
$jakeは今までの失踪事件、猟奇殺人の全てが自分の手によるものだと告白する。自分も$maryと同じように闇の者の血を引く$ajinであり、普通に暮らしていると闇の血が騒ぎ、それを抑えるために誘拐、殺人を行う必要があると語る。
$jakeは真相を知った$maryを殺そうとする。
$ignesたちの情報網で、どうやら$maryに似た娘を廃工場街で見かけたという情報が入る。そこに向かう$limeたち。
$maryは$animal化して$jakeに抵抗していたが、どうしても$sherlockを傷つけることができず、追い詰められる。
そこに$maryを助けにあのホームレスの男が入ってくる。そのホームレスの正体こそが、$sherlockだった。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$maryは空き家からの抜け道を進み、それが廃工場に繋がっていることを知る"),
            w.plot_turnpoint("廃工場で沢山の遺体を発見する"),
            w.plot_develop("遺体が行方不明者だと分かったが、手口がどれも猟奇殺人のそれに似ていた"),
            w.plot_turnpoint("そこに$sherlockに似た男が現れる"),
            w.plot_resolve("$sherlock（に似た男$jake）は自分が失踪事件、猟奇殺人事件の犯人であると告白し、幼少期から鬱屈した歪んだ感情を抱えていたことを語る"),
            w.plot_turnpoint("$maryはその男が偽物であることを見抜いた"),
            w.plot_note("$maryの前に現れた$sherlock（$jake）は「見てしまったね」と寂しげに言う"),
            w.plot_note("$maryは$sherlockに対して「これは？」と"),
            w.plot_note("「みんな違ったんだ」と答える"),
            w.plot_note("意味が分からないが怖くなっている$mary"),
            w.plot_note("$sherlockはその遺体を見ながら告白する"),
            w.plot_note("「誰かを殺したい、と思ったことはないか？」と"),
            w.plot_note("それは$morianoにされたものと同じ質問だった"),
            #
            w.plot_note("$wilsonと$limeは家に$maryが戻っていないことに心配になり、探しに出る"),
            w.plot_note("$limeは市場で$ignesたちと出会い、$maryが空き家を調べるといって、そこで消えてしまったことを知る"),
            w.plot_note("$limeは空き家に向かう"),
            #
            w.plot_note("$jakeは語る。自分が何かを殺したという経験は、まだ物心つく前だった"),
            w.plot_note("虫すら恐れて触れない子供だった"),
            w.plot_note("目の前で母親が殺された"),
            w.plot_note("猟奇的な殺人鬼は母親の腸をひきずりだし、中身が見えていた"),
            w.plot_note("そのトラウマから、$jakeは人の中身を見てみたいという衝動にかられるようになる"),
            w.plot_note("医者という職業があることを知った"),
            w.plot_note("カエルなどの小さな生き物を解剖して遊んだ"),
            w.plot_note("学校ではいつも動物の飼育係だった"),
            w.plot_note("どこをどうすれば壊れるのか、勉強し、実戦した"),
            w.plot_note("成績は優秀だった"),
            w.plot_note("ただ他人との関わり方は知らないまま育った"),
            w.plot_note("大学に入り、生物学、解剖学を学ぶ"),
            w.plot_note("医学にも精通し、将来は医者になるべきだと言われた"),
            w.plot_note("しかし大学で失敗した"),
            w.plot_note("偶然だったが、当時付き合っていた彼女を殺してしまったのだ"),
            w.plot_note("その感覚が忘れられずに、何度か人を殺してみた"),
            w.plot_note("同じ感覚は得られなかった"),
            w.plot_note("一度警察に捕まった"),
            w.plot_note("それからは捕まらないようにどうすればいいか考えた"),
            w.plot_note("やがて、人は突然いなくなるものだと気づいた"),
            w.plot_note("毎日失踪者がいる。誰かは探すが、探されない誰かも多い"),
            w.plot_note("そうやって失踪者を作り、頃合いを見て実験した"),
            w.plot_note("普段は何食わぬ顔で生活している"),
            w.plot_note("誰もが正常の皮をかぶっているという"),
            w.plot_note("自分が$ajinであることなど、都会では忘れてしまう"),
            w.plot_note("でもふとした瞬間に、自分の内側に湧き上がる衝動がある。人を殺してみたい。あのときの感覚を取り戻したい"),
            w.plot_note("連続猟奇殺人を行った$jackは自分だ、と告白する"),
            w.plot_note("その手には独特の形のナイフがある"),
            w.plot_note("ククリナイフと呼ばれるもので、少数部族が持っている狩猟・農耕用のもの"),
            w.plot_note("それで殺されていた"),
            w.plot_note("$jakeは「$morianoに出会った」ことが人生を変えた、という"),
            w.plot_note("$morianoに出会い、殺しが目的になったと"),
            w.plot_note("$maryは語っている$sherlockに似た男が、違うんではないかと気づき始める"),
            w.plot_note("「あなたは、だれ？」"),
            w.plot_note("臭いがずっと気になっていた。$sherlockの臭いがしない"),
            w.plot_note("もっと獰猛な獣の臭い。あの孤島の城でかいだ匂いに近い"),
            w.plot_note("$jakeは語る。自分は「$jake」とかつて呼ばれていたと"),
            w.plot_note("今は名前すらない、ただの殺人鬼$jackだと"),
            w.plot_note("$maryに襲いかかる$jake"),
            w.plot_note("$maryは$transformして応戦する"),
            w.plot_note("しかしあっという間に追い詰められる"),
            w.plot_note("なんとか部屋から抜け出す"),
            w.plot_note("廃工場地帯で、どこも似たようなものばかり"),
            w.plot_note("$jakeも$transformして、追ってくる"),
            w.plot_note("翼が生えた獣だった"),
            w.plot_note("しかし何かを嫌がっている風"),
            w.plot_note("$maryは追い詰められ、部屋にこもる"),
            w.plot_note("外からドアがしめられ、逃げられなくなる"),
            w.plot_note("天井から$jakeが入ってきて、ついに追い詰められる"),
            w.plot_note("もう駄目だ、と思った時だった"),
            w.plot_note("窓から強烈な光が入る"),
            w.plot_note("そのすきにドアが破られ、シルエットの手が伸びてきて、助け出す"),
            w.plot_note("続いて爆発音"),
            w.plot_note("太陽の光が弱点だった"),
            w.plot_note("$jakeは飛び散る"),
            w.plot_note("助けてくれた男をよく見る$mary"),
            w.plot_note("薄れゆく意識の中で見たのは、$sherlockだった"),
            outline=ABSTRACT)

