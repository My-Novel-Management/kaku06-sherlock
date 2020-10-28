
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
MAJOR, MINOR, MICRO = 1, 4, 0
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

def ch_prologue(w: World):
    return w.chapter("プロローグ",
            w.plot_setup("新聞を読んでいる$sherlock"),
            w.plot_setup("再び$bossが？という見出しに苦笑"),
            w.plot_setup("部屋に入ってきた$wilsonが「また何か面白そうな事件でも見つけたかね？」と問う"),
            w.plot_develop("$sherlockの御託並べが始まる"),
            w.plot_resolve("この物語は$sherlockという奇妙な若者との出会いの記録である"),
            w.plot_resolve("$wilsonが記述者で三人称で書き残したもの、という宣言"),
            )

def ch_kingdom_scandal(w: World):
    return w.chapter("皇太子の醜聞",
            "街が舞台",
            w.plot_setup("世間では怪盗$jackという謎の存在が人気を集めていた"),
            w.plot_setup("王室からの使者として$wilsonがある短刀を取り返して欲しいと依頼する"),
            w.plot_setup("実は皇太子が結婚を控えているが、過去の女に預けた宝剣を取り戻したいというのだ"),
            w.plot_setup("だが$sherlockは王室からの依頼は全て断っていた"),
            w.plot_turnpoint("翌日、その$ailyが$sherlockに依頼に訪れた"),
            w.plot_develop("$ailyの恋人が行方不明になったという"),
            w.plot_develop("その上、その男が宝剣を持ち去ったと"),
            w.plot_develop("$sherlockは調査を開始する"),
            w.plot_develop("けれど調べるほどにその男の存在は希薄だった"),
            w.plot_turnpoint("調査結果を伝えに行くと$ailyの家はもぬけの殻になっていた"),
            w.plot_resolve("自分の家に荷物を届けにきた配達人こそが$ailyと分かったが、既に彼女は高跳びした後だった"),
            w.plot_resolve("送られた小包は宝剣だった"),
            w.plot_resolve("だがそこにはまっていた宝珠は消えていた"),
            w.plot_resolve("しかし宝剣に新しい宝珠がつけられ、皇太子の結婚式は無事に行われた"),
            )

def ch_sadness_valley(w: World):
    return w.chapter("悲しみの谷",
            "舞台はそう遠くない田舎町",
            w.plot_setup("谷の田舎町で$gunを使った殺人事件が発生する"),
            w.plot_setup("その事件の容疑者が被害者の娘$maryだった"),
            w.plot_setup("$maryの家の使用人は彼女の無実を訴える"),
            w.plot_turnpoint("話を聞いて$sherlockは$maryの無実を確信する"),
            w.plot_develop("現地に赴き、調査する$sherlock"),
            w.plot_develop("亡くなった男性の家は地元でも有数の金持ちだった"),
            w.plot_develop("一人娘の$maryを愛していたはずの父親と何故口論していたのか、$maryは話したがらない"),
            w.plot_develop("警察に連れて行かれてしまう$mary"),
            w.plot_turnpoint("$maryの部屋で母親の死体が発見される"),
            w.plot_resolve("$maryをはめたのは、使用人の父親だった"),
            w.plot_resolve("婦人との間に作った自分の息子を正当な跡取りとするために、旦那を殺害した"),
            w.plot_resolve("しかし$maryが拾われた子どもだと知り、かつて愛した女を殺してしまった"),
            w.plot_resolve("身寄りを失った$maryを$sherlockは引き取った"),
            )

def ch_red_armor(w: World):
    return w.chapter("赤鎧クラブ",
            w.plot_setup("$maryが居候し始めた"),
            w.plot_setup("買い物にでかけた先で口論からいざこざになったところを、謎の赤鎧の騎士に助けられる"),
            w.plot_setup("王国の第二王女が失踪して半年になっていた"),
            w.plot_turnpoint("その赤鎧の騎士が相談に訪れた"),
            w.plot_develop("騎士は話せず、筆記とジェスチャによる対話となる"),
            w.plot_develop("騎士が言うには自分はある護衛のアルバイトをしているが、護衛仲間に言われて赤鎧の者だけが資格のある報酬のいい短時間仕事をしている"),
            w.plot_develop("その仕事の奇妙さを誰にも相談できずにいたと"),
            w.plot_develop("$sherlockはしばらくそのまま続けるよう指示し、独自に調査を行う"),
            w.plot_turnpoint("赤鎧の騎士が再び訪れ、仕事を首になったと告白した"),
            w.plot_resolve("$sherlockは理由を話す"),
            w.plot_resolve("その店の店長と護衛仲間が共謀し、騎士を護衛場所から一定時間離れさせるのが目的だったと"),
            w.plot_resolve("警察により彼らは逮捕され、店を閉じたから解雇されてしまった"),
            w.plot_resolve("どうやら店の地下に穴を掘り、近所の博物館に展示中のあるものを盗むのが目的だった"),
            w.plot_resolve("しかしそれを偽物に取り替えておいた$sherlockの指示により犯人たちは捕まえられたのだ"),
            w.plot_resolve("事情を理解した騎士$limeは、自分のことについて語る"),
            w.plot_resolve("呪いの鎧を着ていたのは$limeという、かつて失踪した王国の第二王女だった"),
            w.plot_resolve("$limeは事情があり、王室には帰れないというので仕方なく$sherlockたちの家に居候することになった"),
            )

def ch_blue_garnet(w: World):
    return w.chapter("紺碧のガーネット",
            w.plot_setup("最近巷で怪盗$jackの話を聞かなくなっていた"),
            w.plot_setup("$maryが仲良くなった市場の男からニワトリをもらってくる"),
            w.plot_turnpoint("そのニワトリを捌くと中から宝石が出てくる"),
            w.plot_develop("その宝石はどうやら$ailyに盗まれた宝剣についていたものと同じだと分かる"),
            w.plot_develop("$sherlockは$ailyの消息を改めて探る"),
            w.plot_develop("謎の女性の猟奇殺人が発生するが、それが怪盗$jackの死体と言われる"),
            w.plot_turnpoint("$sherlockのもとに$ailyからの手紙が届く"),
            w.plot_resolve("その暗号を解読し、$sherlockは$ailyに会いに向かう"),
            w.plot_resolve("宝石がある儀式に必要とされ、自分が狙われたから預かってもらったと$jackは告白した"),
            w.plot_resolve("$jackは改めて$sherlockに全ての糸を引く黒幕の存在を調べて、その情報が欲しいと依頼した"),
            )

def ch_devil_dog(w: World):
    return w.chapter("魔犬",
            "舞台は荒野ダートムア",
            w.plot_setup("その荒野では魔獣の伝説があった"),
            w.plot_setup("実際に魔獣の仕業と考えられる猟奇殺人が発生する"),
            w.plot_setup("$sherlockのところにその捜査依頼が舞い込む"),
            w.plot_turnpoint("だが別の用事があり$sherlockが行けないと言い出す"),
            w.plot_develop("$maryたちで事件調査に赴く"),
            w.plot_develop("その家は不遇な死が続いていた"),
            w.plot_develop("情報を集めていく中で本物の魔獣に襲われそうになる"),
            w.plot_turnpoint("$maryが魔獣に殺されそうになる"),
            w.plot_resolve("$sherlockがかけつけ、魔獣を追い払う"),
            w.plot_resolve("$maryたちが集めた情報をもとに$sherlockは事件の真相に至る"),
            w.plot_resolve("降霊術で魔獣を呼び出したが、それはただ愛犬を蘇らせたいという女の気持ちだった"),
            w.plot_resolve("魔獣に餌を与える必要があり、仕方なく伝説になぞらえて殺人させたのだ"),
            w.plot_resolve("魔獣は退治され、女は逮捕された"),
            w.plot_resolve("その女に降霊術（偽物）を教えたのはある宗教団体の人間だった"),
            )

def ch_last_case(w: World):
    return w.chapter("最後の事件",
            "隣国マイリンゲンのライヘンバッハ",
            w.plot_setup("今までの事件の黒幕として$morianoが浮かび上がる"),
            w.plot_setup("$sherlockは一人でいるときに$morianoと対峙し、忠告を受ける"),
            w.plot_turnpoint("家が放火された"),
            w.plot_develop("それぞれ別々の仮宿を取った"),
            w.plot_develop("$maryや$limeが襲われる"),
            w.plot_develop("$wilsonまでも負傷し、安全が脅かされる"),
            w.plot_turnpoint("$sherlockは単身、$morianoとの対決に向かった"),
            w.plot_resolve("湖畔の屋敷で待っていた$morianoと対峙する"),
            w.plot_resolve("$morianoは全てを自供する"),
            w.plot_resolve("闇の世界について語り、$bossを復活させるためにあるものが必要だったと"),
            w.plot_resolve("全てが仕組まれていたことだと分かりながらここにやってきた$sherlock"),
            w.plot_resolve("しかし屋敷に続く橋が爆破され、警官隊は来られなかった"),
            w.plot_resolve("$sherlockが$morianoと闇の穴に落ちたと目撃証言が入った"),
            )

def ch_empty_house(w: World):
    return w.chapter("空き家の事件",
            "ベックマン街の空き家",
            w.plot_setup("穴に落ちた$sherlockがどこかで生きていると信じて探す$maryたち"),
            w.plot_setup("しかし一ヶ月経っても何も情報が得られなかった"),
            w.plot_setup("$sherlockが残した資料にあった人物が殺される"),
            w.plot_turnpoint("$wilsonが$sherlockが隠れて生き延びているらしい空き家の情報を手に入れる"),
            w.plot_develop("$maryたちはその空き家を調査する"),
            w.plot_develop("空き家のはずが夜には明かりが灯り、誰かが中に暮らしているのが分かる"),
            w.plot_turnpoint("$maryたちは眠らされ、気づくと縛られた状態で空き家の中にいた"),
            w.plot_resolve("知らない男が入ってきて$maryたちを助け出す"),
            w.plot_resolve("その知らない男の正体は$sherlockだった"),
            w.plot_resolve("何食わぬ顔で戻ってきた$wilsonが偽物だと見抜いていて、警察が踏み込んでくる"),
            w.plot_resolve("逮捕された$wilsonだったが、連行中に自爆して消えた"),
            )

def ch_epilogue(w: World):
    return w.chapter("エピローグ",
            w.plot_setup("一連の事件の黒幕が$morianoではなく$wilsonだったと$sherlockは語る"),
            w.plot_turnpoint("本物の$wilsonがやってくる"),
            w.plot_develop("$wilsonは既に解決した事件の正式な書簡を見せ、$sherlockに仕事を依頼しようとする"),
            w.plot_develop("事情を全て聞かされた$wilson"),
            w.plot_turnpoint("そんな$wilsonに新しい書簡が届く"),
            w.plot_resolve("勇者直系の国王が暗殺されたという"),
            w.plot_resolve("その調査を依頼されるのだ"),
            w.plot_resolve("王室からの依頼は受けないといっていたが、それが自分の兄だと知り、仕方なく出向くことになった"),
            )

def chapters(w: World):
    return (
            ch_main(w),
            ch_prologue(w),
            ch_kingdom_scandal(w),
            ch_sadness_valley(w),
            ch_red_armor(w),
            ch_blue_garnet(w),
            ch_devil_dog(w),
            ch_last_case(w),
            ch_empty_house(w),
            ch_epilogue(w),
            )

# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            "",
            # TODO
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
            *chapters(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

