# -*- coding: utf-8 -*-
'''
Stage: "市場"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   立っている市場はどこでもここを使う。基本は古くから立っている賑わいのあるバラ市場


# alias
MARKET = "Market"


## scenes
def mystery_of_aily_corpse(w: World):
    return w.scene("$aily家の遺体の謎",
            w.plot_note("ただ謎の殺人事件と消えた$ailyについての謎が残った"),
            )


def shopping_enjoy(w: World):
    return w.scene("楽しいお買い物",
            w.plot_note("$maryは料理はあいかわらず下手だが、それでもよく市場に顔を出して買い物をしていた"),
            w.plot_note("$maryは今日も市場に出かける"),
            w.plot_note("この町の市場の賑わいが$maryは好きだった"),
            w.plot_note("市場には少年探偵団の$ignesも働いている"),
            w.plot_note("最近仲良くなった果物屋の$nowlisから友人からガチョウをもらったと言ってそれを分けてもらえた"),
            w.plot_note("$maryはガチョウを持って帰る"),
            )


def wanted_jack(w: World):
    return w.scene("$jackが指名手配",
            w.plot_note("$jackが改めてその殺人事件の容疑者として手配される"),
            )


def goose_jewely_mystery(w: World):
    return w.scene("ガチョウの宝石の謎",
            w.plot_note("その間に$maryたちはガチョウの中から出てくる宝石の謎を追いかける"),
            )


def meatshop_talk(w: World):
    return w.scene("肉屋の話",
            w.plot_note("肉屋の主人からどこでガチョウを仕入れてくるのかを聞いた"),
            w.plot_note("その経路を辿っていくと、飼育業者がその一箇所だと断定できた"),
            )


def wholesaler_talk(w: World):
    return w.scene("卸売業者の話",
            w.plot_note("飼育業者のおじさんに聞いてもダイヤを餌に混ぜたりはしていないと"),
            w.plot_note("仲介業者も卸業者も全然入る余地がなく、結局何も情報を得られないまま帰ってきた"),
            )


def strange_letter(w: World):
    return w.scene("奇妙な手紙",
            w.plot_note("$maryは市場からの帰り道、知らない男から手紙を渡される"),
            w.plot_note("手紙は$morianoから君の悩みの相談に乗ろうというものだった"),
            w.plot_note("$maryはその日、帰ってこなかった"),
            )


## in Empty House
def shal_disappearance_talk(w: World):
    mary = w.get("mary")
    ignes, nowl = w.get("ignes"), w.get("nowlis")
    return w.scene("$sherlockの失踪について",
            w.change_stage(MARKET),
            w.change_time("midmorning"),
            mary.come("市場にやってくる$S"),
            ignes.be("$Sが客引きをしている"),
            ignes.talk("おう$maryちゃん。何か探してる？"),
            mary.talk("おはよう", "$k_shal一人くらいいおらんかな？"),
            ignes.talk("$meらも探してはいるんだけどよ、どうにも情報ないんだわ",
                "結構ネットワークあるんだけど、全然ひっかからねえ"),
            ignes.do("$Sたち少年団も困っていた",
                "彼らは必死にホームレスや少年少女のネットワークを通して情報収集をしてくれていたが、いつものように$sherlockの情報は集まらない"),
            mary.do("ありがとう、といってから、市場を見て歩く"),
            mary.do("最近市場に並ぶものが物騒なものが増えてきていた"),
            mary.do("事件件数もうなぎのぼりで、警察も大変だと$k_patが愚痴っていた"),
            mary.do("$sherlockがいなくなったことで、未解決事件も増え、警察も人員が足りないといっていた"),
            nowl.be("肉屋の$Sがにこやかに声をかける"),
            nowl.talk("お肉買ってく？　今日はちょっといいのが入ってね"),
            mary.talk("$nowlisさん、おはようございます"),
            nowl.talk("なんだ元気ないね。やっぱりあの行方不明になってる？"),
            mary.talk("$nowlisさんだけは死んだって言わないんですね"),
            nowl.talk("だって$maryちゃんは信じてないんだろう？　だったら$meも信じない"),
            mary.talk("ありがとうございます"),
            mary.do("不思議な感じがする相手だった"),
            )


def new_religions(w: World):
    mary = w.get("mary")
    man = w.get("man")
    return w.scene("新興宗教",
            mary.come("市場で買い物を済ませて帰ろうとしている$S"),
            man.be("紺色に染めたフードをかぶった男が配りものをしている"),
            # TODO
            )


## in Epilogue
def social_condition(w: World):
    mary = w.get("mary")
    ignes = w.get("ignes")
    return w.scene("事件後の社会情勢",
            w.change_camera("mary"),
            w.change_stage("Market"),
            mary.come("市場にやってくる$S"),
            mary.do("市場はいつもとおりの賑わい"),
            ignes.be("仲間たちと笑いながらうろついている$S"),
            mary.talk("あ、$ignes"),
            ignes.talk("おう、$maryさんか", "買い物？"),
            mary.talk("うん"),
            mary.do("話を聞くと少年探偵団もそれなりに小さな問題を解決して、ちょっと名が上がったと"),
            mary.think("肉屋の主人の姿を見なくて、あれ？と感じる"),
            )

