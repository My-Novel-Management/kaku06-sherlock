# -*- coding: utf-8 -*-
'''
Episode 5-2
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "失踪者"


# NOTE: outlines
ABSTRACT = """
元刑事$hugarが現場を保存し、警察を呼ぼうとする。だが外は大荒れで更に船が何者かに壊されていた。連絡手段がなく、警察が呼べないとなり、$hugarは自分が現場責任を取ると言い出す。
$sherlockを手下として使い、それぞれのアリバイを聞き出す。
$maryと$lime、$wilsonはそれぞれ$hugarに事情聴取された。彼の聴取は前時代的なもので、最初から「やったこと」にして聴取された。$maryは泣き出すし、$limeはしゃべれなくなる。$wilsonだけがひょうひょうと答えていた。
一方$sherlockは$reui、$karl、$doldらを担当する。それぞれパーティ後からのアリバイを調べた。
双方の情報を集め、$hugarはずっと部屋にこもっていた$karlが怪しいと言い出し、彼の部屋を調べる。$karlの部屋には古文書があり、そこには色々な闇の技法に関する記述があった。中には人を呪い殺す方法などもあり、$hugarは呪い殺したのではないかと疑う。
$sherlockは現場を調べ、人ではないものが殺したように見せかけたのではないかと推理する。ただそこに獣の毛を発見した。
城主の$cherryは体調を崩して部屋にこもってしまい、イベントも開催できず、そんな中、$mochが姿を消した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$reuiが殺されたことで元刑事$hugarが主導権を取り、殺人事件の捜査が行われることになった"),
            w.plot_turnpoint("警察を呼ぼうと船を見ると、船が壊されていた"),
            w.plot_develop("$hugarが$maryたちを助手に使い、全員の取り調べを行うが心霊学者$karlは魔獣の仕業と騒ぎ立てたり、城主$cherryは部屋にこもってしまったりとうまくいかない"),
            w.plot_turnpoint("$sherlockに通信機で連絡を取るが応答がなかった"),
            w.plot_resolve("$hugarは容疑者として地元学者$jamosを部屋に監禁するが、$maryたちにはどうも犯人とは思えなかった"),
            w.plot_turnpoint("その夜、観光課の$mochが失踪した"),
            outline=ABSTRACT)

