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


# Episodes
def mary_and_market(w: World):
    return w.episode("$maryと市場",
            w.plot_note("$limeも同居するようになり、$sherlockの家で暮らす人数が増えた"),
            w.plot_note("$maryは料理はあいかわらず下手だが、それでもよく市場に顔を出して買い物をしていた"),
            w.plot_note("$maryは今日も市場に出かける"),
            w.plot_note("この町の市場の賑わいが$maryは好きだった"),
            w.plot_note("市場には少年探偵団の$ignesも働いている"),
            w.plot_note("最近仲良くなった果物屋の$nowlisから友人からガチョウをもらったと言ってそれを分けてもらえた"),
            w.plot_note("$maryはガチョウを持って帰る"),
            w.plot_note("$limeは料理担当になっていて、そのガチョウをもらってさばいてくれる"),
            w.plot_note("$maryは市場で仕入れた面白い話を$sherlockに話す"),
            w.plot_note("今市場ではガチョウからダイヤが出てくると話題になっていた"),
            w.plot_note("$limeがやってきて、何か出たという"),
            w.plot_note("ガチョウの中から出てきたのは血がついたナイフだった"),
            )


def strange_goose(w: World):
    return w.episode("奇妙なガチョウ",
            w.plot_note("$sherlockはそれがなにかの事件の凶器だと分かり、すぐに警察に連絡を取る"),
            w.plot_note("$restradeがやってきて、それは現在彼が追っている事件の重要な証拠品だと言われた"),
            w.plot_note("$restradeからその事件についての概要を聞く"),
            w.plot_note("事件はある一軒家で起こった"),
            w.plot_note("引退した学者が謎の死を遂げた"),
            w.plot_note("刺殺だったのだが凶器が発見されず、犯人も特定されないまま現在に至る"),
            w.plot_note("そのナイフを警部に渡して調べてもらう"),
            w.plot_note("その間に興味をもった$sherlockは一人でその現場を調べに出ていってしまう"),
            w.plot_note("後日、そのナイフからずっと失踪中の$jackの指紋が検出された"),
            )


def suspect_jack(w: World):
    return w.episode("$jackが容疑者",
            w.plot_note("$jackが改めてその殺人事件の容疑者として手配される"),
            w.plot_note("戻ってきた$sherlockは$maryからそのことを聞き、"),
            w.plot_note("$sherlockは現場を見てきたことを$maryたちに話す"),
            w.plot_note("現場は住宅街から少し離れた郊外の一軒家で、男は民間の研究所をやめたあとも個人的に何かを研究していた"),
            w.plot_note("歴史学と民俗学に造形が深く、$sherlockもその所蔵していた資料に関心をしたくらい"),
            w.plot_note("彼が書き残しているものの一つに古代の技法がいくつか紹介されていた"),
            w.plot_note("刺された場所は彼の家だが、凶器は消えている"),
            w.plot_note("ただし$jackとの関係性は全く見えず、彼女ならそんな手段を使わないと$sherlockは考えた"),
            w.plot_note("$sherlockは誰かが$jackを表舞台に引っ張り出したい、その罠だと考える"),
            w.plot_note("と、差出人不明の手紙に$jackからのメッセージがあった"),
            w.plot_note("助けてほしいと"),
            )


def whereabouts(w: World):
    return w.episode("彼女の行方",
            "$jackからのメッセージを見つけた",
            # TODO
            )


def reunion_her(w: World):
    return w.episode("彼女との再会",
            "$jackは自分がはめられたことを告白した",
            )


def her_message(w: World):
    return w.episode("彼女からのメッセージ",
            "$jackは$sherlockに$stoneを託して、しばらく世間から姿を消すと言い残して、去っていった",
            w.plot_note("$jackは自分が狙われた原因が$stoneにあると、それを見せる"),
            w.plot_note(""),
            w.plot_note("$jackは$sherlockに$stoneを渡す"),
            w.plot_note("誰かがこれを四つ集めて何かしようと企んでいると告げる"),
            w.plot_note("$sherlockになんとしてもそれを阻止してほしいと頼み、彼女は姿を消す"),
            w.plot_note("$sherlockはその$stoneを見ながら考え込んだ"),
            )


# Chapter
def main(w: World):
    return w.chapter(TITLES[4],
            w.plot_setup("$maryは市場の人間と仲良くなり、色々ともらってくるようになっていた"),
            w.plot_turnpoint("市場からもらったガチョウに$stoneと血の付着したナイフが入っているのを発見する"),
            w.plot_develop("殺人事件の凶器と分かり、$maryの友人（市場の男）に容疑がかかる"),
            w.plot_turnpoint("遺体が$jackの仲間と判明する"),
            w.plot_develop("ガチョウの仕入れ先を調べて$jackの関連が浮かび上がる"),
            w.plot_turnpoint("$jackが容疑者として浮上する"),
            w.plot_develop("$jackの行方を探す"),
            w.plot_turnpoint("$ailyから手紙（暗号文）が届く"),
            w.plot_develop("$sherlockは$ailyが事件に関係あると考えて、彼女に会いに行く"),
            w.plot_turnpoint("$sherlockは$jackが犯人でないと知る"),
            w.plot_resolve("$jackは$sherlockに隠し持っていた$stoneを渡して目的阻止を依頼した"),
            mary_and_market(w),
            strange_goose(w),
            suspect_jack(w),
            whereabouts(w),
            reunion_her(w),
            her_message(w),
            "もらったニワトリ",
            w.plot_note("市場から$maryがニワトリをもらってくる"),
            w.plot_note("しかし$sherlockは肉になる前の動物は苦手だという"),
            w.plot_note("$wilsonがニワトリをさばこうと言ってくれる"),
            w.plot_note(""),
            "持ち主は誰だ",
            w.plot_note("市場に向かい、持ち主を探すことにする"),
            "$jackとの再会",
            w.plot_note("そのガーネットについての情報を持っているという謎のタレコミの手紙が届く"),
            w.plot_note("$sherlockは一人、その場所に向かう"),
            w.plot_note("待っていたのは$ailyこと$jackだった"),
            w.plot_note("死んだとは思っていなかったが戻ってくるとは思ってなかった$sherlock"),
            w.plot_note("「一度ちゃんとデートをしたいと言ったでしょう」と$jack"),
            w.plot_note("付き合って欲しい場所があると、日時と場所を指定した$jackのカードを渡される"),
            "$jackとデート",
            w.plot_note("博物館の改築が終わり、そこを見る"),
            w.plot_note("盗まれたことを内緒にしてダミーの宝石が飾られている"),
            w.plot_note("$heroに関しての四つの宝石があり、その一つが宝剣についていたもので、"),
            # NOTE:４つの宝石考える
            w.plot_note("残りの一つがあのニワトリに飲み込まれてしまったガーネットだという"),
            w.plot_note("盗み出したものの、それを持ち運ぶために一旦ニワトリに飲み込ませたが、そのニワトリが混ざってしまい、市場に流れた"),
            w.plot_note("それをたまたま$maryがもらったのがことの発端だった"),
            w.plot_note("宝石を返してもらえるかしら、と$jack"),
            w.plot_note("$sherlockは何故そこまで四つの宝石を必要とするのかを知ることと引き換えに渡すと言い出す"),
            w.plot_note("彼女は「大切なものを取り戻すため」としか答えない"),
            w.plot_note("$sherlockは他にもこの宝石を狙っている勢力があることを伝えて、手を引くように忠告する"),
            w.plot_note("しかし$sherlockは$jackが準備した男たちに取り囲まれ、仕方なく持ってきていたガーネットを渡した"),
            "殺人事件",
            w.plot_note("翌日、川で謎の女性の死体が上がる"),
            w.plot_note("身元不明だったが背格好から逃亡中の$ailyだと推測された"),
            w.plot_note("持ち物はなく、あのガーネットも消えてしまっていた"),
            "事件の顛末",
            w.plot_note("$sherlockのもとに手紙が届く"),
            w.plot_note("差出人名はなかったがそれが$jackのものと分かる"),
            w.plot_note("手紙にはひょっとしたら殺されるかも知れないと書いてある"),
            w.plot_note("内容は$sherlockにその場では話せないと言ったことについてだった"),
            w.plot_note("大昔の秘術で亡くなった人間を蘇らせるというものがあり、それに利用するために高$enagyを閉じ込めた媒体が必要"),
            w.plot_note("それが四つの宝石だった"),
            w.plot_note("これで行方の知れない残り１つの宝石を、謎の勢力が探すことになるだろうと"),
            w.plot_note("$sherlockは自分の情報網にフェイクの情報を流して、その勢力と動きをあぶり出すことにした"),
            )


