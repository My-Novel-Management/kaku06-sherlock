# -*- coding: utf-8 -*-
'''
Chapter "皇太子の醜聞"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from episode1 import about_aily
from episode1 import handyman_sherlock
from episode1 import murder_case
from episode1 import orphanages_lady
from episode1 import prince_matter
from episode1 import prince_wedding


# Episodes
# NOTE
#   .皇太子の依頼＞書簡到着
#   .謎の女＞遺体発見
#   .密室殺人＞容疑者$aily
#   .女と孤児院＞$ailyは死んでいた
#   .怪盗$jack＞宝剣を取り戻した
#   .皇太子の結婚式

# NOTE: outlines
ABSTRACT = """
$wilsonは便利屋$sherlockを訪ねてある依頼をしようとする。しかし$sherlockは$wilsonが話をする前に全てを推理で言い当て、挙げ句に「王室からの依頼は受けない」と断ってしまう。
だがそこに王室付きの秘書$adelがやってきて王子からの依頼の書簡を渡すと、その依頼は引き受けてしまった。
王子の依頼は結婚式に必要なので、オペラ歌手$ailyにプレゼントしてしまった$royalswordを取り戻して欲しいというものだ。$sherlockと$wilsonは$ailyの家に向かうが、そこで謎の女性の死体を発見する。
$aily宅で起こった密室殺人に興味を持った$sherlockは事件を調べていくが、それはやがて巷で噂になっている怪盗$jackへと繋がっていた。
$jackから、$ailyが自殺だったことを聞き、彼女を利用して$royalswordを盗んだが、$sherlockに全てバレてしまったので素直に返却すると申し出があった。
無事に$royalswordを取り戻したはずだったが、そこには肝心の$red_stoneが付いておらず、$jackに出し抜かれた$sherlock。
王子の結婚式は宝石技師$casselの手による偽物の$stoneを使って何とか無事に終わらせた。
"""

# NOTE: charas
#   ・$sherlock（顔出しなど初めて。格好、特に帽子や姿勢を詳しく描写。ロリポップを咥えている
#   ・$restrade
#   ・$aily（$jack
#   ・$adel（初出。$mikelの秘書だが中盤まで内緒。王室からの依頼に訪れる人
#   ・皇太子（名前のみ。結婚式で遠くから姿は見える

# NOTE: stages
#   ・London（都市。説明はここで簡単にする
#   ・Baker街（主要舞台。プロローグ初出。ここで結構書いておく
#   ・$sherlockの家（初出。主要舞台になるのでしっかり描く
#   ・サーペント通り（作中はStJhonsWood。ここのみ？$Baker街から北西の地域
#   ・$aily家（殺人事件現場。ここのみ
#   ・$EastEnd（スラム街。ちょろっとだけ出す
#   ・孤児院（初出。ほぼここだけ

# NOTE: items
#   ・宝剣（ここのみ
#   ・$red_stone（初出。$stoneの存在をちら見せ

# NOTE: case
#   1.皇太子の宝剣を取り戻す　→$jackから返してもらったが$stoneが付いてなかった
#   2.密室殺人（$aily家で謎の女性の死体発見　→$ailyは自殺だった

# NOTE: tech
#   ・犯人探しのために「血液鑑定」を使う。これは冒頭で$sherlockが研究しているもの
#   ・魔導車


# Chapter
def main(w: World):
    return w.chapter(TITLES[1],
            # NOTE
            #   事件：密室殺人
            #   犠牲者：謎の女性　→本物の$aily
            #   容疑者：不明　→$aily
            #   犯人：自殺
            #   トリック：偽装（密室殺人に見せかけた自殺
            #   依頼人：皇太子
            #   結果：宝剣を取り戻したが肝心の$stoneは付いていなかった
            #   ポイント：$science技術／毒薬／$jack／$stone赤／王室
            handyman_sherlock.main(w),
            prince_matter.main(w),
            murder_case.main(w),
            about_aily.main(w),
            orphanages_lady.main(w),
            prince_wedding.main(w),
            outline=ABSTRACT)
