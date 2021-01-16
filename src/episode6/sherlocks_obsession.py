# -*- coding: utf-8 -*-
'''
Episode 6-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$sherlockの執念"


# NOTE: outlines
ABSTRACT = """
$maryが$morianoと一緒にいると知り、どうにかしないといけないと$sherlockに言う$limeだったが、$sherlockは何もしない。彼女の考えに任せればいいと言う。
$wilsonたちにも相談したが、$mary自身の考えはどうしようもないとだけ。
$sherlockは何かに夢中になり、頻繁に外出を繰り返し、頼りない状態だった。
そんな$limeに王室の執務官$mikelがやってきて、王室に戻るように言う。王の病気が悪化したというのだ。$limeは$maryを放っておいたままではいけないと悩む。
一方$sherlockは頼んでおいた毛髪鑑定により、人毛で$morianoと同一の血液型ということまで判明した。しかし決定的証拠にはならない。そこを騙ることでボロを出させようと、研究所に向かう。
だがそこで待ち構えていたのは$transformした$maryだった。$morianoは逃げ出したのだ。
$sherlockの説得むなしく、彼女により$sherlockは酷い傷を追う。それで正気に戻り、$maryは気絶した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("家が燃えた$sherlockは$wilsonの家で世話になることにした"),
            w.plot_turnpoint("戻ってきた$limeから$maryが$morianoの助手になったと聞いた"),
            w.plot_develop("$sherlockは$morianoが危険だと語り、今まで以上に彼の証拠集めに必死になる。一方$limeは王室に戻るかどうかの決断を迫られていた"),
            w.plot_turnpoint("$sherlockは$morianoを追い詰める証拠を見つける"),
            w.plot_resolve("$moriano研究所を訪れる$sherlock。そこで彼を追い詰めようと手を打つが、$maryによって阻止される"),
            w.plot_turnpoint("$transformした$maryにより$sherlockは負傷し、$morianoを取り逃がしてしまう"),
            outline=ABSTRACT)

