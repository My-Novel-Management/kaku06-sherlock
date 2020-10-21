# -*- coding: utf-8 -*-
'''
About: "舞台・世界観"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# world settings
def main_notes(w: World):
    return (
            stages_note(w),
            )


def stages_note(w: World):
    return w.writer_note('舞台設定',
            w.tag.title("イギリスを模した王国（女王の国）"),
            )

