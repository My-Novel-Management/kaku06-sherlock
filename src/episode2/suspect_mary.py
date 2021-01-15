# -*- coding: utf-8 -*-
'''
Episode 2-2: "容疑者$mary"
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
警察にやってきた$sherlockたち。$patsonは$maryとは会わせられないという。
$sherlockは$restradeのツテを利用してなんとか僅かばかりの面会の時間を得る。
面会した$maryは衰弱していたが、$sherlockが$keanの依頼できたことを知ると、全て話すと言った。
$maryは自分が父親に話があるからと呼び出されて事件現場に行った。どうしても家の中で話せないことがあるからと。
そこで自分が拾われた子供だったと告白された。それにショックを受け、そのままその場を立ち去った。途中バラ園で休んでから家に戻った。そのまま部屋から一歩も出ず、翌朝、$kailに起こされて父親が亡くなったことを聞かされた、と。
その時にはまだ誰が殺したか分からず、ただしんだことだけ教わった。
その後、警察が来たり、それぞれ事情聴取された。何故か自分の部屋から凶器の$gunが発見され、容疑者になってしまった。
自分は絶対にやらないし、拾われ子だったことはショックだったが、父親には恩義しか感じていないと。
面会後、$sherlockは全てを語っていないと言う。
$maryは$animalだった。またそれが警察の容疑者候補として強い印象になっていると。
"""


# Episode
def main(w: World):
    return w.episode("容疑者$mary",
            # NOTE
            w.plot_setup("警察にやってきた$sherlockはそこで容疑者の$maryと面会をする"),
            w.plot_turnpoint("$maryは沈黙を守っていたが$keanの名前に安心して話し始めた"),
            w.plot_develop("$maryから事件前後の話を聞く。彼女は父親に呼び出されてある話をされたと語った"),
            w.plot_turnpoint("$maryは家に帰った時に使用人の$kailと顔をあわせたと言った"),
            w.plot_resolve("地元刑事の$patsonは警察は確かな証拠を掴んでいるからこのまま証拠と証言を固めて裁判所に送ると言う"),
            w.plot_turnpoint("$sherlockは$maryが$animalであると言った"),
            outline=ABSTRACT)

