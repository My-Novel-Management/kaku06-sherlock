# -*- coding: utf-8 -*-
'''
Episode 7-4
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


# DEFINE
TITLE = "$bossの復活"


# NOTE: outlines
ABSTRACT = """
$sherlockは$maryが$patsonにより連れ出されたと知り、急いで改装中の大聖堂へと向かう。そこが$boss復活の儀式を行う場所だと言う。
大聖堂の地下には巨大なホールが広がっていた。そこはかつて$bossの居城があった場所で、封印する目的で聖堂を建てたのが今の大聖堂の元になったと説明する。
待ち構えていた$patsonは$maryを人質にして、残り一つの「捧げもの」を$sherlockに要求する。それは$heroの血液だった。
$sherlockの家を荒らしたのは$patsonだった。$sherlockが$heroだと知った彼が血液の研究をしていたのを知っての犯行だ。しかし既に$sherlockが処分した後だった。
$patsonも一部に$ajinの血が入っており、苦しい幼少期を経て今があった。$boss復活すれば$ajin優遇の世界がくると信じていた。
だが$sherlockにより過去、$bossがいた時代の$ajinの扱いがどんなに酷いものだったかが語られる。
$gunを打って$sherlockを負傷させ、$maryを人質に、その血を盃に入れさせた。
$patsonにより、$boss復活の儀式が始まった。
"""


# Episode
def main(w: World):
    return w.episode(TITLE,
            # NOTE
            w.plot_setup("$patsonが裏切り者だった。$boss復活の儀式を行うために$maryを誘拐し、改装中の大聖堂に向かう"),
            w.plot_turnpoint("改装中の大聖堂に、地下に繋がる階段が見つかった"),
            w.plot_develop("$patsonは儀式を行うために$maryを盾にして脅す。必要な祭具の残り一つが分からなかったが$sherlockによりそれが$heroの血であることを教えられる"),
            w.plot_turnpoint("$sherlockは真の$heroだった"),
            w.plot_resolve("道具が揃った$patosonは$boss復活の儀式を開始した"),
            w.plot_turnpoint("だが儀式は途中で失敗する"),
            w.plot_note("$wilsonにより$patsonは殺された"),
            w.plot_note("それを驚きの目で見ている$sherlock"),
            w.plot_note("$patsonが手にしていた古書を拾い上げる$wilson"),
            w.plot_note("$wilsonは$sherlockにどうやって$bossを復活させるのか尋ねる"),
            w.plot_note("$sherlockは自分が知っているのは必要な祭具を整え、場所はこの元$bossの城があった場所で、封印を解く呪文を唱えること"),
            w.plot_note("ただそれでは以前失敗した、と語る"),
            w.plot_note("$steinの研究によれば必要な祭具は四つある$stoneであること"),
            w.plot_note("四つの$stoneが集められた"),
            w.plot_note("それにより行われたのが前回の地震分。それも失敗だった"),
            w.plot_note("しかしもう一つ重要なものが欠けていることが判明する"),
            w.plot_note("それが$heroの血をもつ者の体だった。$bossの魂を呼び戻すにはその器が必要となる"),
            w.plot_note("$steinはそれが$heroの体であろうと書かれていた"),
            w.plot_note("そして$wilsonは$maryを人質にし、$sherlockに台座に立つように言う"),
            w.plot_note("すべてを動かしていたのは$wilsonだった"),
            w.plot_note("王の命令なのか？　と疑うが、$wilsonは違うと言う"),
            w.plot_note("$sherlockは「じゃあやはり君は$wilsonではなかったんだな」と"),
            w.plot_note("$wilsonは偽物だった。$zeronと名乗り、正体をばらす"),
            w.plot_note("ずっと潜伏し、どうすれば$bossが復活できるのか、それを調べていた。機会があれば実行した"),
            w.plot_note("ただそのための装置として誕生し、その大いなる意志に従った"),
            w.plot_note("$morianoという男を利用し、様々なタネをまいた"),
            w.plot_note("最終目的が世界の救済ということで$boss復活を掲げる教団$cultXもまたその一つだった"),
            w.plot_note("実際$stoneを手に入れ、儀式も行った。だがすべて失敗に終わった"),
            w.plot_note("器となる人間が$heroの血を引いたものでないといけないと分かり、今度は$heroを探した"),
            w.plot_note("それが$sherlockだと分かったが、その時には$morianoと対決し、滝壺に落ちて行方不明になってしまった"),
            w.plot_note("その後、手を尽くして他の候補者を探しながらも、$sherlockの行方も探した"),
            w.plot_note("$sherlockが生存していた情報を掴み、陽動するために偽の空き家目撃情報を流した"),
            w.plot_note("それでも動きがなく、$maryたちを巻き込んだ"),
            w.plot_note("結果的には今ここに$sherlockが揃い、よかったと語る"),
            w.plot_note("儀式が始まる"),
            w.plot_note("目覚める$mary"),
            w.plot_note("$sherlockの体に$stoneから次々に$bossの力が注ぎ込まれていく"),
            w.plot_note("しかし$blue_stoneに至った時だった"),
            w.plot_note("$blue_stoneは弾け飛ぶ"),
            w.plot_note("それは精巧に作られた偽物だったからだ"),
            #
            w.plot_note("$wilsonは「またか」と落胆する"),
            w.plot_note("「知っていたのか」と$sherlockに"),
            w.plot_note("「彼女が本物を渡すような真似はしないと分かっていた」と"),
            w.plot_note("そのことは自分を助けてくれた時に匿ってくれた隠れ家で個人的に確認したと"),
            w.plot_note("ただ本当にそれで防げるかどうかは賭けだった"),
            w.plot_note("負傷し、肉体の半分が消えた$zeron"),
            w.plot_note("$sherlockにどこで偽物と分かったのか、と"),
            w.plot_note("$sherlockは$wilsonの家にいった時に、そうじゃないかと分かった"),
            w.plot_note("ただどこかおかしいというのは一番最初の日から分かっていたと"),
            w.plot_note("$adelに対しての態度が完全に初対面だった"),
            w.plot_note("エージェントであり、何度か王宮にもでかけているといっていたが、$adelがそれを記憶していないのはおかしいのだ"),
            w.plot_note("注意深くなりすましたつもりだったのに、そんなことで見破られるとは"),
            w.plot_note("完敗だという$zeronだったが、爆薬をつかい、その場から逃げ出す"),
            w.plot_note("$maryは$sherlockを守った"),
            w.plot_note("こうして一連の事件は終わりを迎えた、かに思えた"),
            outline=ABSTRACT)

