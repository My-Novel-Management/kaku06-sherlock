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
            outline=OUTLINES[0])


def note_for_novel(w: World):
    return w.episode("読者のための諸注意",
            # NOTE
            #   ・事件が全て終わっている
            #   ・三人称で記述する（作中人物の記述者がいる
            outline=OUTLINES[-1])


# Chapter
def main(w: World):
    return w.chapter(TITLES[0],
            troublesome(w),
            note_for_novel(w),
            outline=ABSTRACT)

