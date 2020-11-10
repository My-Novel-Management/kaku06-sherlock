# -*- coding: utf-8 -*-
'''
Chapter "青いガーネット"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES


## chapter
def main(w: World):
    return w.chapter(TITLES[4],
            w.plot_setup(""),
            w.plot_turnpoint(""),
            w.plot_develop(""),
            w.plot_turnpoint(""),
            w.plot_develop(""),
            w.plot_turnpoint(""),
            w.plot_develop(""),
            w.plot_turnpoint(""),
            w.plot_develop(""),
            w.plot_turnpoint(""),
            w.plot_resolve("$jackは$sherlockに隠し持っていた$stoneを渡して目的阻止を依頼した"),
            #
            w.plot_setup("最近巷で怪盗$jackの話を聞かなくなっていた"),
            w.plot_setup("$maryが仲良くなった市場の男からニワトリをもらってくる"),
            w.plot_turnpoint("そのニワトリを捌くと中から宝石が出てくる"),
            w.plot_develop("その宝石はどうやら$ailyに盗まれた宝剣についていたものと同じだと分かる"),
            w.plot_develop("$sherlockは$ailyの消息を改めて探る"),
            w.plot_develop("謎の女性の猟奇殺人が発生するが、それが怪盗$jackの死体と言われる"),
            w.plot_turnpoint("$sherlockのもとに$ailyからの手紙が届く"),
            w.plot_resolve("その暗号を解読し、$sherlockは$ailyに会いに向かう"),
            w.plot_resolve("宝石がある儀式に必要とされ、自分が狙われたから預かってもらったと$jackは告白した"),
            w.plot_resolve("$jackは改めて$sherlockに全ての糸を引く黒幕の存在を調べて、その情報が欲しいと依頼した"),
            "もらったニワトリ",
            w.plot_note("市場から$maryがニワトリをもらってくる"),
            w.plot_note("しかし$sherlockは肉になる前の動物は苦手だという"),
            w.plot_note("$wilsonがニワトリをさばこうと言ってくれる"),
            w.plot_note(""),
            "持ち主は誰だ",
            w.plot_note("市場に向かい、持ち主を探すことにする"),
            "$jackとの再会",
            w.plot_note("そのガーネットについての情報を持っているという謎のタレコミの手紙が届く"),
            w.plot_note("$sherlockは一人、その場所に向かう"),
            w.plot_note("待っていたのは$ailyこと$jackだった"),
            w.plot_note("死んだとは思っていなかったが戻ってくるとは思ってなかった$sherlock"),
            w.plot_note("「一度ちゃんとデートをしたいと言ったでしょう」と$jack"),
            w.plot_note("付き合って欲しい場所があると、日時と場所を指定した$jackのカードを渡される"),
            "$jackとデート",
            w.plot_note("博物館の改築が終わり、そこを見る"),
            w.plot_note("盗まれたことを内緒にしてダミーの宝石が飾られている"),
            w.plot_note("$heroに関しての四つの宝石があり、その一つが宝剣についていたもので、"),
            # NOTE:４つの宝石考える
            w.plot_note("残りの一つがあのニワトリに飲み込まれてしまったガーネットだという"),
            w.plot_note("盗み出したものの、それを持ち運ぶために一旦ニワトリに飲み込ませたが、そのニワトリが混ざってしまい、市場に流れた"),
            w.plot_note("それをたまたま$maryがもらったのがことの発端だった"),
            w.plot_note("宝石を返してもらえるかしら、と$jack"),
            w.plot_note("$sherlockは何故そこまで四つの宝石を必要とするのかを知ることと引き換えに渡すと言い出す"),
            w.plot_note("彼女は「大切なものを取り戻すため」としか答えない"),
            w.plot_note("$sherlockは他にもこの宝石を狙っている勢力があることを伝えて、手を引くように忠告する"),
            w.plot_note("しかし$sherlockは$jackが準備した男たちに取り囲まれ、仕方なく持ってきていたガーネットを渡した"),
            "殺人事件",
            w.plot_note("翌日、川で謎の女性の死体が上がる"),
            w.plot_note("身元不明だったが背格好から逃亡中の$ailyだと推測された"),
            w.plot_note("持ち物はなく、あのガーネットも消えてしまっていた"),
            "事件の顛末",
            w.plot_note("$sherlockのもとに手紙が届く"),
            w.plot_note("差出人名はなかったがそれが$jackのものと分かる"),
            w.plot_note("手紙にはひょっとしたら殺されるかも知れないと書いてある"),
            w.plot_note("内容は$sherlockにその場では話せないと言ったことについてだった"),
            w.plot_note("大昔の秘術で亡くなった人間を蘇らせるというものがあり、それに利用するために高$enagyを閉じ込めた媒体が必要"),
            w.plot_note("それが四つの宝石だった"),
            w.plot_note("これで行方の知れない残り１つの宝石を、謎の勢力が探すことになるだろうと"),
            w.plot_note("$sherlockは自分の情報網にフェイクの情報を流して、その勢力と動きをあぶり出すことにした"),
            )


