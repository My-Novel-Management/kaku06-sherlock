# -*- coding: utf-8 -*-
'''
Episode: 0-0 "厄介事と便利屋"
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
遥か昔に$bossが倒されて平和になったはずの世界。$science技術により産業革命が起こる変革期だった。$wilsonは王室から第二王女失踪の調査を依頼され、困っていた。
行きつけの酒場で旧知の元軍医$stanと再会し、彼から便利屋$sherlockという男を教わる。翌日、$sherlockに仕事を依頼しようと彼の家を訪れるのだが。
その出会いが、やがて大きな事件に関わることに繋がっていた。
"""


# Episode
def main(w: World):
    return w.episode("厄介事と便利屋",
            # NOTE
            w.plot_setup("王室の厄介事を片付けるエージェントの$wilsonは第二王女が失踪した件についての調査と捜査をすることになっていた"),
            w.plot_turnpoint("情報を集める為に訪れたパブで旧知の元軍医$stanと再会する"),
            w.plot_develop("$stanとは王立学校時代の同期生で彼は医師を目指し、$wilsonは弁護士を目指した仲だった。互いの近況を語り合う"),
            w.plot_turnpoint("$stanから便利屋$sherlockについて教わる"),
            w.plot_resolve("後日、その便利屋$sherlockに仕事を依頼する為に彼の家を訪れた"),
            outline=ABSTRACT)

