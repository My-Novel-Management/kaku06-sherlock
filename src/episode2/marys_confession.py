# -*- coding: utf-8 -*-
'''
Episode 2-4: "$maryの告白"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$maryの告白"


# NOTE: outlines
ABSTRACT = """
検出結果を受けて$sherlockは再度$royd邸を訪問する。
$jeanは体調悪いからと使用人$kailに断られたが$maryを連れてきて、彼女と直接話があるというと奥から$jeanが出てきて応じてくれた。
$maryはあの場所で父親になんと言われたかを語った。
それは決して遺産相続の話ではなく、自分の出自にかかわることだった。
拾われた子供だ、というのは既に街の人間の噂から察していたが、それだけでなく$animalだと告白された。それも、自分と別の$animalの子供だ、と。実の娘だった。
それは$royd氏がずっと隠していた事実であり、だからこそ$royd氏は遺書で全財産を娘にやると書いていたのだ。
それにショックを受けて家に戻った$mary。一晩中自分の気持を処理できずに寝られなかった。
その告白に対して$jeanはずっとそうじゃないかと疑っていたと。だから余計に愛せなかったと。
そして前日の夜、$roydから直接、話す決意をしたと聞かされた。それは$maryの十六歳の誕生日を迎えるからだった。
$jeanは遺産を$maryにあげたくなくて、$roydを殺して$maryを犯罪者にしたと告白したが、
その時$kailがナイフを振りかざして人質に取った
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            #   NOTE
            w.plot_setup("$sherlockは再度$jeanと$kailに話を聞きに邸宅を訪れる"),
            w.plot_turnpoint("$kailから$jeanが体調を崩していて会えないと断られる"),
            w.plot_develop("$jeanは$maryが拾われ子であり$animalだということを知っていたのを隠していたことを告白する"),
            w.plot_turnpoint("そこに警察が$maryを連れてくる"),
            w.plot_resolve("$kailと$jeanは$maryが父親を憎んでいてそれで殺したと罪をなすりつけようとするが、$sherlockにより証言の齟齬が突かれてボロが出る"),
            w.plot_turnpoint("$maryは$kailたちが父親を殺したことに激怒し、$transformした"),
            w.plot_note("翌日$sherlockは$royd邸を訪れた"),
            w.plot_note("$jeanへの面会を求めたがやはり使用人$kailにより体調が悪いからと断られる"),
            #
            w.plot_note("$sherlockは$keanにバラ園を見せてもらう"),
            w.plot_note("遺体発見現場となった小屋は氏のプライベートルームになっていたようで、頼まれた時以外は$keanも入らないようにしていると"),
            w.plot_note("鍵を開けてもらい、中に入る"),
            w.plot_note(""),# TODO
            outline=ABSTRACT)

