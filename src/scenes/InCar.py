# -*- coding: utf-8 -*-
'''
Stage: "車・車内"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   魔導車。基本的にほとんど誰も所持していない高級品なので、特別な場合か、ウィルソンに連れて行ってもらう時だけ
#   後部座席あわせて四人まではいける


## scenes
def goto_aily_house(w: World):
    return w.scene("$ailyの家に向かう",
            w.plot_note("$carに乗せてもらい$wilsonの運転でその女の家に向かう"),
            w.plot_note("手紙に同封されていた地図と情報を見る$sherlock"),
            )


def goto_orphanage(w: World):
    return w.scene("孤児院に向かう",
            w.plot_note("$ailyという女性については謎が多い"),
            w.plot_note("市場によって$ignesたちに情報を集めるように指示する"),
            w.plot_note("$wilsonの財布を返してもらったが、中身は減っていた"),
            )
