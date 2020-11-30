# -*- coding: utf-8 -*-
'''
Stage: "警察署"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   交番規模のものから、警察署本部までこちらで


## scenes
def interrogation(w: World):
    return w.scene("事情聴取",
            w.plot_note("警察の事情聴取を受けた$maryたち"),
            )

