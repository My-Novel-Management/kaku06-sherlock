# -*- coding: utf-8 -*-
'''
Episode 2-5: "本当の気持ち"
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
殺人を計画したのは$kailだった。学校時代から憧れの女性で、ずっと彼女に思いを寄せていた$kailは、彼女の悩みのよき相談相手だった。
彼女が結婚してからも、ここで使用人としていることで彼女の助けになった。
$roydが病気でそう長くないことを知らされ、今回の殺人を思いついた。
$jeanには口裏をあわせてもらっただけで、あとで殺すつもりだったと語る。
だがそれが$jeanをかばっていることは明らかだった。
$kailは剥きになり、$jeanを殺そうとする。
その時$maryが$transformし、$jeanを守った。だが$jeanはそれでも$maryを愛しているとは言えなかった。
こうして事件が終わった。
後日$keanからの手紙で$maryが遺産相続を放棄し、邸宅も地元に寄付することになったと教わる。
$maryは遠くの親戚に預けられるそうだが、$keanは父親と$jeanの戻る場所を守るために邸宅の管理をしつつバラ園を整備するという。
そこに$maryが大きな荷物を持ってやってくる。
$maryは$sherlockの家で暮らすと言った。
"""


# Episode
def main(w: World):
    return w.episode("本当の気持ち",
            # NOTE
            w.plot_setup("$transformした$maryを$kailが$gunで殺そうとする"),
            w.plot_turnpoint("しかし$jeanによりそれが阻止される"),
            w.plot_develop("実行犯は$kailだった。$jeanも加担したが心の底からは賛成していなかった。逃げ出した$kailが逮捕され、事件は解決に向かう"),
            w.plot_turnpoint("$jeanは$maryに対して「愛せなくてごめん」と謝罪した"),
            w.plot_resolve("遺産相続を放棄した$maryは荷物を持って$sherlockの家に押しかけた"),
            outline=ABSTRACT)

