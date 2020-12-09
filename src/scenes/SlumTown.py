# -*- coding: utf-8 -*-
'''
Stage: "スラム街"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   切り裂きジャック事件で有名なホワイト・チャペル地区（イーストエンドの一部）。有名な貧困街
#   チャリング・クロスの東5.5Km


# alias
TOWN = "Whitechapel"

# Scenes
## in Empty House
def goto_empty_house(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    return w.scene("空き家に向かう",
            w.change_stage(TOWN),
            mary.come("$wilsonにつれられ、スラム街にやってくる"),
            wil.come(),
            lime.come(),
            mary.do("この一年ほどの間に連続失踪・殺人事件が発生している有名な$Whitechapel地区だった"),
            mary.do("恐い、と感じていつも足を踏み入れないように$Sは注意していた"),
            mary.do("煙をくゆらせ、男も女も鋭い眼光でちらっと見てくる"),
            lime.do("$maryを守るようにして歩く$S"),
            wil.talk("この先らしい"),
            wil.do("手帳を見ながら先に歩いていく$S"),
            )


def rescue_mary(w: World):
    lime = w.get("lime")
    ignes = w.get("ignes")
    pat = w.get("patson")
    return w.scene("$maryを助けに",
            w.change_camera("lime"),
            w.change_stage(TOWN),
            lime.come("$Sは$ignesとともに彼らが見つけた廃工場にやってくる"),
            ignes.come(),
            pat.come("$Sも駆けつけてくれた"),
            pat.talk("本当にここに？"),
            ignes.talk("$sherlockの指示通りだとちょうどこの辺りなんだ"),
            lime.do("その時、大きな爆音がして吹き飛んだ"),
            pat.talk("な、何だ！？"),
            ignes.talk("あっちか"),
            ignes.do("$Sが先に走り出す"),
            lime.do("$Sもそのあとを追った"),
            )
