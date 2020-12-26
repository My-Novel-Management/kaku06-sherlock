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
OUTLINES = [
        "行きつけのバーにきていた$wilsonは旧知の$stanと出会う。厄介事を抱えて悩んでいた$wilsonに彼は便利屋$sherlockという男を紹介する",
        "この半年ばかりで発生している謎の失踪事件。その中のある人物について調査を依頼しようと、$wilsonは$sherlock宅を訪れた",
        "※記述者視点になり。本書が全てが終わった後で情報を伝聞により補完し書かれたことと、全て三人称で書かれていることを提示",
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


def troublesome(w: World):
    return w.episode("厄介事",
            # NOTE
            #   ・数日前の大地震で、大聖堂の一部が破損し、改修中になっている
            #   ・魔導冷蔵庫により$scienceによる技術革命が起こっている世界と提示（1850年頃に商業用冷蔵庫があったが一部のみだった
            #   ・一部で戦争があること提示（米南北戦争など
            #   ・$cultXの男が世界平和を訴えている
            w.plot_setup("$scienceにより夜でも明るい街"),
            w.plot_setup("$bossが$heroによって倒され、世界は人間が溢れていた"),
            w.plot_setup("それでも問題は山積で、$wilsonはそんな問題に頭を悩ませている一人"),
            w.plot_develop("$wilsonは馴染みのバーに立ち寄る"),
            w.plot_turnpoint("$wilsonに声をかける$stan"),
            w.plot_develop("$wilsonは今時分が王室から色々と頼まれて厄介事を解決する部署にいると話す"),
            "お互いに雰囲気が変わった、と話す",
            w.plot_turnpoint("知人の$stanから便利屋$sherlockのことを教わる"),
            w.plot_resolve("翌日に$sherlockの家を訪ねようと考えて、店を出る"),
            w.plot_resolve("店を出たところで宗教の男からビラをもらう。$bossが消えても世界から驚異は消えないと訴え"),
            outline=OUTLINES[0])


def handyman_sherlock(w: World):
    return w.episode("便利屋$sherlock",
            # NOTE
            #   ・ここいらないかも？
            w.plot_setup("翌朝、$sherlockの家に向かう$wilson"),
            w.plot_setup("$sherlockの家は$Baker街にある"),
            w.plot_develop("$carを準備して、$sherlockの家に向かう"),
            w.plot_develop("産業革命が起こり、街は急成長している"),
            w.plot_develop("ただところどころに旧時代の名残がある"),
            w.plot_turnpoint("$carから降りると子供たち（$ignes）に囲まれる"),
            w.plot_develop("$wilsonは"),
            w.plot_turnpoint("何とか$sherlockの家のドアをノックした"),
            w.plot_resolve("$ignesたちを何とか追い払い、$sherlockの家のドアをノックした"),
            outline=OUTLINES[1])


def note_for_novel(w: World):
    return w.episode("作品のための注意書き",
            # NOTE
            #   ・事件が全て終わっている
            #   ・三人称で記述する（作中人物の記述者がいる
            "一旦話を切って、前設定的な説明を（叙述トリック用）",
            w.plot_setup("これは「私」が$sherlockという実に偏屈で素晴らしい人物と出会った記録である"),
            w.plot_setup("「この世界」は$bossが退治され、世界に平和が取り戻されたはずの世界"),
            w.plot_setup("そこでも多くの事件が起こり、犠牲者が跡を絶たない"),
            w.plot_develop("作中では様々な事件が起こる"),
            w.plot_develop("犠牲者も何人か出る"),
            w.plot_turnpoint("全ての事件に一旦の決着がついてから、これを書いている"),
            w.plot_resolve("全ての事件が一旦落ち着いた後に情報を整理して物語に仕立てている"),
            w.plot_resolve("$sherlockに$heroについて尋ねると「$heroは幻想で、本当は沢山の人の犠牲によって結果が得られている。$heroの必要ない世界がそこまできているのに、まだ$heroの話を持ち出す必要ない」と"),
            "物語全体のイメージを決める小言。また現代人であるっぽいふり",
            outline=OUTLINES[2])


# Chapter
def main(w: World):
    return w.chapter(TITLES[0],
            w.plot_setup("$wilsonは王室からいろいろな厄介事を頼まれる存在"),
            w.plot_turnpoint("最近続いている謎の失踪事件の調査を頼まれる"),
            w.plot_develop("新聞を見ながら趣味でやっている日記を書き始める"),
            w.plot_turnpoint("$sherlockという男が街の便利屋という噂を知ったところから物語は始まる"),
            w.plot_resolve("$sherlockの家を訪問する$wilson"),
            #
            troublesome(w),
            handyman_sherlock(w),
            note_for_novel(w),
            )


