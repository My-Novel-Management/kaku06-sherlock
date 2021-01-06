# -*- coding: utf-8 -*-
'''
Chapter "プロローグ"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import ReadingRoom
from scenes import WilsonHouse


# Episodes
# NOTE
#   .問題はいつも山積み＞便利屋$sherlock
#   .便利屋$sherlock＞$sherlockの家の前までやってきた
#   .注意書き

# NOTE: outlines
ABSTRACT = """
ある長旅から戻った$wilsonは行きつけの酒場で昔の知人$stanと出会う。戦争から戻ってきた軍医で、$wilsonが抱えているある案件で困っていると話すと、偏屈だが難解な事件解決を得意としている便利屋$sherlockを紹介された。$wilsonは翌朝、準備をしてその男が住むという$Baker街に向かう。
※作品本編に入る前に、この物語が全て三人称で記述され、一連の事件が終焉を迎えた後に情報を補完し、読みやすく小説として書き直したものだ、と注意書きがなされる
"""
OUTLINES = [
"""
遥か昔に$bossが倒されて平和になったはずの世界。$science技術により産業革命が起こる変革期だった。$wilsonは王室から第二王女失踪の調査を依頼され、困っていた。
行きつけの酒場で旧知の元軍医$stanと再会し、彼から便利屋$sherlockという男を教わる。翌日、$sherlockに仕事を依頼しようと彼の家を訪れるのだが。
その出会いが、やがて大きな事件に関わることに繋がっていた。
""",
"""
※記述者視点となる。本作は全ての事件に一応の解決が見られてから伝聞により情報を補完し、小説として再構成されたことが注記される。
"""
        ]

# NOTE: charas
#   ・$wilson（偽物。）
#   ・$sherlock（$stanから話を聞くだけ。１話まで顔出しなし）
#   ・$stan（$wilsonの知人。ここだけ？）

# NOTE: stages
#   ・$wilson家（かなり後で引っ越すが、それまではここしか触れられない）
#   ・行きつけのバー

# NOTE: items
#   ・骨董品の杯（$boss杯。初出だが、こそっと。これが重要な祭具

# NOTE: case
#   ・？

# NOTE: tech
#   ・照明（入り口はガス灯だが、中に$enagy式灯を使っている
#   ・魔導車（次も

def troublesome(w: World):
    return w.episode("厄介事と便利屋",
            # NOTE
            #   ・数日前の大地震で、大聖堂の一部が破損し、改修中になっている
            #   ・魔導冷蔵庫により$scienceによる技術革命が起こっている世界と提示（1850年頃に商業用冷蔵庫があったが一部のみだった
            #   ・一部で戦争があること提示（米南北戦争など
            #   ・$cultXの男が世界平和を訴えている
            w.plot_setup("$wilsonは王室からの依頼を引き受けるエージェントで、第二王女失踪の調査中だった"),
            w.plot_note("遥か昔に$bossが$heroによって倒され、世界に平和が取り戻された（はず）世界"),
            w.plot_note("$scienceにより夜でも明るい街"),
            w.plot_note("$science技術により、$car等も走っている"),
            w.plot_note("駅があり、$trainが$lightを放って走っている"),
            w.plot_note("情報入手のために馴染みのパブを訪れる$wilson"),
            w.plot_note("パブは色々な人間、人種が混ざり合い、飲んでいる"),
            w.foreshadow("客の中には明らかに人間ではない者も潜んでいる", flagname="$ajin"),
            w.foreshadow("男たちがこっそり紙包みを取引きしている", flagname="$gun"),
            w.plot_turnpoint("馴染みのパブで$wilsonは旧知の元軍医$stanに声を掛けられる"),
            w.plot_develop("$wilsonと$stanは互いの近況を語り合い、お互いに苦労症だと苦笑し合う"),
            w.plot_note("$stanは戦争帰り（大陸の方で大きな戦争が終わっで間もない）"),
            w.plot_note("$wilsonと$stanは王立大学の同期生で、共通の知人がいる"),
            w.plot_note("医学を中心に学んだ$stanと文学を中心に学んだ$wilsonだったが、共通の知人を通じて親交があった"),
            w.plot_note("$stanは帰国後、開業医をすることが決まっているが、場所などは今決めているところ"),
            w.plot_note("$wilsonは公務員だが、主に王室からの面倒な依頼を処理するエージェントという役回り"),
            w.plot_note("この半年ほどの間に謎の失踪事件が相次いでいる"),
            w.plot_note("人が失踪するのは珍しいことじゃない、と$stan"),
            w.plot_note("$wilsonは内緒だが、と断り、第二王女も失踪したと伝える"),
            w.foreshadow("互いに互いを「変わったな」と言う", flagname="偽$wilson"),
            w.plot_turnpoint("旧知の元軍医$stanから難事件をいくつも解決している便利屋$sherlockという男の情報を得る"),
            w.plot_resolve("$wilsonは$sherlockに依頼するため、彼の家を訪れた"),
            w.plot_note("$sherlockという名前は耳にしたことのない$wilson"),
            w.plot_note("とにかく一度会えばその特異性が理解できると、$stan"),
            w.plot_note("$stanとまた一緒に飲もうと約束して、$wilsonは別れる"),
            w.plot_note("翌日、$carを準備して、$sherlockの家を訪ねることにした"),
            outline=OUTLINES[0])


def note_for_novel(w: World):
    return w.episode("読者のための諸注意",
            # NOTE
            #   ・事件が全て終わっている
            #   ・三人称で記述する（作中人物の記述者がいる
            w.plot_setup("（記述者視点に切り替わり）一連の事件が全て片付いた後で書かれていると注記される"),
            w.plot_note("”私”という一人称で、ここは書かれる"),
            w.plot_note("本作が「私と$sherlockの出会い」によって書かれた"),
            w.plot_develop("作中は記述者を含めて原則三人称で書かれ、情報は不足していた部分を伝聞によって補い、小説にする時に補足して書かれている"),
            w.plot_note("全ての情報が補完されている訳ではないが、ある程度、その当時の状況も踏まえて作中で再現されている"),
            w.plot_note("原則時系列順に並べて書かれている"),
            w.plot_resolve("$sherlockとの出会いによって記述者の世界は大きく変わり、その後の人生も左右するほどの人生の変化があった"),
            w.foreshadow("自分を含めて全て三人称で記述する、という注意書き", flagname="記述者"),
            outline=OUTLINES[-1])


# Chapter
def main(w: World):
    return w.chapter(TITLES[0],
            troublesome(w),
            note_for_novel(w),
            outline=ABSTRACT)

