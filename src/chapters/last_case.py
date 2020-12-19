# -*- coding: utf-8 -*-
'''
Chapter "最後の事件"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from scenes import AbandonedHouse
from scenes import InCar
from scenes import InCity
from scenes import Market
from scenes import MorianoHouse
from scenes import SherlockHouse
from scenes import SteinHouse


# Episode
def the_fixer(w: World):
    return w.episode("事件の黒幕",
            SherlockHouse.commision_of_murder_case(w),
            InCar.goto_incident_scene(w),
            SteinHouse.case_of_house(w),
            )


def about_moriano(w: World):
    return w.episode("$morianoについて",
            SteinHouse.restrade_meets(w),
            SteinHouse.about_moriano(w),
            )


def his_warning(w: World):
    return w.episode("$morianoの警告",
            SherlockHouse.moriano_is_here(w),
            )


def lookfor_mary(w: World):
    return w.episode("$maryの捜索",
            SherlockHouse.marys_strange(w),
            Market.strange_letter(w),
            SherlockHouse.where_is_mary(w),
            InCity.goto_moriano(w),
            MorianoHouse.broken_fire(w),
            SherlockHouse.alive_moriano(w),
            )


def rescue_mary(w: World):
    return w.episode("$mary救出劇",
            SherlockHouse.morianos_whereabouts(w),
            AbandonedHouse.awaking_mary(w),
            AbandonedHouse.escape_from_danger(w),
            SherlockHouse.vanished_sherlock(w),
            )


def his_letter(w: World):
    return w.episode("$sherlockからの手紙",
            SherlockHouse.sherlocks_information(w),
            SherlockHouse.no_sherlock_life(w),
            SherlockHouse.serching_sherlock(w),
            SherlockHouse.arrived_his_message(w),
            )


def sad_news(w: World):
    return w.episode("悲しいお知らせ",
            SherlockHouse.sadness_report(w),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[6],
            # NOTE
            #   事件：研究者密室殺害事件／$moriano殺人
            #   被害者：$stein元教授／$moriano
            #   容疑者：$moriano／$sherlock
            #   犯人：$jake／$jake
            #   依頼者：$appolo（$sherlockの恩師）
            #   トリック：改造$gunにより外から遠隔操作で毒薬を打ち込み、死亡
            #   結果：$morianoが死に、姿を消した$sherlockがその重要参考人として手配された
            #   ポイント：$stone黒（$sherlockの手紙と一緒に届く）／目的は$boss復活
            w.plot_setup("孤島の事件の後、$sherlockはやたらと図書館にでかけていた"),
            w.plot_setup("事件の陰で暗躍した$cultXについては小規模の新興宗教団体として以上の情報なかった"),
            w.plot_setup("他にも四つの$stoneについて調べたり、ブラックマーケットの情報を漁ったりしていた"),
            w.plot_setup("$maryと$limeは料理を教わったり、仲良くなっていた"),
            w.plot_setup("世間では$festivalを前にして、賑わいの空気に満ちていた"),
            w.plot_setup("元研究者の謎の密室殺人事件が発生する"),
            w.plot_turnpoint("$restradeがやってきて、殺人事件の解決を依頼する"),
            w.plot_develop("$restradeから事件の概要を詳しく聞く"),
            w.plot_develop("$sherlockは研究者の家を訪れて調査する"),
            w.plot_develop("一方$maryは市場にでかけて、$sherlockに言われた言葉が気になっていた"),
            w.plot_develop("いつかは自分の将来のことを決めなければいけない、ということに悩んでいた"),
            w.plot_develop("その$maryは不思議な老人と出会う"),
            w.plot_develop("家に戻った$sherlockは$wilsonに興奮気味に$morianoについて語る"),
            w.plot_develop("$morianoは$sherlockがやっと突き止めた様々な犯罪の裏側にいる大きな黒幕だった"),
            w.plot_develop("$morianoの経歴は大学教授になり最初の論文を発表するまではすさまじい"),
            w.plot_develop("幼少期から神童と呼ばれ、十代で博士号を取得した"),
            w.plot_develop("特に数学的見地に長け、論理的に人間を動かす方法に長けていた"),
            w.plot_develop("しかしある時を境に表舞台から姿を消し、自分の研究所を作ってひっそりと暮らす"),
            w.plot_develop("そこからこの街の犯罪は複雑性をましたと$sherlockは語る"),
            w.plot_turnpoint("$maryが連れてきた老人は$morianoだった"),
            w.plot_develop("$morianoは挨拶をして、$maryに与えた飴が毒薬だと語る"),
            w.plot_develop("解毒剤は準備してあるが、$sherlockが自分について調べるのをやめるのと引き換えだと脅す"),
            w.plot_develop(""),# TODO
            w.plot_turnpoint(""),
            w.plot_turnpoint("$sherlockから手紙が届いた"),
            w.plot_resolve("手紙には$sherlockが$morianoと会う直前にその後のことを推測して書いた結末が書かれていた"),
            w.plot_resolve("手紙が届いたということは$morianoを道連れにして$sherlockも亡くなったということだと"),
            w.plot_resolve("それでも信じられない$maryは$sherlockが向かったという$morianoの別荘に向かう"),
            w.plot_resolve("しかしそこで警察の捜索隊により$sherlockの帽子が事故現場から発見された"),
            #
            w.plot_setup("$sherlockは全ての黒幕として$morianoに辿り着く"),
            w.plot_turnpoint("$morianoのメッセージ（暗号）が新聞に掲載される"),
            w.plot_develop("$sherlockが$morianoについて説明する"),
            w.plot_turnpoint("$morianoが現れる"),
            w.plot_develop("$morianoは$sherlockに全てから手を引くよう警告する"),
            w.plot_turnpoint("$maryが人質として連れ去られる"),
            w.plot_develop("$morianoの手がかりを見つけ出し、$maryの居所を見つける"),
            w.plot_turnpoint("$maryを助け出す"),
            w.plot_develop("$sherlockは$maryたちを騙して単身$morianoの隠れ家に向かった"),
            w.plot_turnpoint("$sherlockから手紙が届く"),
            w.plot_resolve("$sherlockからの最後の手紙で彼が$morianoと共に穴に落ちたことを知る"),
            the_fixer(w),
            about_moriano(w),
            his_warning(w),
            lookfor_mary(w),
            rescue_mary(w),
            his_letter(w),
            sad_news(w),
            )


