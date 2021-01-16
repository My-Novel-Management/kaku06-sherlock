# -*- coding: utf-8 -*-
'''
Chapter "魔獣"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import TITLES
from episode5 import dark_dogs_fang
from episode5 import first_murder
from episode5 import legend_of_dark_dog
from episode5 import missing_person
from episode5 import second_murder
from episode5 import sorrow_end


# Episodes
# NOTE
#   .魔獣伝説＞パーティの招待状が届く
#   .第一の殺人＞事件解決専門家が死体で発見される
#   .第二の殺人＞$mochが失踪した
#   .地下室＞地下室を発見した
#   .魔犬＞$cherryが魔犬に殺された
#   .儀式＞復活の儀式があることを知る

# NOTE: outlines
ABSTRACT = """
ある島には$bossがいた時代には沢山存在していた魔獣が今も棲んでいて人を喰らっているという。
その島にある城の城主から$sherlockの許にパーティの招待状が届く。旅行気分で$sherlockに同行する$maryたちだったが、島へのガイドを担当した地元の観光課勤務の$mochから実際に魔獣によるものと見られる連続殺人が起こっていると脅される。
城には$sherlock以外にも元刑事や新聞記者、社会学者、心霊学者、地元の歴史研究家なども呼ばれていた。更にパーティ用に料理人や使用人も雇われていた。$mochの説明では島からほとんどの住民が避難してしまった惨状をどうにかしようと、魔獣伝説にまつわるイベントを開催して、何とか観光資源にできないかという話だった。
だがその夜、社会学者の$reuiが惨殺死体で発見される。
元刑事の$hugarは独自の推理を展開し、$sherlockたちや心霊学者の$karlや地元の学者$jamosを疑う。
しかし次の日に姿を消したのは地元観光課の$mochだった。
$mochが犯人として探したが、彼は最初に魔獣伝説の発端となった殺人事件があった雑木林で無残な姿で発見された。
船は流され、海は大時化で、警察に連絡を取ることもできず、$sherlockたちは孤立する。
一方、城主の$cherryは部屋に閉じこもり、出てこなくなった。妙に思った$hugarが強引にドアを破って中に入ると、彼女の姿も消えていた。
心霊学者の$karlも失踪し、多くの人間が既に被害に遭っているのではないかという話になる。
$sherlockは$cherryの寝室に抜け道を発見し、更に談話室で地下への階段を見つける。
地下には昔の拷問部屋があったが、そこに現れたのは城主$cherryと巨大な黒い犬だった。
部屋に犬とともに閉じ込められた$sherlcok。しかし$transformした$maryにより傷つけられた黒犬は部屋を抜け出し、逃げ出した。
$cherryも後を追って姿を消したが、ようやく駆けつけた警察とともに捜索した結果、黒犬に食われて亡くなっているところが発見され、黒犬は警察により射殺された。
事件後、地下の別の部屋から、復活の儀式を行った跡が発見された。黒犬は闇の技法により蘇った闇の生き物だったのだ。$cherryはそれを維持するために人を殺してその肉を与えたいたのだと分かった。
"""

# NOTE: charas
#   ・$cherry（ここのみ。城主。真犯人
#   ・$moch（ここにみ。観光協会の人間。共犯者

# NOTE: stages
#   ・地方（ダートムーア。ここのみ。原作とは異なり、南西部の海に浮かぶ孤島に設定
#   ・$baskervilles家（ここのみ？

# NOTE: items
#   ・$black_stone（話だけ。$baskervilles家の所有物だったが闇オークションに出されて行方不明　→？

# NOTE: case
#   ・魔犬伝説の猟奇殺人　→当時の魔術の失敗による自殺
#   ・孤島事件第一の殺人（犯罪研究家）　→$moch。最初から観光を盛り上げるための事件と割り切り計画していた
#   ・孤島事件第二の殺人（観光課の$moch）　→$cherry。仲間割れと口封じ（当初から殺す計画
#   ・孤島事件第三の殺人（霊能者）　→$cherry。犯行現場を見られた

# NOTE: tech
#   ・通信技術（モールス信号？）


# Chapter
def main(w: World):
    return w.chapter(TITLES[5],
            # NOTE
            #   事件：犬による猟奇殺人／孤島の招待客連続殺人
            #   被害者：数名の地域の人／
            #   容疑者：伝説の魔犬
            #   犯人：$cherry（犬の餌として必要だった）
            #   依頼人：城主の$cherry
            #   トリック：偽装（歯型の凶器を使い、犬がやったように見せかけた
            #   結果：二人が死亡（うち一人は共犯）、城主の$cherryは飼い犬に食い殺され、魔犬は射殺
            #   ポイント：蘇りの$sorcery／$stone黒の行方情報（闇オークションに出回った）
            legend_of_dark_dog.main(w),
            first_murder.main(w),
            missing_person.main(w),
            second_murder.main(w),
            dark_dogs_fang.main(w),
            sorrow_end.main(w),
            outline=ABSTRACT)


