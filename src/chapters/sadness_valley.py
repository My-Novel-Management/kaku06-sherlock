# -*- coding: utf-8 -*-
'''
Chapter "悲しみの谷"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[2],
            "舞台はそう遠くない田舎町",
            w.plot_setup("谷の田舎町で$gunを使った殺人事件が発生する"),
            w.plot_setup("その事件の容疑者が被害者の娘$maryだった"),
            w.plot_setup("$maryの家の使用人は彼女の無実を訴える"),
            w.plot_turnpoint("話を聞いて$sherlockは$maryの無実を確信する"),
            w.plot_develop("現地に赴き、調査する$sherlock"),
            w.plot_develop("亡くなった男性の家は地元でも有数の金持ちだった"),
            w.plot_develop("一人娘の$maryを愛していたはずの父親と何故口論していたのか、$maryは話したがらない"),
            w.plot_develop("警察に連れて行かれてしまう$mary"),
            w.plot_turnpoint("$maryの部屋で母親の死体が発見される"),
            w.plot_resolve("$maryをはめたのは、使用人の父親だった"),
            w.plot_resolve("婦人との間に作った自分の息子を正当な跡取りとするために、旦那を殺害した"),
            w.plot_resolve("しかし$maryが拾われた子どもだと知り、かつて愛した女を殺してしまった"),
            w.plot_resolve("身寄りを失った$maryを$sherlockは引き取った"),
            "$wilsonの依頼",
            w.plot_note("改めて$wilsonは$sherlockに依頼内容を語る"),
            w.plot_note("実はこの半年の間に謎の失踪事件が続いている"),
            w.plot_note("それは誰もが「$heroの血を引く者」だった"),
            w.plot_note("$heroとはかつて$bossを倒し、この世界に平和をもたらした存在とその仲間たちのことで、"),
            w.plot_note("現在この王国を始め、様々な重要部署を取り仕切っている"),
            w.plot_note("その中で血を濃く引くと言われているいくつかの家系がある"),
            w.plot_note("それぞれの家で直系の人間が失踪している"),
            w.plot_note("何か関連があるのか、あるとすればどんな力が働いているのか、それらを調べて報告してもらいたいと"),
            w.plot_note("$sherlockは新聞のスクラップを見せて「すでに興味がある事件だ」と答える"),
            w.plot_note("ただ情報が少ないので今すぐどうこうは言えないが、それでもある程度の推測は持っていると答えて、依頼を受けることにした"),
            "殺人事件",
            w.plot_note("そこに依頼の電報が舞い込む"),
            w.plot_note("内容はある殺人事件の容疑者となった女性を救って欲しいというものだった"),
            w.plot_note("$sherlockは$wilsonに車を出してもらい駅まで向かうことにした"),
            "谷の街",
            w.plot_note("駅まで迎えに来た少年$keanはある屋敷に務める使用人の家族の子だと自己紹介する"),
            w.plot_note("$sherlockはすぐにこの土地の大地主である$ln_royd家のものだと分かる"),
            w.plot_note("事件については現地についてから聞くことにして、まずこの街についての知識を確かめる$sherlock"),
            w.plot_note("街は大きな沼地で、昔は人家も少なく、作物もできず、その土地を購入した$ln_royd氏がここで育つ作物を見つけて財を成したらしい"),
            w.plot_note("谷の名前もそこからきている"),
            w.plot_note("屋敷は街の北側にあり、そこまで広大な湿原が広がっている"),
            w.plot_note("農場の手伝いもする$keanは事件が起こった場所で説明を始める"),
            "事件概要",
            w.plot_note("事件は呼び出された$royd氏とその娘である$maryが口論をしていて、翌朝、死体となって$royd氏が発見されたところから始まる"),
            w.plot_note("口論の現場を目撃したのは使用人の$kail（$keanの父）で、その証言と現場で発見されたナイフについていた$maryの指紋から容疑者が確定している"),
            w.plot_note("現場は湿原で、酷い雨により足跡は全て書き消えてしまっている"),
            w.plot_note(""),
            # TODO
            )

