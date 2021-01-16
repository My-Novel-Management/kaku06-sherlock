# -*- coding: utf-8 -*-
'''
Episode 6-3
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$maryの乱心"


# NOTE: outlines
ABSTRACT = """
$maryがいなくなり、$limeはどこにいったのか探さないといけないと主張するが、$sherlockは放っておけばいいと聞かない。
$limeは$ignesたちに協力してもらい、$maryの行方を探す。
一方$sherlockは$steinの家の再調査に訪れていた。$morianoが関与した証拠を探すためだ。しかし痕跡が綺麗に消されている。だが$steinの日記のページの間に一本の毛髪を見つけた。毛髪を証拠にできないかと考える$sherlock。
$limeは$morianoの研究所に入るのを見たという情報を得て、単身研究所に向かう。研究所では助手の$muranだけがいて、$morianoがどんな人物なのか、何をしようとしているのか、その本当の姿を語った。
そこに$maryを連れて$morianoが戻ってくる。彼女は誘拐された訳でも監禁された訳でも何か弱みを握られている訳でもなく、自分の考えでここにいると言った。
$maryは戻らないと$limeに言った。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("いなくなった$maryを$limeは探そうとするが$sherlockは放っておけばいいと言って取り合わない"),
            w.plot_turnpoint("$limeはしばらく別のところで暮らすと出ていく"),
            w.plot_develop("$limeは市場の人間や今までの知人、また王室関係の力を使って$maryを探す。すると$maryが$moriano犯罪研究所に入るのを見たという情報が入った"),
            w.plot_turnpoint("$moriano犯罪研究所で$maryと出会う"),
            w.plot_resolve("$limeは$maryに戻ってくるよう説得を試みたが$maryの決意は固く、$morianoの手伝いをすると言って、帰された"),
            w.plot_turnpoint("$sherlockの火の不始末により自宅が燃えてしまう"),
            outline=ABSTRACT)

