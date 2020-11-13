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


# Episode
def lookfor_sherlock(w: World):
    return w.episode("$sherlockを探して",
            )


def empty_house(w: World):
    return w.episode("空き家の冒険",
            "$sherlockに似た人を空き家で見かけたという情報が入る",
            )


def secret_message(w: World):
    return w.episode("内緒の連絡",
            "$sherlock（偽物）に捕まえられて$maryたちは監禁される",
            )


def in_the_darkness(w: World):
    return w.episode("暗闇の中で",
            "刑事の一人が改造$gunを使って殺そうとしたところを逮捕",
            )


def his_alive(w: World):
    return w.episode("$sherlockは生きている",
            "$wilsonが指名手配される",
            )


def reunion(w: World):
    return w.episode("再会",
            "$wilsonが偽物だと$sherlockが教える",
            )


def strange_end(w: World):
    return w.episode("奇妙な結末",
            "$sherlockは偽$wilsonがまだどこかで生きているんじゃないかと疑う（何かを見つけて）",
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[7],
            w.plot_setup("$maryたちは$sherlockが生きていると信じて捜索を続けていた"),
            w.plot_turnpoint("$sherlockに似た人を空き家で見かけたという情報が入る"),
            w.plot_develop("空き家の調査を行い、そこで身元不明の遺体を発見する"),
            w.plot_turnpoint("空き家の遺体の犯人が$sherlockとして指名手配される"),
            w.plot_develop("$sherlockから$maryたちに秘密の連絡がある"),
            w.plot_turnpoint("$sherlock（偽物）に捕まえられ、$maryたちは監禁される"),
            w.plot_develop("$maryたちは暗闇に閉じ込められ、同じ手法で殺されそうになる"),
            w.plot_turnpoint("刑事の一人が改造$gunを使って殺そうとしたところを逮捕される"),
            w.plot_develop("助け出された$maryたちは$sherlockが生きていると$restradeから知らされる"),
            w.plot_turnpoint("$wilsonが指名手配される"),
            w.plot_develop("$sherlockと再会し、全ての事情を聞く"),
            w.plot_turnpoint("$wilsonが偽物だと$sherlockが教える"),
            w.plot_resolve("偽$wilsonが遺体となって発見された"),
            #
            lookfor_sherlock(w),
            empty_house(w),
            secret_message(w),
            his_alive(w),
            reunion(w),
            strange_end(w),
            "$sherlockを探して",
            w.plot_note("$maryたちは$sherclokを探し続けていた"),
            w.plot_note("しかし一月しても見つからないし、情報もなかった"),
            w.plot_note("$ignesら少年探偵団にも手伝ってもらっていたが何もない"),
            w.plot_note("ただ死体も何も発見されていないので、生きていると$maryは信じていた"),
            "$sherlockの噂",
            w.plot_note("ある日、$sherlockらしい人間を市場で見たという情報を$wilsonが持ってくる"),
            w.plot_note("調べていくと、幽霊騒動のあった空き家に入っていくのを見たということらしい"),
            w.plot_note("その空き家に向かう"),
            w.plot_note("空き家なはずなのに、夜になると電灯が灯り、確かに誰かの影を確認できた"),
            w.plot_note("しばらくそこを監視することにする$mary"),
            "偽物の再会",
            w.plot_note("$maryたちは空き家に侵入して$sherlockかどうか確かめることにする"),
            w.plot_note("夜を狙って空き家に入る"),
            w.plot_note("空き家の中にいたのは$sherlockの格好をした知らない男だった"),
            w.plot_note("そこで$maryは後ろから殴られ、気絶する"),
            "騙された",
            w.plot_note("目覚めると$maryと$limeは椅子にしばりつけられ、燃えている空き家のなかにいた"),
            w.plot_note("$maryは自分たちがピンチなのだけは理解できた。騙されたのだ"),
            w.plot_note("$wilsonは既に殺されたのだろうか"),
            w.plot_note("そこに男がやってくる"),
            w.plot_note("ずっと空き家の周囲をうろついていた浮浪者だ。やはり仲間だった"),
            w.plot_note("男はナイフを手にした"),
            "本当の再会",
            w.plot_note("男は$maryたちを助け、隠れ家へと連れて行く"),
            w.plot_note("そこで男は自分を$sherlockとばらす"),
            w.plot_note("そして$sherlockは$wilsonの所在を尋ねる"),
            w.plot_note("そこに情報が飛び込んでくる"),
            w.plot_note("魔獣がそこかしこで暴れているというのだ"),
            "$wilsonの行方",
            w.plot_note("$sherlockは$wilsonの住居を探す"),
            w.plot_note("そこは長い間人が住んでいないのが分かった"),
            w.plot_note("$wilsonに似た男が消えた場所の情報を手に入れ、そこに向かう"),
            w.plot_note("そこはあの宗教団体の一つの施設だった"),
            w.plot_note("そこの地下に向かう"),
            "黒幕",
            w.plot_note("そこには$wilsonを騙った男がいた"),
            w.plot_note("「来ると思っていた」と彼は言う"),
            w.plot_note("$wilsonではなく、名前すらないその存在は、闇の者だと語る"),
            w.plot_note("$bossを復活させることが目的で、そのために$hero関係者を殺し、その心臓を手に入れた"),
            w.plot_note("また$bossの$enagyを封じ込めた$stoneを手に入れる必要があった"),
            w.plot_note("残りは$sherlockの心臓だけだ、と語る"),
            w.plot_note("それは$sherlockこそが、探していた最後の$heroの血縁だからだ"),
            w.plot_note("その腕には$heroの紋章があった"),
            "最後の戦い",
            w.plot_note("$sherlockは周囲を囲まれ、あとがない"),
            w.plot_note("だがその時、水が大量に講堂に入り込んでくる"),
            w.plot_note("近所の川が決壊したのだ"),
            w.plot_note("その場にいた魔獣たちは溺れる"),
            w.plot_note("祭壇は崩れ、入ってきた警官隊により、$stoneはそれぞれ破壊され、水に流されてしまう"),
            w.plot_note("$wilsonと対峙した$sherlockは初めて見せる剣術で、その息の根を止めた"),
            w.plot_note("こうして全ての事件は終わった"),
            )


