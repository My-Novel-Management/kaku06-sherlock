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
from chapters import c4_blue_garnet
from chapters import c5_devil_dog
from chapters import c7_empty_house
from chapters import c8_epilogue
from chapters import c6_last_case
from chapters import c1_prince_scandal
from chapters import c0_prologue
from chapters import c3_red_armor_club
from chapters import c2_sadness_valley


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 10K
#   4. Spec
#   5. Plot         - 1/4: 25K
#   6. Scenes
# > 7. Conte        - 1/2: 50K
#   8. Layout
#   9. Draft        - 1/1: 100K
#
################################################################

# Constant
TITLE = "勇者シャーロックは冒険しない　闇色の研究"
MAJOR, MINOR, MICRO = 1, 7, 1
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
def chapters(w: World):
    return (
            # NOTE
            #   - （勇者の）血にまつわる数々の事件
            #   - 亜人が関係する悲しい事件
            #   - 魔王復活のために四つの魔石と勇者の心臓が必要
            #   - 魔導により、かつての魔法や魔術は古いものとされている変革の時代
            w.plot_setup("$heroたちにより$bossが倒され、平和が取り戻された世界"),
            w.plot_setup("かつて存在した$magicや$sorceryは廃れ、代わりに$scienceが世界技術の基盤になっていた"),
            w.plot_setup("世間では謎の連続失踪事件が発生していた"),
            w.plot_setup("そんな中、王室の第二王女が失踪する"),
            w.plot_setup("$wilsonは王室からの依頼でその第二王女を探すことになった"),
            w.plot_setup("難解な謎を解決する便利屋の$sherlockという男がいた"),
            w.plot_turnpoint("$wilsonは$sherlockに連続失踪事件についての依頼をする"),
            w.plot_develop("$sherlockは持ち込まれた依頼を解決する"),
            w.plot_develop("解決した事件で天涯孤独の身になった$maryが$sherlockの家に居候するようになる"),
            w.plot_develop("$maryが謎の鎧騎士を連れてきて、奇妙な仕事について$sherlockに助言を求める"),
            w.plot_turnpoint("謎の鎧騎士の正体は失踪中の第二王女$limeだった"),
            w.plot_develop("ある事情から王室に戻りたくないという$limeが、$sherlockの家に居候する"),
            w.plot_develop("$morianoが全ての事件の糸を引いていると知る"),
            w.plot_develop("$morianoが$sherlockに手を引けと警告する"),
            w.plot_turnpoint("$sherlockが$morianoとともに死ぬ"),
            w.plot_develop("$maryたちは$sherlockが残した手がかりを使い、$boss復活を阻止するために四つの$stoneを集める"),
            w.plot_turnpoint("だが$patsonに裏切られ、集めた$stoneを盗まれる"),
            w.plot_develop("$boss復活の儀式を行う$patson"),
            w.plot_develop("しかし儀式は失敗し、$patsonは死んでしまう"),
            w.plot_develop("$sherlockが生きていることが分かる"),
            w.plot_turnpoint("$sherlockが$heroの血を引く人間だった"),
            w.plot_develop("$sherlockが囚われ、儀式に利用されようとする"),
            w.plot_develop("$maryたちは$sherlockを救出に向かう"),
            w.plot_turnpoint("全ての黒幕は$wilsonだった"),
            w.plot_resolve("$wilsonは偽物で$boss復活のために裏で色々と動いていた"),
            w.plot_resolve("$magicを使い姿を消した偽$wilsonはその後、山中の小屋で自殺しているのが発見された"),
            w.plot_resolve("本物の$wilsonが出現し、$sherlockたちの活躍を本にして金にすることになった"),
            # NOTE
            #   $boss復活／$scienceと$magic／血／$animal（闇の住人）／革命により変わりゆく世界
            #   1. 世界観披露（$hero後の世界）／$sherlock紹介／$scienceと$magic／$stone
            #   2. $animal登場
            #   3. 王室（血脈）／
            #   4. $jackと孤児院（$animalの）／黒幕／$stoneの意味
            #   5. 古代$magic／
            #   6. 黒幕$morianoと改造$gun
            #   7. $boss復活の儀式と全ての伏線回収
            c0_prologue.main(w),
            c1_prince_scandal.main(w),
            c2_sadness_valley.main(w),
            c3_red_armor_club.main(w),
            c4_blue_garnet.main(w),
            c5_devil_dog.main(w),
            c6_last_case.main(w),
            c7_empty_house.main(w),
            c8_epilogue.main(w),
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
            title_note(w).omit(),
            *persons.main_notes(w),
            *stages.main_notes(w),
            *settings.main_notes(w),
            theme_note(w).omit(),
            motif_note(w).omit(),
            *chapters(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

