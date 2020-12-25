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
from scenes import Market
from scenes import School
from scenes import SherlockHouse
from scenes import Street


# Episodes
# NOTE
#   .市場のガチョウ＞ガチョウからナイフと宝石が出てくる
#   .凶器のない殺人＞市場の$nowlisや$jackが容疑者となる
#   .ガチョウクラブ＞$maryが捕まる
#   .事件捜査＞$jackが$maryを助ける
#   .事件解決＞$sherlockが$jackとの交換条件を飲む
#   .四つの$stone＞$jackから青$stoneを預かる

# NOTE: charas
#   ・（ここのみ。ガチョウクラブ会員
#   ・$hornet（ここにみ。ガチョウ卸問屋。容疑者の一人
#   ・$peter（ちょい出演役。ガードマン

# NOTE: stages
#   ・$moura（ここのみ。事件被害者

# NOTE: items
#   ・ナイフ（凶器
#   ・$blue_stone（$jackが盗んだものだが、最終的に$jackから$sherlockに預けられる

def market_and_goose(w: World):
    return w.episode("市場とガチョウ",
            w.plot_setup("$limeが同居するようになり、$limeが料理や家事を担当するように変化する"),
            w.plot_setup("$maryは自分の居場所が失われたような気持ちになる"),
            w.plot_setup("$maryは市場への買い出し役しかなくなった"),
            w.plot_develop("$maryは肉屋の$nowlisからガチョウをもらう"),
            w.plot_turnpoint("ガチョウの中から青い宝石と血のついたナイフが一緒に出てきた"),
            )


def missing_murder_weapon(w: World):
    return w.episode("凶器のない殺人",
            w.plot_turnpoint("$jackが殺人事件の容疑者に浮上した"),
            )


def goose_club(w: World):
    return w.episode("ガチョウクラブ",
            w.plot_setup("容疑者として$jackが陰で指名手配"),
            w.plot_setup(""),
            w.plot_turnpoint("$maryは市場の知人の容疑を晴らそうと独自に調査する"),
            w.plot_turnpoint("$maryが帰ってこなかった"),
            )


def investigate_case(w: World):
    return w.episode("事件捜査",
            w.plot_turnpoint(""),
            )


def case_end(w: World):
    return w.episode("事件解決",
            w.plot_turnpoint("女警官は$jackだった"),
            )


def four_stones(w: World):
    return w.episode("四つの$stone",
            w.plot_resolve("$jackから$blue_stoneを託された"),
            )


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
            w.plot_setup("$limeが新しい同居人になり、料理は彼女の担当となっていた"),
            w.plot_setup("自分の居場所が危うくなったと感じた$maryは空回りしては失敗してしまう"),
            w.plot_setup("落ち込んで買い物にでかけた$maryを見て、肉屋の$nowlisがもらったガチョウを安く売ってくれる"),
            w.plot_setup("$sherlockは第二王女を発見し$wilsonからの依頼を達成したものの、まだ失踪事件について調べていた"),
            w.plot_setup("$hornet夫人殺害事件が発生していたが、その凶器が発見されていないと謎になっていた"),
            w.plot_turnpoint("ガチョウの中から袋に入った血付き小型のナイフと青い宝石が出てくる"),
            w.plot_develop("$sherlockはナイフを世話になっている鑑識官$edoに見せて調べてもらう"),
            w.plot_develop("そのナイフが$hornet夫人殺害の凶器と判明"),
            w.plot_develop("また同時に付いていた血が$jackと同一だと分かる"),
            w.plot_develop("$jackが極秘に警察の指名手配になる"),
            w.plot_turnpoint("$maryは自分がガチョウをもらったことで肉屋の$nowlisが重要参考人になっていると知り、独自に調査を開始する"),
            w.plot_develop("卸業者を当たる$mary。そこでガチョウクラブの存在を知る"),
            w.plot_develop("ガチョウクラブは毎月定額でガチョウを届けてくれる集まりだったが、友人紹介システムなど怪しいところがあった"),
            w.plot_develop("$maryはガチョウクラブの勧誘に会い、抜け出せなくなる"),
            w.plot_develop("そこを通りかかった$limeに助けられる"),
            w.plot_turnpoint("もらったガチョウの中から盗まれた宝石が出てくる"),
            w.plot_develop("一方$sherlockは青$stoneについて図書館に調べにきていた"),
            w.plot_develop("$stoneはかつて活躍した$heroたちの持っていた武器についていたものだと分かる"),
            w.plot_develop("四つの$stoneは次に$bossが復活した時に必ず必要になるとされ、厳重に保管されているはずだった"),
            w.plot_develop("$sherlockに近づいてきた女司書から、その$stoneが権力の象徴となり、多くの人間の手を渡って今に至ることを説明される"),
            w.plot_turnpoint("$sherlockの前に$jackが現れる"),
            w.plot_develop("$jackは自分が何も関係していないことを証明して、無実を晴らしてほしいと頼む"),
            w.plot_develop("こうなったのも自分が青$stoneを持っていたためで、それを預けるとも"),
            w.plot_develop("もし依頼を達成したら、本当に困った時に必ず助けになると約束した"),
            w.plot_develop("また$jackは最近アンダーグラウンドで不穏な動きがあり、大きな勢力が動いていると忠告する"),
            w.plot_turnpoint("$maryが失踪したと$limeから連絡が入る"),
            w.plot_develop("$sherlockは$limeから事情を聞き、すぐに犯人の目星をつける"),
            w.plot_develop("手配して、ガチョウクラブに警察を向かわせる"),
            w.plot_develop("$hornet夫人もガチョウクラブの会員だと分かり、事件の証拠を掴んだ$maryが殺される恐れがあると"),
            w.plot_develop("犯人が逃げていた家に侵入し、$maryを助け出す"),
            w.plot_develop("$limeが襲われそうになったところを$maryが獣化して助けた"),
            w.plot_turnpoint("$hornet夫人がガチョウクラブというネズミ講のチームの一員で、殺人は仲間割れだったことが判明した"),
            w.plot_resolve("$sherlockの兄がやってきて、ガチョウクラブの会員だったがそれが突如閉会になり、いわくつきのガチョウを持って訪れた"),
            w.plot_resolve("兄は$sherlockを説得していたが、話し合いは不調に終わった"),
            w.plot_resolve("$sherlockは青$stoneを兄に預けた"),
            #
            market_and_goose(w),
            missing_murder_weapon(w),
            goose_club(w),
            investigate_case(w),
            case_end(w),
            four_stones(w),
            )


