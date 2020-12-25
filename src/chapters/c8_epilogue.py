# -*- coding: utf-8 -*-
'''
Chapter "エピローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import Market
from scenes import ReadingRoom
from scenes import SherlockHouse
from scenes import WilsonHouse


# Episode
# NOTE
#   .全ての顛末＞本物の$wilsonが帰ってくる
#   .探偵の誕生＞探偵社を設立
#   .$wilsonの手記＞新しい仕事が舞い込んでくる

# NOTE: charas
#   ・本物の$wilson（一応ここが初出。だが$nowlisとして市場で出てきた男でもある。勘のいい読者だけ分かるように

# NOTE: stages

# NOTE: items

def total_the_end(w: World):
    return w.episode("全ての顛末",
            )


def detective_office(w: World):
    return w.episode("探偵の誕生",
            )


def wilsons_papers(w: World):
    return w.episode("$wilsonの手記",
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[-1],
            w.plot_setup("莫大な弁護士費用などで借りていた住居を追い出されそうになる"),
            w.plot_turnpoint("本物の$wilsonが帰ってくる"),
            w.plot_develop("$wilsonは$sherlockたちから全ての事情を聞く"),
            w.plot_turnpoint("$wilsonが$sherlockの活躍を小説にして出版することになる"),
            w.plot_resolve("正式に$officeを設立し、情報を集めながら$bossを復活させようという勢力と闘うことになった"),
            #
            total_the_end(w),
            detective_office(w),
            wilsons_papers(w),
            w.symbol("（了）"),
            )


