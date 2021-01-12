# -*- coding: utf-8 -*-
'''
Chapter "最後の事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AbandonedHouse
from scenes import InCar
from scenes import InCity
from scenes import Market
from scenes import MorianoHouse
from scenes import SherlockHouse
from scenes import SteinHouse


# Episode
# NOTE
#   .ある殺人事件＞$sherlockが$morianoの名を口に出す
#   .犯罪学者$moriano＞老人は$morianoだった
#   .$maryの不安＞$maryが姿を消した
#   .$maryと$moriano＞$sherlockが救出にやってきた
#   .$maryの不審＞$sherlockは姿を消した
#   .$sherlockの消息＞$sherlockの帽子が見つかった

# NOTE: outlines
ABSTRACT = """
孤島の事件の後で$sherlockは頻繁に王立図書館に出かけて調べ物をしていた。
元大学教授$steinが自宅で謎の死を遂げる。その関係者の一人として$sherlockが浮上し、容疑者として事情聴取される。
$maryは$limeから編み物を習ったりして良好な関係を築いていたが、孤島から戻ってきて以来、少し考え事をしている時間が増えた。
その$maryは市場からの帰り、ふさぎ込んでいる老人を助ける。
一方自分と$stein教授の関係を話して容疑を晴らす$sherlock。その話から$morianoの名前を出し、彼こそが全ての元凶だと語る。そこに$maryが老人を連れて戻ってきたが、その老人こそが$morianoだった。
$morianoは$maryに毒入りの飴を与えたと言い、$sherlockに自分の件から手を引くように脅す。$morianoは$boss復活を考えていて、人間同士による戦争でやがて人間が滅びると予想していた。
$morianoが去った後、$sherlockは彼の言葉が全て嘘で、世界を混乱に陥れたいだけだと語るが、$maryの心には今の$ajin差別がかつてはなかったという言葉が引っかかっていた。
後日、$maryが姿を消す。$sherlockは放っておけというが$limeは探しに歩く。
$morianoの犯罪研究所を訪れると助手の$muranから彼の研究が世界を良くすることに貢献していると知る。また$maryが現在$morianoの研究を手伝っていることも知った。
何とか説得し、戻ってくるようにと伝えたが、$maryは戻ってこなかった。
ずっと$morianoが犯罪に関わった証拠を探していた$sherlockは$steinの家でやっとその痕跡を発見し、$morianoを追い詰める為に彼の研究所に赴く。
だが洗脳された$maryによりその行為は阻止され、$morianoの逃亡を許す。その上、$maryは$sherlockを傷つけてしまったショックから意識を失う。
目覚めた$maryは$limeから$sherlockが$morianoを追いかけて、滝に落ちたことを知る。
後日届いた手紙には、$sherlockから$morianoの犯罪に関する証拠を警察に送ったことと、$maryへの謝罪が書かれていた。
"""
OUTLINES = [
"""
孤島事件後から$sherlockは頻繁に外に出かけるようになっていた。
$maryたちは少し退屈さを感じつつも、自分の今後の身の振り方について考える時間を持つ良い機会だった。
一方、元大学教授が謎の死を遂げた。その容疑者の一人として$sherlockが浮上する。
$maryは市場への買い物の帰り道で、ふさぎ込んでいる老紳士と遭遇し、彼を助ける。
やってきた$patsonは何かの資料を調べるのに必死になっている$sherlockに、$stein元教授殺人事件について事情をきかせろと迫る。
""",
"""
$sherlockはすぐにアリバイを語り、自分の容疑を晴らす。
そもそも$stein教授とは王立図書館で出会った。彼の論文は$sherlockもよく目を通していて、教授から古代の知識について色々と教わっていたと話す。
そして$steinは$morianoの友人だと言い出す。
$morianoについて誰も知らなかった。
$sherlockは$morianoについて語る。この都市の多くの犯罪の糸が$morianoに繋がっていた。$sherlockは珍しく自分の命に代えても$morianoを倒すと言う。
そこに$maryが連れてきた老人こそが$morianoだった
""",
"""
$morianoは$sherlockに対して自分は$steinの死とは無関係だと言う。証拠がないだろうと。
$sherlockは$morianoがどんな犯罪も自分で直接手をくださず、故に現在の司法では立件できず罪に問えないと言う。
だがそこを何とか見つけ出し、必ず罪を償わせると豪語する$sherlock。
その$sherlockに対し、$morianoは$maryに毒入りの飴を与えたことで脅し、これ以上は深入りしないようにと警告した。
その上で、$morianoは$sherlockが人の気持ちより謎解きの方を大切にすると指摘し、$maryたちも捨てられると予言する。$morianoは$sherlockに犯罪をなくすことは不可能だと言い、これ以上自分を追うと余計な犠牲者が出ると脅した。
その翌日、全員が出払っていた間に$sherlockの家は放火されてしまう。全焼こそ免れたが、中も荒らされていて、しばらく使えないという判断から、少しの間$wilson宅で暮らすことにした。
後日、$maryが市場に買い出しに出かけたまま帰ってこなかった。彼女は失踪した。
""",
        # $morianoの甘言にのり、$maryが姿を消した
"""
$maryがいなくなり、$limeはどこにいったのか探さないといけないと主張するが、$sherlockは放っておけばいいと聞かない。
$limeは$ignesたちに協力してもらい、$maryの行方を探す。
一方$sherlockは$steinの家の再調査に訪れていた。$morianoが関与した証拠を探すためだ。しかし痕跡が綺麗に消されている。だが$steinの日記のページの間に一本の毛髪を見つけた。毛髪を証拠にできないかと考える$sherlock。
$limeは$morianoの研究所に入るのを見たという情報を得て、単身研究所に向かう。研究所では助手の$muranだけがいて、$morianoがどんな人物なのか、何をしようとしているのか、その本当の姿を語った。
そこに$maryを連れて$morianoが戻ってくる。彼女は誘拐された訳でも監禁された訳でも何か弱みを握られている訳でもなく、自分の考えでここにいると言った。
$maryは戻らないと$limeに言った。
""",
"""
$maryが$morianoと一緒にいると知り、どうにかしないといけないと$sherlockに言う$limeだったが、$sherlockは何もしない。彼女の考えに任せればいいと言う。
$wilsonたちにも相談したが、$mary自身の考えはどうしようもないとだけ。
$sherlockは何かに夢中になり、頻繁に外出を繰り返し、頼りない状態だった。
そんな$limeに王室の執務官$mikelがやってきて、王室に戻るように言う。王の病気が悪化したというのだ。$limeは$maryを放っておいたままではいけないと悩む。
一方$sherlockは頼んでおいた毛髪鑑定により、人毛で$morianoと同一の血液型ということまで判明した。しかし決定的証拠にはならない。そこを騙ることでボロを出させようと、研究所に向かう。
だがそこで待ち構えていたのは$transformした$maryだった。$morianoは逃げ出したのだ。
$sherlockの説得むなしく、彼女により$sherlockは酷い傷を追う。それで正気に戻り、$maryは気絶した。
""",
"""
$maryが病院で目覚めると$limeから$sherlockが国外逃亡した$morianoを追っていることを聞かされる。
$maryが自分が$sherlockを傷つけてしまったことを後悔していた。
後日、$sherlockから手紙が届く。そこには$morianoを道連れにしてでも滅ぼす決意と、彼の犯罪関与の証拠とそれについて書いた書類が既に警察に発送されていると記されていた。
最後に$maryについての謝罪が書かれていた。
警察の捜査で$sherlockと$morianoが滝から落下したことが判明。現場に残されていた彼の帽子と血液から、二人は死亡したものと見られた。
""",
        ]

# NOTE: charas
#   ・$moriano（名前もここが初出。ほぼここのみ
#   ・$stein教授（事件被害者。$morianoの知人。$boss復活研究家

# NOTE: stages
#   ・$steinの家
#   ・$moriano研究所
#   ・$morianoの別荘
#   ・王立大学

# NOTE: items

# NOTE: case
#   ・$stein元教授殺人事件　→$cultXの支援を受けて研究していたが、危険なことだと分かり、裏切ったために処分（$jakeによる

# NOTE: tech
#   ・


def the_fixer(w: World):
    return w.episode("事件の黒幕",
            # NOTE
            outline=OUTLINES[0])


def about_moriano(w: World):
    return w.episode("$morianoについて",
            # NOTE
            outline=OUTLINES[1])


def his_warning(w: World):
    return w.episode("$morianoの警告",
            # NOTE
            outline=OUTLINES[2])


def lookfor_mary(w: World):
    return w.episode("$maryの捜索",
            # NOTE
            outline=OUTLINES[3])


def rescue_mary(w: World):
    return w.episode("$mary救出劇",
            # NOTE
            outline=OUTLINES[4])


def his_letter(w: World):
    return w.episode("$sherlockからの手紙",
            # NOTE
            outline=OUTLINES[5])


# Chapter
def main(w: World):
    return w.chapter(TITLES[6],
            # NOTE
            #   事件：研究者密室殺害事件／$moriano殺人
            #   被害者：$stein元教授／$moriano
            #   容疑者：$moriano／$sherlock
            #   犯人：$jake／$jake
            #   依頼者：$appolo（$sherlockの恩師）
            #   トリック：改造$gunにより外から遠隔操作で毒薬を打ち込み、死亡
            #   結果：$morianoが死に、姿を消した$sherlockがその重要参考人として手配された
            #   ポイント：$stone黒（$sherlockの手紙と一緒に届く）／目的は$boss復活
            the_fixer(w),
            about_moriano(w),
            his_warning(w),
            lookfor_mary(w),
            rescue_mary(w),
            his_letter(w),
            outline=ABSTRACT)


