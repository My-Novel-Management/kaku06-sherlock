
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
import persons
import stages
import plots
import settings
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
TITLE = "勇者シャーロックは冒険しない"
MAJOR, MINOR, MICRO = 1, 2, 1
COPY = "勇者は冒険よりも事件解決を選んだ"
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
def ep_crades_meet_hero(w: World):
    return w.episode("$heroを訪ねて",
            w.plot_note("$cradesは$alexを訪ねる"),
            w.plot_note("ある依頼をしようとやってきたのだが、依頼を口にする前から色々と言い当てられてしまう"),
            w.plot_note("自分の正体が元神官だとばらして、その上で依頼をする"),
            w.plot_note("依頼内容は「ある女性から短刀（宝剣）を取り返して取り返してもらいたい」というもの"),
            w.plot_note("それがどういう由来を持つかは聞かないなど、条件つき"),
            w.plot_note("実は王子$adamsが結婚することになり、過去の女性関係を精算したが、その女性にプレゼントした宝剣はどうしても返してもらえなかった"),
            w.plot_note("そういう事情なら泥棒にでも頼めばいいと断る"),
            w.plot_note("世間では義賊として「怪盗$rudy」が暗躍していた"),
            )

def ep_phantom_rudy(w: World):
    return w.episode("怪盗$rudy",
            w.plot_note("王国や金持ちが所有している中から宝石などを盗み出し、孤児院などに寄付をしていく怪盗がいた"),
            w.plot_note("正体を見た者はいない"),
            w.plot_note("色々な噂があったが、王国警察もまだ捕まえるに至っていない"),
            )

def ep_clever_lady(w: World):
    return w.episode("賢い女$ail",
            w.plot_note("変装して逃亡しようとした$ailを最後のところで追い詰める"),
            w.plot_note("$alexは$ailが$rudyだと見破っていた"),
            w.plot_note("宝剣の場所を尋ねるが既に闇マーケットに流したらしい"),
            w.plot_note("なぜ王国に恨みを持つのかという質問には王国の謎を突き止めれば自然と分かるとだけ"),
            w.plot_note("最後のところで逃してしまう"),
            )

def ep_red_armor(w: World):
    return w.episode("赤鎧組合",
            w.plot_note("赤い鎧を着た者だけを集めている不思議な組合があった"),
            w.plot_note("そこで選ばれた赤鎧はずっと写本をしているだけで給料と食べ物が支給された"),
            w.plot_note("その謎の仕事について依頼がある"),
            w.plot_note("実は金持ちの家の護衛を休ませて、その間に秘密の抜け穴を掘るということを盗賊団が行っていた"),
            w.plot_note("その赤鎧組合の中に一人奇妙な鎧がいた"),
            w.plot_note("それも女性で、実は彼女は失踪中の第二王女だった"),
            w.plot_note("$emilは$alexたちの住居に居候することになる"),
            )

def ep_falling_down(w: World):
    return w.episode("落下の滝",
            )


def ep_darkdog(w: World):
    return w.episode("恐怖の魔犬",
            )


def ep_comeback_hero(w: World):
    return w.episode("戻ってきた英雄",
            w.plot_note("奇妙な密室殺人についての調査を引き受けた$crades"),
            w.plot_note("$cradesは頭を悩ませていた"),
            w.plot_note("謎の男の正体は$alexだった"),
            )


# Chapters
def ch_main(w: World):
    return w.chapter('main',
            w.plot_setup("かつて世界は$bossの脅威にさらされた"),
            w.plot_setup("しかし$heroと呼ばれる存在たちの手によりその脅威は拭い去られ、世界に平和がもたらされた"),
            w.plot_setup("現在世界は$heroとその仲間の末裔たちによって統治、管理されている"),
            w.plot_setup(""),
            w.plot_setup("かつて勇者と呼ばれていた若者のもとに老人$cradesがやってくる"),
            w.plot_setup("$cradesは魔王が復活して世界を滅ぼそうとしているから助けてほしいと頼むが、勇者は応じない"),
            w.plot_turnpoint("そんな二人の前に、ある事件が持ち込まれた"),
            w.plot_turnpoint("$heroが谷に落ちて消える"),
            w.plot_resolve("化けていた$heroが正体を現して事件を解決する"),
            "１話あたり5000文字×４話の２万字相当で、全体を２０万字で調整する",
            "一応中央値１０万字で折り返しになるように",
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def title_note(w: World):
    return w.writer_note("タイトル考",
            "基本的に名作ミステリのタイトルをもじる",
            "「虹色の研究」",
            "「赤鎧組合」",
            "「勇者の帰還」",
            "「鼻のねじれた男」",
            "「バンカーブルの魔犬」",
            "「勇者最後の事件」",
            "「廃墟の冒険」",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "全体に共通するのは「事実は小説より奇なり」",
            "ファンタジーで不思議な能力や生き物のいる世界を扱うけれども、リアルを考えるとそう心地のいい世界でも都合のいい世界でもないよ、ということ",
            )

def motif_note(w: World):
    return w.writer_note("モチーフ",
            "ミステリ",
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
            *plots.main_notes(w),
            title_note(w),
            *persons.main_notes(w),
            *stages.main_notes(w),
            *settings.main_notes(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

