# -*- coding: utf-8 -*-
'''
Stage: "廃工場"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# NOTE
#   廃工場。いろいろな死体が捨てられていた


FACTORY = "AbandonedFactory"


# Scenes
## in Empty House
def many_dead(w: World):
    mary, lime = w.get("mary"), w.get("lime")
    return w.scene("多くの遺体",
            w.change_camera("mary"),
            w.change_stage(FACTORY),
            w.plot_note("その地下道を抜けた先に廃工場があり、その中に失踪した多くの人間の遺体が放置されていた"),
            w.plot_note("そこで$sherlockと再会する"),
            "ここは$mary一人だけできたことにする",
            mary.come(),
            mary.do("梯子を上がると、そこはどこかの廃工場の中だった"),
            mary.do("むわっと何かが腐った臭いが充満している"),
            mary.do("暗くてよく分からない"),
            mary.do("足元はぬめぬめしていた"),
            mary.do("何か濡れている"),
            mary.do("そこに誰かが明かりを照らす"),
            mary.do("見ると$sherlockによく似たシルエットだが逆光になって分からない"),
            mary.do("$Sはその明かりで転がっているのが人の死体だと分かり、悲鳴を上げた"),
            mary.do("その男に口を押さえられ、強引に何か薬品をかがされて意識が消えた"),
            )


def sherlocks_confession(w: World):
    return w.scene("$sherlockの告白",
            # NOTE: ここはomitする
            w.plot_note("$sherlockは自分の正体が「$moriano」だと告白する"),
            w.plot_note("実は二重人格で表は正義感を振りかざしながら裏では犯罪者として振る舞うことに快感を覚えるのだと"),
            w.plot_note("信じられない$maryは$sherlockが薬でおかしくなっているのだと考えた"),
            w.plot_note("獣化し、囲む敵と戦って逃げ出そうとする"),
            w.plot_note("しかし$wilsonを人質にとられてしまい、断念"),
            w.plot_note("おとなしく捕まった"),
            )


def in_the_darkness(w: World):
    mary = w.get("mary")
    man = w.get("man")
    return w.scene("暗闇の中で",
            w.change_stage(FACTORY),
            w.plot_note("目覚めると真っ暗な中、縛られた状態で背中合わせだった$maryと$lime"),
            w.plot_note("妙な音が聞こえる"),
            w.plot_note("ぱっと明るくなり、ここがどこかの廃工場の中だと分かる"),
            w.plot_note("明るくなったのは炎だった"),
            w.plot_note("火事で事故死に見せかけて殺すつもりだと分かる"),
            mary.be("目覚めるとどこかの廃工場の中"),
            mary.do("暗くてよく分からないが、自分の手が後ろで縛られていて動けない"),
            mary.think("どうしよう、と焦るが、まずは$sherlockに教わったように情報を集めることだと、周囲を確認する"),
            mary.do("周囲を確認する"),
            mary.do("窓は閉ざされて薄暗く、それでも夜目の力を使わなくても見えるのは屋根の一部が崩壊しているから"),
            mary.do("ただ高くてとてもそこからは出られない"),
            mary.do("窓はトゲの針金で覆われ、出られなくされている"),
            mary.do("妙な臭いがした"),
            mary.do("可燃性の液体が広がっているのが分かる"),
            mary.do("そこに誰かやってくる"),
            man.come(),
            man.do("$sherlockによく似た男が、$maryを一瞥してから、火種を窓越しに投げ込んで走り去っていく"),
            mary.think("混乱する$mary"),
            mary.do("燃え広がる炎を前になすすべがない"),
            )


def desparete_escape(w: World):
    mary = w.get("mary")
    return w.scene("決死の脱出劇",
            w.change_camera("mary"),
            w.change_stage(FACTORY),
            w.plot_note("$maryは獣化して抜け出そうとするが、月の光が遮光されていて変身できない"),
            w.plot_note("$limeは仕込みナイフを使って縄を切ろうとするが、特殊な金属の縄で切れない"),
            w.plot_note("八方塞がりの中でも$sherlockの言葉を思い出して推理する"),
            w.plot_note("$wilsonはここにはいない"),
            w.plot_note("あの$sherlockが本物の$sherlockとは利き腕が違っていたことを思い出す"),
            w.plot_note("偽$sherlockがなぜ自分たちを陥れ、ここで火事で殺そうとしているのか考えると、全てを$sherlockにかぶせたい人間がいることに気づく"),
            w.plot_note("$maryはなんとか足だけ抜け出し、部屋から出ようとする"),
            w.plot_note("そこで闇から現れる銃口が自分を狙っていることに気づく"),
            w.plot_note("これが空き家の殺人の正体だった"),
            w.plot_note("$maryは撃たれそうになる$limeを庇って撃たれる"),
            mary.be("縛られたまま、炎に囲まれている"),
            mary.think("一旦冷静に落ち着こうと自分に話し掛ける"),
            mary.do("状況は最悪だった"),
            mary.do("炎の周りは早く、しかし、液体がかけられているのは周辺ばかりで蒸し風呂状態。逃げ場はない"),
            mary.do("獣化するにも月がなく、鉄格子の窓と有刺鉄線で囲まれているのを見て、脱出できないように細工されているのが分かった"),
            mary.do("けれど状況は詰みではないと、$sherlockが教えてくれている"),
            mary.do("わずかに空いた天井の隙間、そこに薄っすらと月が見える"),
            mary.do("ひとまず獣化し、鎖をちぎる"),
            mary.do("ただ炎の壁はどうしようもない"),
            mary.do("消化方法は、油だから、空気をなくすことだ"),
            mary.do("$Sは積み上げられていた鉄くずを炎の壁に投げ込んでいく"),
            mary.do("空気をなくせば炎は消える"),
            mary.do("加勢が弱まったのを見てハッチを開け、物置に潜り込む"),
            mary.do("爆薬を見つけて、それで爆破することを思いつく"),
            mary.do("置かれていた大型の金属製の箱に隠れることにして、火薬を導火線にしてその先に火薬詰めた樽を並べた"),
            mary.do("$Sは導火線との間の衝立をはずし、一気に箱に逃げ込む"),
            mary.do("大爆発した"),
            )


def hero_appairs(w: World):
    mary, lime = w.get("mary"), w.get("lime")
    shal = w.get("sherlock")
    ignes, pat = w.get("ignes"), w.get("patson")
    jake = w.get("jake")
    return w.scene("遅れてきた英雄",
            w.change_camera("lime"),
            w.change_stage(FACTORY),
            w.plot_note("発射した弾が何かにはじかれる"),
            w.plot_note("突入してきたのは一度見たことのあるホームレスの一人だった"),
            w.plot_note("彼が$maryたちを助け出してくれる"),
            w.plot_note("しかし警戒する$maryと$lime"),
            w.plot_note("ただ$maryはそのホームレスにどこか懐かしい匂いを感じる"),
            w.plot_note("彼は「$sherlockは生きている」と言い残して去っていった"),
            lime.come("燃え盛る瓦礫の山にかけつける$Sたち"),
            ignes.come(),
            pat.come(),
            lime.do("その炎の中で剣を手に戦っている人影を見つける"),
            shal.be(),
            jake.be(),
            lime.do("$sherlockと知らない男、だがよく彼に似ている男だった"),
            ignes.talk("$sherlock！"),
            shal.talk("$ignes！　そこの箱の中に$maryがいる！　すぐに助け出すんだ！"),
            ignes.talk("わかった"),
            ignes.do("箱に向かう$S"),
            pat.talk("一体どうなってるんだ……"),
            pat.do("状況が理解できずに呆然とする$S"),
            lime.do("$Sは$sherlockの加勢に向かう"),
            shal.talk("ありがとう。$meは肉体労働は苦手なんだ"),
            lime.do("$Sにより組み伏せられる$jake"),
            shal.talk("この男がね、連続誘拐犯だよ", "それも$ajinだ"),
            shal.do("$Sはそう言って、男の覆面を外す"),
            shal.do("そこには獣の毛がびっしりと生えていて、ひと目で$animalだと分かった"),
            )
