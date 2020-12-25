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
from scenes import Bar
from scenes import BasementInCastle
from scenes import BedroomInCastle
from scenes import Church
from scenes import InShip
from scenes import InTrain
from scenes import Island
from scenes import Library
from scenes import LoungeInCastle
from scenes import OldCastle
from scenes import Port
from scenes import SherlockHouse
from scenes import Station
from scenes import Street


# Episodes
# NOTE
#   .魔獣伝説＞パーティの招待状が届く
#   .第一の殺人＞事件解決専門家が死体で発見される
#   .第二の殺人＞$mochが失踪した
#   .地下室＞地下室を発見した
#   .魔犬＞$cherryが魔犬に殺された
#   .儀式＞復活の儀式があることを知る

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

def legend_of_dark_dog(w: World):
    return w.episode("魔犬の伝説",
            w.plot_turnpoint("$cherryから招待状がくる"),
            )


def first_murder(w: World):
    return w.episode("第一の殺人",
            w.plot_turnpoint("第一の殺人（犯罪研究家が死亡）が発生"),
            )


def second_murder(w: World):
    return w.episode("第二の殺人",
            w.plot_turnpoint("失踪した$mochが雑木林で遺体で発見される"),
            )


def trapped_in_castle(w: World):
    return w.episode("城壁の虜囚",
            w.plot_turnpoint(""),
            )


def dark_dogs_fang(w: World):
    return w.episode("魔犬の牙",
            w.plot_turnpoint(""),
            )


def dark_ritual(w: World):
    return w.episode("暗黒の儀式",
            w.plot_resolve(""),
            )


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
            w.plot_setup("その島では魔獣伝説が残っていた"),
            w.plot_setup("実際に近年も犬に食い殺されたような猟奇殺人が発生している"),
            w.plot_setup("$sherlockは特集記事を読みながらも怪奇伝説や幽霊は信じないと豪語する"),
            w.plot_turnpoint("$sherlockのもとにその孤島からパーティの紹介状が届く"),
            w.plot_develop("$sherlockたちは船で孤島に渡る"),
            w.plot_develop("城の主である$cherryは島に人が戻ってくるようにと、探偵や心霊研究家などに声を掛けて集めた"),
            w.plot_develop("それぞれ伝説について持論を展開する"),
            w.plot_develop("$sherlockは観光課の職員$mochに最初の事件があった場所に案内してもらう"),
            w.plot_develop("事件があった雑木林は立て札が立てられ、整備されてしまっていた"),
            w.plot_develop("観光課の$mochは観光によって人を呼び戻したいと言う"),
            w.plot_develop("夜、地元の学者からこの島がどこかの魔族の成れの果てが落ち延びてきた場所だと話す"),
            w.plot_turnpoint("翌朝、事件解決専門家が酷い姿で発見される"),
            w.plot_develop("警察を呼ぼうということになるが、海が荒れていて船を出せない"),
            w.plot_develop("元刑事は自分たちの力で問題解決しようと提案する"),
            w.plot_develop("心霊研究家は魔犬が出たと騒ぐ"),
            w.plot_develop("$sherlockは事件があった部屋を調べる"),
            w.plot_develop("確かに犬のような獣に仕業に見えたが、少し気になる部分があると$sherlockは言った"),
            w.plot_develop("$sherlockは$cherryに許可をもらい、城内を調べて回る"),
            w.plot_develop("古い城で、アンティークな鎧や槍、剣などの飾りがあった"),
            w.plot_turnpoint("何も情報が得られずホールに戻ると、元刑事が心霊研究家を犯人にしたてていた"),
            w.plot_develop("実は心霊研究家ではなく、詐欺師だったのだ"),
            w.plot_develop("その人物を個室に閉じ込めて、事件解決したことにした元刑事"),
            w.plot_develop("$sherlockは厨房に向かい、パーティのために呼ばれた料理担当と昨日のアリバイを聞く"),
            w.plot_develop("手配はすべて観光課の$mochが行ったと聞いた"),
            w.plot_develop("夜、情報を整理する$sherlock"),
            w.plot_turnpoint("翌朝、$mochが失踪した"),
            w.plot_develop("みんなで手分けして$mochを探す"),
            w.plot_develop("$mochは雑木林で惨殺死体になって発見された"),
            w.plot_develop("城に戻り、元刑事が犯人として閉じ込めた男の部屋を開けると、そこから血だけを残して人が消えていた"),
            w.plot_develop("本当に魔犬がいたのだという話になり、みんなおののいて、城から逃げ出す"),
            w.plot_develop("城に残った$sherlockは改めて城内を調査する"),
            w.plot_turnpoint("食堂でシェフと逃げた男の二人の死体を発見する"),
            w.plot_develop("他にも$cherryの姿もなくなり、殺されている恐れがあると城内を探す"),
            w.plot_develop("$sherlockは$wilsonに外に出た人たちに固まっているように伝えるよう命じて、自分は殺人鬼を探す"),
            w.plot_turnpoint("談話室に抜け道を見つけた"),
            w.plot_develop("地下室には拷問部屋があり、そこに残りの一人の遺体も見つかった"),
            w.plot_develop("またそこに本物の黒い獣の毛があった"),
            w.plot_develop("だが部屋に閉じ込められ、ガスを入れられる"),
            w.plot_develop("$sherlockは全てが$cherryの仕業と分かったが、動けなくなる"),
            w.plot_turnpoint("$maryが獣化し、扉をぶちやぶる"),
            w.plot_develop("しかし追い詰めた$cherryの前に本物の黒い魔犬が現れる"),
            w.plot_develop("$cherryを守ろうとした魔犬は$limeの起点により負傷し、逃げ出す"),
            w.plot_develop("魔犬に手間取っている間に$cherryは逃げ出してしまった"),
            w.plot_turnpoint("警察が島に到着する"),
            w.plot_develop("$wilsonが警察を連れて戻ってくる"),
            w.plot_develop("すぐに逃げた$cherryと魔犬を探すように言う"),
            w.plot_turnpoint("逃げた$cherryが魔犬に食い殺された無残な姿で発見され、その魔犬は警察により射殺された"),
            w.plot_resolve("犯人の死という形で事件は解決を迎えた"),
            w.plot_resolve("$cherryの部屋から日記が見つかり、それによってかつての飼い犬を復活させ、それが魔犬になったと書かれていた"),
            w.plot_resolve("事件後、$sherlockは城の地下に儀式を行った跡を見つけた"),
            w.plot_resolve("その儀式を教えたのが$cultXの関係者と分かる"),
            #
            legend_of_dark_dog(w),
            first_murder(w),
            second_murder(w),
            trapped_in_castle(w),
            dark_dogs_fang(w),
            dark_ritual(w),
            )


