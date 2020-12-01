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
def true_wilson(w: World):
    return w.episode("本物の$wilson",
            "ここはまだ三人称のまま",
            WilsonHouse.after_case(w),
            Market.social_condition(w),
            WilsonHouse.lost_home(w),
            WilsonHouse.real_wilson(w),
            WilsonHouse.know_all_things(w),
            WilsonHouse.wilsons_proposal(w),
            )


def heros_office(w: World):
    return w.episode("$hero探偵社",
            "ここで$wilsonの一人称に変更",
            "これからの物語",
            ReadingRoom.allend_and_allstart(w),
            SherlockHouse.last_scene(w),
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
            true_wilson(w),
            heros_office(w),
            w.symbol("（了）"),
            )


