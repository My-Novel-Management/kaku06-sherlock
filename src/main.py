
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
from settings import world_note
from settings import calture_note
from plots import mystery_note
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
MAJOR, MINOR, MICRO = 1, 2, 1
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
            w.plot_setup("世界から突如魔王の脅威が消え去った"),
            w.plot_setup("かつて勇者と呼ばれていた若者のもとに老人$cradesがやってくる"),
            w.plot_setup("$cradesは魔王が復活して世界を滅ぼそうとしているから助けてほしいと頼むが、勇者は応じない"),
            w.plot_turnpoint("そんな二人の前に、ある事件が持ち込まれた"),
            w.plot_turnpoint("$heroが谷に落ちて消える"),
            w.plot_resolve("化けていた$heroが正体を現して事件を解決する"),
            "１話あたり5000文字×４話の２万字相当で、全体を２０万字で調整する",
            "一応中央値１０万字で折り返しになるように",
            w.plot_note("１話（安楽椅子・ダイイングメッセージ）：$cradesが$heroを見つけて、魔王退治を依頼する。現場に行かずに事件解決（しかし情報間違っていたので後で推理し直す）"),
            w.plot_note("２話（アリバイ・人物偽装）：ボヘミアの醜聞。$ail登場"),
            w.plot_note("３話（事実誤認）：$pan仲間回。ボスコム警告の惨劇"),
            w.plot_note("４話（奇妙な設定）：$emil仲間回。赤毛組合。鎧騎士だけを集めた謎の組合"),
            w.plot_note("５話（密室）：くちびるのねじれた男"),
            w.plot_note("６話（クローズド）：犬の仕業みたいな謎の殺人事件発生"),
            w.plot_note("７話（奇妙な凶器）：魔獣の討伐依頼"),
            w.plot_note("８話（不可能犯罪）：$ail再登場し、警告"),
            w.plot_note("９話（見立て）：冒険嫌いの理由。"),
            w.plot_note("１０話（心理トリック）：$heroが滝に落ちる。ライヘンバッハの滝（最後の事件）"),
            w.plot_note("１１話（人物誤認）：実は謎の男の正体は$heroだった。空き家の冒険"),
            w.plot_note("１２話（叙述トリック）：戻ってきた$hero。実は$gradesは偽物で、連続殺人の真犯人だった"),
            w.plot_note("実は$cradesは魔王の使いで、勇者がまだ生きていることの確認とその殺害が目的だった"),
            w.plot_note("本物の$cradesは後になって登場する。ずっと謎の空間に閉じ込められていて、様々な時空を彷徨っていた"),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "基本路線は「長編１本」で、細かい事件や仲間集めを挟みつつ、冒険嫌いな勇者に冒険させるような展開",
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
            "１話は「緋色の研究の冒頭」＋「冒険」",
            "５話以降は「緋色の研究」のラストを使う。ワトソン役の$cradesが記述して残して研究していくことを決める",
            "勇者は「なぜ突然魔王が消えたのか」を知っていると$cradesと読者に思わせる",
            "１話で「$heroと$crades」コンビ結成かつ$heroの能力披露",
            "２話が$pan参加の話", "以前は「白馬に乗った王子伝説」",
            "３話が$emilの話", "大食い仮面騎士",
            "４話くらいで$ailの話ひっかけ",
            "５話からちょっと大型事件、連続殺人とか、密室殺人とか",
            "基本方針は「冒険の旅に出るまで」この街で事件解決をしつつ仲間や情報を揃える、が１巻",
            "全体の流れ：",
            "謎の殺人事件が裏で起こっている。関係者はかつて勇者に協力したとされる人間（事実ではなく噂であっても）",
            "最初は「簡単な依頼」を$cradesが持ってくる",
            "でもその事件を解決すると殺人事件に遭遇",
            "その容疑者に$pannaが選ばれる",
            "容疑を晴らすためにがんばる",
            "途中で謎の赤鎧組合が関わっているのを知る",
            "そこに潜んでいたのは「失踪中の第二王女」だった",
            "鎧の呪いを解いたが彼女は無口でしゃべらない",
            "四人の仲間と同居することになる",
            "ここまでが四話",
            "残りで怪盗と勇者連続殺人事件の真犯人を追い詰める",
            "実は$cradesが真犯人で、$cradesを名乗る別の人物だった",
            "$k_shalを$heroと確認し、滝壺に落とす",
            "しかし廃墟の冒険で生きていたことが分かり、$cradesを追い詰める",
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
            title_note(w),
            chara_note(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            world_note(w),
            calture_note(w),
            mystery_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

