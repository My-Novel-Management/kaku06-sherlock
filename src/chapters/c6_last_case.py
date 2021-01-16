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
from episode6 import about_moriano
from episode6 import disturbance_of_mary
from episode6 import his_warning
from episode6 import letter_from_him
from episode6 import researcher_of_ancient
from episode6 import sherlocks_obsession


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
            researcher_of_ancient.main(w),
            about_moriano.main(w),
            his_warning.main(w),
            disturbance_of_mary.main(w),
            sherlocks_obsession.main(w),
            letter_from_him.main(w),
            outline=ABSTRACT)


