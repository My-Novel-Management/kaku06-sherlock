# -*- coding: utf-8 -*-
'''
Stage: "空き家"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   シャーロックがいたと言われる空き家。ホワイト・チャペル地区のスラム街にある。比較的ガワが残っていて、隣の家のように崩れてはいない
#   [キッチン][バス]
#   [寝室][寝室]
#   [リビング][応接間]
#   [玄関]


# alias
HOME = "EmptyHouse"


# Scenes
## in Empty House
def strange_empty_house(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    return w.scene("奇妙な空き家",
            w.change_stage(HOME),
            w.change_time("afternoon"),
            w.plot_note("$wilsonに連れられて$maryと$limeは$sherlockに似た人を見たという空き家にやってくる"),
            w.plot_note("バラックが並ぶスラム街にあるたくさんの空き家の一つ"),
            w.plot_note("見たというホームレスは夜にその空き家だけ明かりがつくのが妙だと思って監視していたと証言する"),
            mary.be(),
            wil.be(),
            lime.be(),
            mary.do("$wilsonに連れられてその$sherlockがいたという空き家までやってくる"),
            mary.do("空き家はスラム街の同じようなバラックが並ぶ中にいくつかある一戸建ての家の一つだった"),
            mary.do("一部の窓ガラスは割れ、壁の色がはがれていたが、それでも屋根も落ちていないし、壁も崩れていない"),
            mary.do("$Sたちは斜向かいの空き家に入り、そこからその空き家を監視することにする"),
            mary.do("$wilsonが近所で何か食べ物と飲み物を仕入れてくると出ていく"),
            wil.go(),
            mary.do("$Sは$limeと二人で、$sherlockが何故こんな空き家で暮らしているのかを考える"),
            mary.think("もし生きているとして、仮に記憶喪失のような、自分が分からない状態なら、助けてもらった人と一緒に行動しているのも分かる"),
            mary.think("しかし$sherlockが正常で、いつものように深い思考を行える状態なら、ここで暮らしている理由が何かあるはずだった"),
            mary.think("彼はいつも言っていた。人の行動というものは深く考えていなかったとしても何かしらその人の思考が反映されていると"),
            mary.think("今$sherlockはあの空き家で暮らすべき事情を持っているのだ"),
            mary.think("一番考えられるのは「$morianoたちにバレない」ことだった"),
            mary.think("ただ$maryたちに知られてしまったら、たぶん、そこから伝わるだろう"),
            mary.do("$Sは$limeに自分たちがこのままここで待っていていいのだろうかと言う"),
            lime.do("$Sはもし何か考えがあるとしても、一旦合流した方がお互いに安心なんじゃないかと"),
            mary.think("どうすべきか考えていると、空き家の方で進展があった"),
            )


def resident_of_empty_house(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    return w.scene("空き家の住人",
            mary.be(),
            lime.be(),
            mary.talk("見て"),
            mary.do("向かいの空き家に男が入っていく"),
            mary.do("確かに着ているものはよく$sherlockが羽織っていたチェック柄のマントに帽子"),
            mary.do("しかしそんな目立つ格好でわざわざここに戻ってくるだろうか、と疑問"),
            mary.do("つまりわざと見つかるように、そうしているのだ、という考えにたどり着く"),
            wil.come("そこに$wilsonが戻ってくる"),
            wil.talk("ん？　$sherlockが入っていったのか。それじゃあやっぱり言っていたことは本当だったんだな"),
            mary.talk("わざとあんな目立つ格好してるんやと思うん", "誰かをおびき寄せてるんちゃうん？"),
            wil.talk("$morianoか", "そういえば$sherlockの手紙に気をつけろと書かれていたな"),
            wil.talk("じゃあこのまま監視して、$meたちが$morianoの残党を見つければいいんじゃないか"),
            mary.talk("そうすれば$sherlockとは早く会える？"),
            wil.talk("そうだな。きっと"),
            mary.do("じっと監視する$S"),
            wil.talk("ああ、これをどうぞ"),
            mary.do("$Sたちは$wilsonからもらったパンをかじる"),
            )


def searching_empty_house(w: World):
    return w.scene("空き家の探索",
            w.plot_note("一度空き家の中を探索するが、確かに人が暮らしている証拠が見つかる"),
            w.plot_note("$maryたちは夜になるのを待った"),
            )


def night_and_light(w: World):
    return w.scene("夜の明かりと人影",
            w.plot_note("空き家に人影が入り、そこで明かりが灯る"),
            w.plot_note("明かりの人影は読書しているように見えた"),
            w.plot_note("もう一人の人間もいるようで、二人で会話をしている風でもある"),
            w.plot_note("しばらくするとその明かりは消えてしまう"),
            w.plot_note("誰も出てこないので、翌朝、$maryたちはその空き家に訪問してみる"),
            )


def silent_house(w: World):
    return w.scene("静まる空き家",
            w.plot_note("呼びかけても応答はなく、奥に入っていく"),
            w.plot_note("空き家の中で殺された男性の死体を発見した"),
            w.plot_note("それは先月から行方不明の神官だった"),
            w.plot_note("現場からは$sherlockの愛用していた手袋が発見される"),
            w.plot_note("警察は$sherlockを重要参考人として指名手配する"),
            )


def re_searching_house(w: World):
    return w.scene("空き家の再調査",
            w.plot_note("そこで$wilsonは抜け道を発見する"),
            )


def mystery_subway(w: World):
    return w.scene("謎多き地下道",
            w.plot_note("地下道に繋がっていて、そこを進んでいく"),
            )
