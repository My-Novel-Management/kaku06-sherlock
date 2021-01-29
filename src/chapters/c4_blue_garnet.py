# -*- coding: utf-8 -*-
'''
Chapter "青いガーネット"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from episode4 import case_end
from episode4 import four_stones
from episode4 import goose_club
from episode4 import investigate_case
from episode4 import market_and_goose
from episode4 import missing_murder_weapon


# Episodes
# NOTE
#   .市場のガチョウ＞ガチョウからナイフと宝石が出てくる
#   .凶器のない殺人＞市場の$nowlisや$jackが容疑者となる
#   .ガチョウクラブ＞$maryが捕まる
#   .事件捜査＞$jackが$maryを助ける
#   .事件解決＞$sherlockが$jackとの交換条件を飲む
#   .四つの$stone＞$jackから青$stoneを預かる

# NOTE: outlines
ABSTRACT = """
$limeも同居するようになり$sherlockの周囲に賑やかな日常がやってきた。ただ$limeは$maryとは異なり、家事全般器用にこなし、$sherlockとしては非常に助かる存在になっていた。そのことが$maryには気がかりで、自分の無力さに情けなくなり、市場で仲良くなった肉屋の$nowlisに愚痴っていた。$nowlisはそんな$maryに沢山貰ったからとガチョウを一羽プレゼントしてくれる。
だが家に戻り、$maryはそのガチョウを$limeに捌いてもらったところ、中からナイフと$blue_stoneが出てきた。
警察に届けるとそのナイフに付着していた血液が、凶器が発見されていない殺人事件の被害者のものと一致するということが判明し、ガチョウを渡した$nowlisが容疑者の一人になってしまった。
$maryは容疑を晴らすために一人で事件の調査を開始する。調査の過程でガチョウクラブが浮上し、被害者がガチョウクラブ会員だったことが分かる。
しかしそのクラブが実は$drag密売の為の組織で、取引現場を目撃してしまった為に$maryは捕まってしまう。
$limeは$maryが戻ってこないことを妙に思い、探しに出る。$sherlockは$ignesたちに指示して$maryがどこにいったか探してもらう。その一方で自分は事件調査に乗り出した。
$ignesたちの情報で$maryがガチョウクラブに捕まったことが分かり、$limeは単身、彼女を助けに乗り込む。危うく二人とも殺されそうになるが、そこに警察が突入し、事なきを得た。$sherlockが指示したものだった。
一方、$sherlockは$blue_stoneが$jackによって隠されたものだと分かり、それを取り戻しにきた$jackと出会う。彼女から四つの$stoneが存在することを知らされ、何者かにより企まれていることを阻止して欲しいという依頼をされ、$blue_stoneを預かった。
"""


# NOTE: charas
#   ・（ここのみ。ガチョウクラブ会員
#   ・$hornet（ここにみ。ガチョウ卸問屋。容疑者の一人
#   ・$peter（ちょい出演役。ガードマン

# NOTE: stages
#   ・$moura（ここのみ。事件被害者

# NOTE: items
#   ・ナイフ（凶器凶
#   ・$blue_stone（$jackが盗んだものだが、最終的に$jackから$sherlockに預けられる

# NOTE: case
#   ・ガチョウの中からナイフと$blue_stoneが出てくる　→$blue_stoneは$jackが逃げる最中に隠した／ナイフは殺人犯が凶器を慌てて隠した
#   ・$moura夫人殺人事件（凶器が見つからない　→ガチョウの中のナイフで$jack容疑者　→ガチョウクラブの仲間割れで殺された。$jackは無関係

# NOTE: tech
#   ・


# Chapter
def main(w: World):
    return w.chapter(TITLES[4],
            # NOTE
            #   事件：$hornet夫人殺害／ガチョウから凶器（ナイフ）と$stone青が出てくる
            #   被害者：$hornet夫人
            #   容疑者：$jack／配管工や卸問屋の男
            #   犯人：$stoneは$jack／殺害は旦那
            #   依頼人：$mary（市場の知人が容疑者の一人に）／$jack（自分が容疑者になった）
            #   トリック：消失する凶器（ガチョウの中に隠す）→実は偽装で、容疑を$jackにかけるため
            #   結果：痴情のもつれから夫人の間男（ガチョウクラブ主催）が行ったもので、$jackの偽装は闇オークションに出回っていたものを利用
            #   ポイント：$stone青／$jackへの恩（最後の事件後匿ってもらう）
            #   サブ：$maryと$limeの仲が深まる（二人で探索＆調査）
            market_and_goose.main(w),
            missing_murder_weapon.main(w),
            goose_club.main(w),
            investigate_case.main(w),
            case_end.main(w),
            four_stones.main(w),
            outline=ABSTRACT)


