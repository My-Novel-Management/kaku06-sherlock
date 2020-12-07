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
            mary.come(),
            lime.come(),
            mary.do("梯子を上がると、そこはどこかの廃工場の中だった"),
            mary.do("むわっと何かが腐った臭いが充満している"),
            mary.do("暗くてよく分からない"),
            mary.do("足元はぬめぬめしていた"),
            mary.do(""),
            # TODO
            )


def sherlocks_confession(w: World):
    return w.scene("$sherlockの告白",
            w.plot_note("$sherlockは自分の正体が「$moriano」だと告白する"),
            w.plot_note("実は二重人格で表は正義感を振りかざしながら裏では犯罪者として振る舞うことに快感を覚えるのだと"),
            w.plot_note("信じられない$maryは$sherlockが薬でおかしくなっているのだと考えた"),
            w.plot_note("獣化し、囲む敵と戦って逃げ出そうとする"),
            w.plot_note("しかし$wilsonを人質にとられてしまい、断念"),
            w.plot_note("おとなしく捕まった"),
            )


def in_the_darkness(w: World):
    return w.scene("暗闇の中で",
            w.plot_note("目覚めると真っ暗な中、縛られた状態で背中合わせだった$maryと$lime"),
            w.plot_note("妙な音が聞こえる"),
            w.plot_note("ぱっと明るくなり、ここがどこかの廃工場の中だと分かる"),
            w.plot_note("明るくなったのは炎だった"),
            w.plot_note("火事で事故死に見せかけて殺すつもりだと分かる"),
            )


def desparete_escape(w: World):
    return w.scene("決死の脱出劇",
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
            )


def hero_appairs(w: World):
    return w.scene("遅れてきた英雄",
            w.plot_note("発射した弾が何かにはじかれる"),
            w.plot_note("突入してきたのは一度見たことのあるホームレスの一人だった"),
            w.plot_note("彼が$maryたちを助け出してくれる"),
            w.plot_note("しかし警戒する$maryと$lime"),
            w.plot_note("ただ$maryはそのホームレスにどこか懐かしい匂いを感じる"),
            w.plot_note("彼は「$sherlockは生きている」と言い残して去っていった"),
            )
