# -*- coding: utf-8 -*-
'''
Stage: "通り"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   路地は基本ここで処理。家の前なども路地側なので、こちらで
#   市内の路地の多くは石畳化されている


## scenes
def baker_street(w: World):
    return w.scene("$Baker通り",
            w.plot_note("$wilsonは$carで$sherlockの家の前までやってくる"),
            w.plot_note("$wilsonは近くにいた子供（$ignes）に家を尋ねて教えてもらう"),
            w.plot_note("そこで子供たちがもめ始めて、困惑"),
            w.plot_note("なんとか場が収まり、$sherlockの家を訪問する"),
            )


def he_is_sherlock(w: World):
    return w.scene("$sherlockという男",
            w.plot_note("$sherlockは何も言っていないのに$wilsonの素性を言い当てる"),
            w.plot_note("その上で王室からの依頼は受けないと言って断る"),
            w.plot_note("最後に「さっきの子供に財布をすられてるよ」と"),
            w.plot_note("$wilsonは振り返ったがもう子供たちの姿は消えていた"),
            )


def goto_curio_dealer(w: World):
    return w.scene("古物商を訪ねて",
            w.plot_note("$sherlockは裏通りを歩く"),
            )


def later_talk_of_aily(w: World):
    return w.scene("$ailyについての後日談",
            w.plot_note("殺人の謎は改造された$gunの発見により、犯人はわからないまま、解決された"),
            w.plot_note("$sherlockは犯人はプロの人間だろうという"),
            w.plot_note("そもそも$jackと関係していたかどうか分からないし、それを追うための情報もないと"),
            w.plot_note("更に彼女があの宝剣ではなく、そこにはまっていた$stoneを売り払ったのだと分かった"),
            w.plot_note("一番大事な$stoneが偽物とわかり、どうするか問題となった"),
            )


def prince_wedding(w: World):
    return w.scene("皇太子の結婚式",
            w.plot_note("偽物の$stoneを使い、無事に皇太子の結婚式は行われた"),
            )


def mary_walked_lime(w: World):
    return w.scene("$limeを送り届ける",
            w.plot_note("$maryは彼女に$sherlockのことを謝りながら送っていく"),
            )


def meaning_for_his_advice(w: World):
    return w.scene("忠告の意味",
            w.plot_note("$sherlockは$maryになぜ自分が忠告したかについて語る"),
            w.plot_note("どう考えても妙なアルバイトは彼女をその場から離れさせるための口実だった"),
            w.plot_note("事実、店番をもう片方にまかせている間に、実際は抜け穴をずっと掘っていた"),
            w.plot_note("$ignesの監視情報から、$limeが店を離れると店を一時閉めていたと"),
            w.plot_note("その間に抜け穴を完成させ、盗み出す計画だったが、最後にその計画を知っていた$binsを殺害した"),
            w.plot_note("$limeもオーナー夫婦も質屋から離れた場所で暮らしている"),
            w.plot_note("そのアリバイを証明するだけでいいと$sherlockは言う"),
            )


def lime_and_marys_talk(w: World):
    return w.scene("$limeと$mary",
            w.plot_note("$limeも同居するようになり、$sherlockの家で暮らす人数が増えた"),
            )


def lookfor_jack(w: World):
    return w.scene("$jackを探して",
            w.plot_note("$sherlockはそのメッセージを配達した人間が$jackだと気づいて追いかける"),
            w.plot_note("見失ったが彼女が残したヒントから居場所を推測する"),
            )


def back_street(w: World):
    return w.scene("裏通り",
            )
