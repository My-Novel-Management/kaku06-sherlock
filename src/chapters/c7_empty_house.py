# -*- coding: utf-8 -*-
'''
Chapter "空き家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from episode7 import adventure_of_empty_house
from episode7 import he_is_back
from episode7 import lookfor_sherlock
from episode7 import one_mans_confess
from episode7 import revive_boss
from episode7 import total_the_end


# Episode
# NOTE
#   .$sherlockを探して＞$sherlockを空き家で見たという情報が入る
#   .空き家の冒険＞空き家の殺人事件の容疑者に$sherlock
#   .$maryの探検＞$maryが捕らえられた
#   .彼が戻ってきた＞$sherlockが戻ってきた
#   .$boss復活＞祭壇は大爆発した
#   .偽$wilsonの思惑＞偽$wilsonは山小屋で自殺しているのが見つかった

# NOTE: outlines
ABSTRACT = """
$sherlockが滝に落ちて行方不明になってから三ヶ月、未だに生存の証拠は見つからなかった。
$maryも$limeもそれぞれアルバイトを探し、$maryは市場で手伝いを、$limeは守衛のアルバイトをしつつ、$sherlockの情報を集めていた。
ある日、$wilsonが$sherlockを見かけたという情報を持ってくる。
$maryたちは$sherlockに似た男が暮らしているというその空き家を監視する。夜になり、後ろ姿が$sherlockに似た男がその空き家に入り、明かりが灯る。本を読む様は確かに$sherlockを思わせたが、そこに来客があり、しばらく後に揉めている様子が伝わり、明かりが消えた。
そこから何も音がしなくなったので、$maryたちが空き家を調べに行くと、そこで知らない男が亡くなっていた。
$sherlockが容疑者として浮上し、警察は$maryたちに事情聴取する。
$maryは$sherlockの容疑を晴らすために空き家を調べる。抜け道を見つけ、それを辿っていくと廃工場に出た。そこで今までに失踪した多くの人の遺体が転がっているのを目撃する。
だが何者かによって意識を失った。
気づいた$maryが見たのは$sherlockで、彼は今までの事件は全て自分がやったと告白する。衝動が押さえられなくなり犯行に及んでしまう、一種の病気だった。
$maryは$sherlockを信じて庇おうとするが、彼は$maryを殺そうとする。
そこをホームレスの男が助ける。彼こそが本物の$sherlockだった。警察がかけつけ、偽物の$sherlockこと連続猟奇殺人事件の犯人$jakeを捕まえる。
負傷した$maryは入院する。
これで全て解決かと思ったが、$sherlockは$limeたちにまだ解決していないと言う。
病院の$maryから$blue_stoneを返してもらう必要があると言い、病院に向かったが、$maryは$patsonにより連れ出された後だった。
改装中の大聖堂の地下、そこでは$patsonが$boss復活の儀式の準備をしていた。
$sherlockは$maryを助け出すためにやってきたが、$patsonは$sherlockの血と交換だと言う。何故ならずっと探していた$heroこそが$sherlockだったからだ。その血が儀式に必要だった。
$sherlockは$maryを助けるために血を盃に注ぐ。それにより四つの$stoneと$heroの血が揃い、儀式が始まる。
だが$blue_stoneが偽物だった為に儀式は失敗し、地下のホールは大爆発した。$jackが渡した$stoneが偽物だったのだ。
そこで$patsonは$wilsonに泣きつくが、$wilsonは$patsonを撃ち殺した。彼こそが本当の黒幕、闇の世界から$boss復活のためにやってきた$zeronだった。
$sherlockはそのことに気づいていて、$wilsonの計画が失敗するように敢えて偽物だと分かって儀式を行わせた。
逃げ出した偽$wilsonは、後日、山中の山小屋で自殺しているのが発見された。$zeronの死により、全ての関連が断たれ、$boss復活にかかわる一連の事件は終焉を迎えた。
"""


# NOTE: charas

# NOTE: stages
#   ・大聖堂（中は初出
#   ・イーストエンド（スラム街。少し扱ってきたが本格的はここで
#   ・空き家（事件に使われる場所。ここのみ
#   ・抜け道（EE内に数多くある、地下道の一つ。ここのみ
#   ・廃工場（EE内にいくつもある。ここのみ

# NOTE: items
#   ・$red_stone
#   ・$blue_stone
#   ・$white_stone
#   ・$black_stone
#   ・$bossの杯
#   ・$bossのドクロ（大聖堂の地下に厳重に保管されていたはずのもの

# NOTE: case
#   ・空き家殺人事件　→失踪者の一人の遺体を放置し、$sherlockに容疑が向かうようにした。実行犯は$jake

# NOTE: tech
#   ・


# Chapter
def main(w: World):
    return w.chapter(TITLES[7],
            # NOTE
            #   事件：空き家密室殺人／連続失踪事件
            #   被害者：$ronald卿
            #   容疑者：$sherlock
            #   犯人：$jake（$sherlockに似た$ajin）
            #   依頼者：$wilson？
            #   トリック：偽装トリック（争ったように見せかけて遺体を部屋に置いた）＆抜け道を使った密室
            #   結果：$jakeを殺して事件解決
            #   ポイント：連続失踪事件の犯人／$boss復活の儀式とその失敗
            lookfor_sherlock.main(w),
            adventure_of_empty_house.main(w),
            one_mans_confess.main(w),
            he_is_back.main(w),
            revive_boss.main(w),
            total_the_end.main(w),
            outline=ABSTRACT)


