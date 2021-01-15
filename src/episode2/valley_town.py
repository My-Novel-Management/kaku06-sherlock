# -*- coding: utf-8 -*-
'''
Episode 2-1: "谷の田舎町"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


# Scenes
# NOTE

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
    return w.episode("谷の田舎町",
            # NOTE
            w.plot_setup("事件のあった田舎町にやってくる$sherlockと$wilsonは$keanの案内で事件の調査を行う"),
            w.plot_turnpoint("地元新聞社の記者$milkから事件に関する記事や情報をもらう"),
            w.plot_develop("事件現場を確認した後に$royd氏の邸宅で$jean夫人と使用人$kailから話を聞く"),
            w.plot_turnpoint("$maryは警察に勾留され、面会できないと聞く"),
            w.plot_resolve("警察にやってきた$sherlockは$restradeの名前を出して交渉する"),
            w.plot_turnpoint("$restradeのコネで$maryとの面会許可が降りた"),
            outline=ABSTRACT)

