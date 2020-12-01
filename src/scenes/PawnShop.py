# -*- coding: utf-8 -*-
'''
Stage: "質屋"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   ライムが勤めていた質屋。
#   SaxeCoburgSquareに存在する
#   [倉庫][控室][トイレ]
#   [店舗]
#   [玄関]


## scenes
def limes_job_place(w: World):
    return w.scene("$limeが働く場所",
            )

