# -*- coding: utf-8 -*-
'''
Stage: "（ロンドン）市内"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   市内をモンタージュ的に巡る時にはここを使う
#   俯瞰映像やイメージで語る時も使ってよい


## scenes
def magic_and_tech_city(w: World):
    return w.scene("$magicと産業革命の街",
            w.plot_note("車で走りながら市内の簡単な紹介"),
            w.plot_note("王宮を中心に、南側にはテムズ川が東西に伸びて"),
            w.plot_note("各地に市場が立っている"),
            w.plot_note("まるで何事もないような賑わい"),
            w.plot_note("ただこの街で既に百名が失踪している"),
            )

