
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
# import chapters
from chapters import blue_garnet
from chapters import devil_dog
from chapters import empty_house
from chapters import epilogue
from chapters import last_case
from chapters import prince_scandal
from chapters import prologue
from chapters import red_armor_club
from chapters import sadness_valley


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
MAJOR, MINOR, MICRO = 1, 5, 1
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


# Chapters
def ch_main(w: World):
    return w.chapter('main',
            w.plot_setup("かつて世界は$bossの脅威にさらされた"),
            w.plot_setup("しかし$heroと呼ばれる存在たちの手によりその脅威は拭い去られ、世界に平和がもたらされた"),
            w.plot_setup("現在世界は$heroとその仲間の末裔たちによって統治、管理されている"),
            w.plot_setup("ある目的で$wilsonは捜し物が得意という男の許を訪ねる"),
            w.plot_setup("依頼しようとした$wilsonの素性を言い当てたその男$sherlockは「勇者さん」と呼ばれていた"),
            w.plot_turnpoint("そんな二人の前に、ある事件が持ち込まれた"),
            w.plot_develop("$heroはその知的好奇心と抜群の推理力をいかして持ち込まれた事件を解決する"),
            w.plot_develop("その事件関係者だった、容疑者にされて家から排除されそうになった$maryや、呪いの鎧を着てしゃべれなくなった失踪中の第二王女を仲間にする"),
            w.plot_develop("一方、世間では謎の怪死事件が続いていた"),
            w.plot_develop("その事件に関わっているのが宗教団体という情報を手に入れ、その捜査を行う"),
            w.plot_turnpoint("しかしそれは罠で、$heroがこの世ではないどこかに通じるという穴に落ちて姿を消してしまう"),
            w.plot_resolve("残された$wilsonと$maryたちは彼の行方を探しつつ、持ち込まれた依頼の対応をしようとする"),
            w.plot_resolve("実は$wilsonは偽物で、本物の勇者の末裔を探し出し、それの心臓を手に入れようとした闇のモノだった"),
            w.plot_resolve("偽$wilsonの罠にはまりそうになった$maryたちを謎の男が救出したが、その男は変装していた$sherlockだった"),
            w.plot_resolve("本物の$wilsonが現れ、王室から正式に「魔王探索」を依頼され、冒険の旅に出ることになった"),
            "８章か７章でまとめる",
            )

def chapters(w: World):
    return (
            ch_main(w),
            prologue.main(w),
            prince_scandal.main(w),
            sadness_valley.main(w),
            red_armor_club.main(w),
            blue_garnet.main(w),
            devil_dog.main(w),
            last_case.main(w),
            empty_house.main(w),
            epilogue.main(w),
            )

# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            "ライトノベル界隈では異世界ファンタジィが一大勢力となり、その他は衰退した",
            "出版社側も求められているのは異世界転生か、異世界ものファンタジィ、あるいはラブコメと決めてしまって、",
            "なかなか他のジャンルは日の目を見ない",
            "中でも正統派のファンタジィは難しく、またミステリも一部では人気があるものの、やはり肩身が狭い思いをしている",
            "そこで今回は古典的探偵ものの名作である「シャーロック・ホームズ」をベースにして、そこに「勇者」や「魔王」といった世界観をプラスしてしまおうという企画である",
            "これが生まれる背景には、以前書いた「勇者は冒険より謎解きが得意」というシリーズがある",
            "勇謎シリーズは元ネタに「えんどろ〜」というドラクエＲＰＧライクな世界観のゆる百合ファンタジィ作品がある",
            "あんな絵柄で簡単なミステリを、カクヨムの企画のために短編連作でいけるようにと書いたものだった",
            "おそらくライトな雰囲気があった方が多くの人がとっつきやすいのだろうが、そういう雰囲気を意識しつつも、ミステリ部分は本格を目指す",
            "ノリは多少ライトな部分はあるが、ファンタジィの世界観もミステリのトリックもしっかりと構築した、世界と世界観を楽しめる作品とする",
            "本作はライトノベル業界の新しい潮流の一つとなる可能性を秘めている",
            "ウェブ派生の作家が、とにかく早く、大量に書くということを強いられているが、やはりしっかりとしたものを、構成を考えて書かれたものを、提供すべきだ",
            "これはその第一の矢となる作品である",
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
            "ファンタジーで不思議な能力や生き物のいる世界を扱うけれども、リアルを考えるとそう心地のいい世界でも都合のいい世界でもないよ、ということ",
            w.tag.title("全体テーマ"),
            "全体に共通するのは「事実は小説より奇なり」",
            "$sherlockは常に「不思議というのは単なる思考停止だ。それを見て考えることを放棄する行為だ」と",
            w.tag.title("醜聞のテーマ"),
            "見栄と知恵",
            "人間は見栄を張りながら生きていて、どうしても曲げられない部分を持っているのが息苦しい原因である",
            w.tag.title("谷のテーマ"),
            "「家族」",
            "偽物の家族と血筋を巡る駆け引きとか悲しいことがある",
            w.tag.title("赤鎧テーマ"),
            "「施し」",
            w.tag.title("ガーネットテーマ"),
            "「犠牲」",
            "誰かの生命は誰かの犠牲の上に成り立っている。人間は動物を植物を食べて生きる。そうやって繋がっている",
            w.tag.title("魔犬のテーマ"),
            "「愛情（わがまま）」",
            w.tag.title("最後の事件テーマ"),
            "「裏切り」",
            w.tag.title("空き家のテーマ"),
            "「信頼」",
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
            *chapters(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

