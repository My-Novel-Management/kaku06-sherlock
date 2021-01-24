# -*- coding: utf-8 -*-
'''
Episode 5-5
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "悲しみの結末"


# NOTE: outlines
ABSTRACT = """
伝説の魔犬が存在していたのだと騒ぐ$jamos。だが魔犬は襲いかかってくることはなく、$maryにじゃれつく。
それを外から見ていたのは城主の$cherryで、彼女は魔犬が$sherlockたちを食わないことに腹をたて、睡眠ガスを部屋に送り込もうとするが、$sherlockの機転により阻止される。
全ての事件が$cherryの手により行われたものだと言った$sherlockに対し、$cherryは皆殺しにしようと襲いかかってくるが、$maryと$limeにによって阻止される。
逃げ出した魔犬を追って$cherryも部屋から出た。
部屋に閉じ込められた$sherlockたちは何とか部屋から脱出し、$cherryを探す。
途中でやっと上陸できた警察と合流した。
$cherryは雑木林で魔犬に食われて亡くなっていて、魔犬は警察により射殺された。
$sherlockは$cherryが魔犬の餌にするために人殺しを行っていたのだと語る。
後日、地下の別の部屋から闇の技法を用いて愛犬を復活させたと考えられる儀式の形跡が見つかった。そしてその資金の為に所有していた$black_stoneが闇マーケットに売られていたことが判明した。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("本当に魔獣の仕業だったと騒ぎ立てるが$sherlockは殺人が犬の仕業ではないことを伝えて、隠れていた$cherryを呼び出した"),
            w.plot_turnpoint("$cherryは自分が犬にやるために人を殺したと告白する"),
            w.plot_develop("$cherryは自分の罪を告白しながらも部屋に毒ガスをまこうとするが、犬が共倒れになりそうになって中止し、犬とともに逃亡する"),
            w.plot_turnpoint("$cherryが犬に食い殺されているのが発見された"),
            w.plot_resolve("事件は$cherryの死により結末を迎えた。後日城の地下で儀式の跡が見つかった"),
            w.plot_note("大きな黒い魔獣を前にして$maryは$animal化し、戦おうとする"),
            w.plot_note("だがそこに「待って！」と声をかけて現れる$cherry"),
            w.plot_note("彼女は$maryと獣の間に割って入る"),
            w.plot_note("守るではなく、まるで対峙するように間に立った"),
            w.plot_note("$cherryは「この子は安全だから」と言う"),
            w.plot_note("$wilsonが殺したのはその獣じゃないのかと尋ねたが、彼女はそれを強く否定した"),
            w.plot_note("$maryが「事情があるなら話して欲しい。力になれるならなりたい」と"),
            w.plot_note("$cherryは「あなたたちには言っても理解してもらえない」"),
            w.plot_note("とにかくもうここを出ていって欲しいという。それがお互いにとって一番いいと"),
            w.plot_note("「でも人が死んでる。そのままにしておけない」と$mary"),
            w.plot_note("「この島ではずっとこうしてきた。だからこれからも……よそ者は入れないでいい」"),
            w.plot_note("$maryは$cherryが犯人だということが分かってしまう"),
            w.plot_note("$cherryさんが殺したんですね？　と"),
            w.plot_note("彼女はやっていないと言う"),
            w.plot_note("そこに$sherlockたちが駆けつける"),
            w.plot_note("$sherlockは「これ以上手を汚すことはない」と$cherryに忠告する"),
            w.plot_note("そして$doldのことを呼び出し、彼が真犯人だと言った"),
            w.plot_note("「あなたが$baskervillesの末裔ですね」と"),
            w.plot_note("$doldは「小さな食堂のシェフだよ」と答えるが、$cherryが「もういいじゃないの」と"),
            w.plot_note("$sherlockは事前に参加者を調べていた"),
            w.plot_note("確かに地元で食堂をやっているが$doldは$cherryの兄だった。腹違いの"),
            w.plot_note("$mochと三人で共謀し、ここに有名人を集めて殺人ショーを行おうとした"),
            w.plot_note("だが$mochが殺されているところから、何か仲間割れがあったか、計画の変更があったか、もともとその予定だったか"),
            w.plot_note("$mochを殺したのは探しに出た$doldで確定"),
            w.plot_note("ただ他の何人かについては$cherryの可能性が高くなる"),
            w.plot_note("殺害するときはここの道具を使い、魔獣に殺されたように見せかけている"),
            w.plot_note("しかしかならず殴打した形跡があり、死後に傷つけている"),
            w.plot_note("遺体が損壊しているのは、その一部を持ち去ったからだ"),
            w.plot_note("この部屋を見て、犬の餌にしているのだと分かった"),
            w.plot_note("そこまで$sherlockが一気に語る"),
            w.plot_note("$doldは$cherryの愛犬が人しか食わないから仕方なかった、と語る"),
            w.plot_note("本当は今回の計画にまぎれて$mochだけ始末できればよかったと"),
            w.plot_note("$doldが全てやったと語る"),
            w.plot_note("けれど$maryは言った。獣の方からじゃなく、$maryの方から臭いがすると"),
            w.plot_note("$sherlockは「信じたくはないが本当に人を食うことになるようだな」と$cherryを見て言う"),
            w.plot_note("$sherlockは自分が調べている古代の技法には、死んだものを復活させる技がある"),
            w.plot_note("ただしそうやって蘇ったものは定期的に生きているものの命を喰らう必要がある、と"),
            w.plot_note("$doldは「だから愛犬を蘇らせて、犬にだな」と"),
            w.plot_note("$sherlockは否定する。「犬なら犬でいいんです。何故人なのか。それは蘇ったのが$cherryさんだからですよ」"),
            w.plot_note("$maryは驚く"),
            w.plot_note("しかし$cherryは本性を現した"),
            w.plot_note("人の姿をした、獣。魔獣だった"),
            w.plot_note("$cherryは逃げ出す"),
            w.plot_note("$doldが部屋をしめている間に、逃した"),
            w.plot_note("「もう長く生きられない。頼むから見逃してやってくれないか」"),
            w.plot_note("$mochから定期的に殺人ツアーをやればいいと言われ、それに一旦は乗ったが、結局人殺しを何度すればいいか考えると無理だった"),
            w.plot_note("犬は大人しくしている"),
            w.plot_note("それでも$sherlockは言う。「ちゃんと殺すべきだ」と"),
            #
            w.plot_note("地下室を出て、外に出る"),
            w.plot_note("犬に走らせる"),
            w.plot_note("ついていくと雑木林のところで日光に照らされて骨と化していく$cherryを見つけた"),
            w.plot_note("その$cherryに自分を食えと$doldが差し出す"),
            w.plot_note("だが$cherryは「もういいよ、にいさん」と。消えていった"),
            #
            w.plot_note("事件は終わった"),
            w.plot_note("概ね$sherlockの推理した通りだったが、一月前の殺人は$mochによるものだった。それにより人を殺すことの快楽を覚えたそうだ"),
            w.plot_note("$sherlockは$maryに言う。オカルトよりも本当に恐いのは、そこにリアルにある人の意志だと"),
            outline=ABSTRACT)

