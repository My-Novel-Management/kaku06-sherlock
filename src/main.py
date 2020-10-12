
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 10K
#   4. Spec
#   5. Plot         - 1/4: 25K
#   6. Scenes
#   7. Conte        - 1/2: 50K
#   8. Layout
#   9. Draft        - 1/1: 100K
#
################################################################

# Constant
TITLE = "勇者は冒険より謎解きが得意"
MAJOR, MINOR, MICRO = 1, 1, 0
COPY = "勇者は冒険することよりも謎解きをしている方が楽だった"
ONELINE = "冒険嫌いな勇者は旅の仲間と共に今日も謎を解いては冒険せずにいる。そんな彼は今日も謎を見つけてそちらに吸い寄せられる"
OUTLINE = "冒険嫌いな勇者は魔王を倒すことよりも謎解きに執心していた"
THEME = "謎解きで世界を救う"
GENRE = "謎解きファンタジィ"
TARGET = "10-30years"
SIZE = "10万字以上"
CONTEST_INFO = "第6回カクヨムコンテスト（異世界ファンタジー部門）"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["ファンタジー", "勇者", "謎解き", "ミステリ"]
RELEASED = (12, 1, 2020)


# Episodes
def ep_xxx(w: World):
    return w.episode('episode_title',
            outline="description")


def ch_main(w: World):
    return w.chapter('main',
            )

# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            )

def motif_note(w: World):
    return w.writer_note("モチーフ",
            )


# Main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            plot_note(w),
            chara_note(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

