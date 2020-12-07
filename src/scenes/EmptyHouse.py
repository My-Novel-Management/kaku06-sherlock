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


def night_and_light(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    man = w.get("man")
    return w.scene("夜の明かりと人影",
            w.change_time("night"),
            w.plot_note("空き家に人影が入り、そこで明かりが灯る"),
            w.plot_note("明かりの人影は読書しているように見えた"),
            w.plot_note("もう一人の人間もいるようで、二人で会話をしている風でもある"),
            w.plot_note("しばらくするとその明かりは消えてしまう"),
            w.plot_note("誰も出てこないので、翌朝、$maryたちはその空き家に訪問してみる"),
            mary.be(),
            lime.be(),
            mary.do("結局そのまま動きがなく夜になる"),
            wil.come("外から戻ってくる$S"),
            wil.talk("何か進展は？"),
            lime.do("首を振る$S"),
            wil.talk("見回ってきたが特に怪しげな人物はいなかったよ", "たぶんまだ$sherlockの存在に気づいているのは$meたちだけなんだろう"),
            mary.do("見ているとうっすらと明かりが灯る部屋がある"),
            mary.do("シルエット越しに、いつも$sherlockが椅子に座って本を読んでいる姿が見える"),
            mary.talk("何してるんやろ"),
            wil.talk("さあね"),
            wil.talk("しばらくこのまま見ておくから、君たちは少し眠るといい"),
            mary.talk("ありがとう、$wilsonさん"),
            )


def silent_house(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    man = w.get("man")
    return w.scene("静まる空き家",
            w.change_time("midnight"),
            w.plot_note("呼びかけても応答はなく、奥に入っていく"),
            w.plot_note("空き家の中で殺された男性の死体を発見した"),
            w.plot_note("それは先月から行方不明の神官だった"),
            w.plot_note("現場からは$sherlockの愛用していた手袋が発見される"),
            w.plot_note("警察は$sherlockを重要参考人として指名手配する"),
            wil.be(),
            mary.be(),
            lime.be(),
            wil.talk("なんだ？"),
            mary.do("$wilsonの声で目覚める"),
            mary.do("$wilsonに言われて見てみると、明かりがついた部屋で二人の人影が争っている風"),
            mary.talk("どうしたん？"),
            wil.talk("わからない。少し目を離したすきにああなってて"),
            mary.do("と、何かが割れる音がして、明かりが消えた"),
            mary.do("しばらく待っていたが静かなままだった"),
            mary.think("どうしようと考える"),
            mary.think("もし$sherlockに危険が及んでいるなら助けに行かないといけないけれど、自分たちが出ていって本当の危険が及ぶのも恐い"),
            wil.talk("様子を見てくる"),
            wil.go("だが$Sが先に出ていってしまう"),
            mary.talk("$meらも"),
            mary.go("$Sと$limeも続いた"),
            lime.go(),
            )


def discover_dead(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    return w.scene("遺体の発見",
            mary.come("$Sたちは空き家に侵入する"),
            wil.come(),
            lime.come(),
            mary.do("先頭をいく$wilsonのオイルライターを光源にして、進む"),
            mary.do("ドアは施錠されていなく、少し開けられていた"),
            mary.do("中は一般的な一戸建てで、玄関に続いてリビングといくつか部屋がある構造らしい"),
            mary.do("$Sたちが見ていたのはリビングの隣の書斎らしく、しかし、そこのドアが開け放たれている"),
            wil.talk("いいか"),
            wil.do("$Sが確認してから、中を照らす"),
            mary.do("そこに黒い人形が倒れているのを見つけて、$Sは悲鳴を上げた"),
            )


def searching_house(w: World):
    mary, wil, lime = w.get("mary"), w.get("wilson"), w.get("lime")
    return w.scene("空き家の再調査",
            w.change_stage(HOME),
            w.change_time("midmorning"),
            w.plot_note("そこで$wilsonは抜け道を発見する"),
            mary.come("$Sは一人で空き家にやってくる"),
            mary.do("入り口に警官が立っていて、中に入れないでいる"),
            mary.do("しかし近所のホームレスが揉め事をはじめて、その間に持ち場を離れてしまう"),
            mary.do("$Sはそのすきに家の中に入る"),
            mary.do("中は既に警察が調べた後だった"),
            mary.do("遺体はなくなっていて、そこに遺体の形にチョークでかかれている"),
            )


def mystery_subway(w: World):
    return w.scene("謎多き地下道",
            w.plot_note("地下道に繋がっていて、そこを進んでいく"),
            )
