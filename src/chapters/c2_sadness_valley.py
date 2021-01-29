# -*- coding: utf-8 -*-
'''
Chapter "悲しみの谷"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from episode2 import family_circumstances
from episode2 import marys_confession
from episode2 import real_mind
from episode2 import sad_case
from episode2 import suspect_mary
from episode2 import valley_town


# Episodes
# NOTE
#   .依頼＞$trainで目的地に
#   .事件について＞$maryと面会可能になる
#   .$maryとの面会＞$maryは$animal
#   .家族の話＞$maryが連れてこられる
#   .母と娘＞使用人$kailが本性を現して人質を取る
#   .事件の顛末＞$maryが同居人に

# NOTE: outlines
ABSTRACT = """
$wilsonは聞いてもらえなかった依頼をしようと再び$sherlock宅を訪れる。$sherlockは相変わらず$wilsonの話に聞く耳を持たず、新聞記事にあった父親殺しの悲しい事件について感想を述べる。
そこにちょうどその事件の関係者である使用人の$keanがやってきて、$sherlockに事件の容疑者になってしまった娘$maryの容疑を晴らして欲しいと依頼した。
$sherlockは現場に赴いて調査を行う。
$maryと面会し、$sherlockは証言だけでなく彼女が$animalであることが容疑を決定付けていると語る。
しかし更に調査を進めると$jeanと$kailの関係が$jeanが$royd氏と結婚するより遥か以前にあり、莫大な遺産の相続権が娘の$mary一人になりそうだったという事情が判明する。
$sherlockは最新の指紋検出技術を用いて凶器となった$gunから$jeanと$kailの指紋のみが検出されたことで、二人を追い詰める。
$kailが自分一人だけでやったと$jeanを人質に取るが、$transformした$maryにより阻止され、事件は解決した。
後日、遺産相続権を放棄し、邸宅も地元に寄付をした$maryが、荷物を持って$sherlock宅に押しかけた。
"""

# NOTE: charas
#   ・$mary（初出。最初は怯えて寡黙になっているただの少女。あとで印象変わる
#   ・$jean（ここのみ。$mary母
#   ・$kail（ここのみ。使用人。$keanの父
#   ・$kean（ここのみ？使用人
#   ・$patson（初出。地元の刑事。後に本庁に取り上げられる。もともと$cultX信者

# NOTE: stages
#   ・西部の田舎町（原作のボスコム谷。ここでも沼地。ただ特殊な鉱石が採掘できるのでそれで一部が儲けていた

# NOTE: items
#   ・魔導列車（初出？

# NOTE: case
#   ・父親殺し事件　→偽装で、本当は遺産目当ての妻と、幼馴染の使用人の共犯

# NOTE: tech
#   ・凶器を使った人間を探すために最新技術の「指紋鑑定」を使う
#   ・魔導列車


# Chapter
def main(w: World):
    return w.chapter(TITLES[2],
            # NOTE
            #   事件：$gunによる目撃者のいない殺人
            #   被害者：地元の名士$royd氏
            #   容疑者：$mary
            #   犯人：家の使用人の$kail（共犯としての$jean）
            #   依頼人：家の使用人の息子の$kean
            #   トリック：アリバイ偽装（偽証と指紋偽装）
            #   結果：共犯として母親が逮捕され、$maryが遺産を独り占めすることになった
            #   ポイント：$animalの存在示唆／改造$gun
            sad_case.main(w),
            valley_town.main(w),
            suspect_mary.main(w),
            family_circumstances.main(w),
            marys_confession.main(w),
            real_mind.main(w),
            outline=ABSTRACT)


