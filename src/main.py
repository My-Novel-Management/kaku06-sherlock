
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
def ch_main(w: World):
    return w.chapter('main',
            w.plot_setup("世界から突如魔王の脅威が消え去った"),
            w.plot_setup("かつて勇者と呼ばれていた若者のもとに老人$cradesがやってくる"),
            w.plot_setup("$cradesは魔王が復活して世界を滅ぼそうとしているから助けてほしいと頼むが、勇者は応じない"),
            w.plot_turnpoint("そんな二人の前に、ある事件が持ち込まれた"),
            w.plot_turnpoint("$heroが谷に落ちて消える"),
            w.plot_resolve("化けていた$heroが正体を現して事件を解決する"),
            w.plot_note("後半の中編の途中で最後の事件からの空き家の冒険のコンボを決める"),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "１０万字の予定は以下のようにする",
            "短編（１万から２万字）を３本で５万字",
            "中編（５万字）を１本",
            "これで１冊分になるように調整する",
            "今回はホームズシリーズから色々と引っ張ってきて、そのタイトルをかぶせる",
            "冒険に出たくない勇者を大好きな「謎」を餌になんとか冒険させようとする、という形に",
            "ホームズ（初期型）とワトソン（クラデス）に、途中参加メンバーを加えてパーティにする",
            "勇者ということは隠しつつ、探偵です、の代わりに「勇者です」と言う",
            "「ただの謎解き好きな勇者です」",
            "全体を通して「緋色の研究」を。内容として細かく「踊る人形」とか入れていく",
            "ボヘミアの醜聞と赤毛組合、",
            "短編は基本的に「冒険」から引く",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "勇者はDQっぽく、何か名前があるんだろうけど「あんた」とか呼ばせる",
            "全体は三人称で",
            "特殊な場合に限り、一人称もあり（叙述トリックなど）",
            "パーティは勇者、元神官の魔法使い、女騎士、女武闘家",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            "魔王の脅威にさらされていたが、ある日突如として魔王が消えた世界",
            "なぜか突然戻った平和な世界で、隠居した勇者を引っ張り出す",
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

